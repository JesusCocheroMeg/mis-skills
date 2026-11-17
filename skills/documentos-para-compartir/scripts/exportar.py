#!/usr/bin/env python3
"""Exporta un documento de láminas a HTML autónomo y a PDF de 1280×720.

Uso:
  python3 exportar.py FUENTE.html --salida DIR --nombre NOMBRE [--fuente-pdf OTRA.html] [--zoom-min 0.72]

FUENTE.html es el fragmento que también se publica como artefacto: <title>, <link> de fuentes,
<style> y <main class="deck"> con una <section class="slide"> por lámina.

Qué hace:
  1. Escribe DIR/NOMBRE.html (el fragmento envuelto en un documento completo con <!doctype>).
  2. Mide cada lámina en Chrome sin interfaz a varios anchos y elige, por lámina, el zoom más
     grande con el que cabe en 1280×720. Así la letra queda lo más grande posible en cada página.
  3. Si una lámina no cabe ni con el zoom mínimo, la lista y NO genera el PDF (código de salida 2):
     hay que dividirla en la fuente del PDF (--fuente-pdf) o recortar texto.
  4. Escribe DIR/NOMBRE.pdf y muestra cuántas páginas tiene.

--fuente-pdf permite usar para el PDF una versión con las láminas largas divididas, sin tocar la
versión web, que se lee de arriba abajo y no tiene límite de alto.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
IMPRESION = os.path.join(AQUI, '..', 'assets', 'impresion.css')
ANCHO, ALTO = 1280, 720
ZOOMS = [1.35, 1.25, 1.15, 1.05, 0.95, 0.85, 0.78, 0.72, 0.66]

BASE = '''
html.pm,html.pm body{background:var(--slide);margin:0}
html.pm .deck{max-width:none;padding:0;gap:0;display:block}
html.pm .deck>section{border-radius:0;border:0;padding:48px 64px 56px;box-sizing:border-box;align-content:center;min-height:0}
html.pm .deck>section.section{align-content:space-between}
html.pm .big{white-space:nowrap}
html.pm .num{right:32px;bottom:22px}
html.pm body{-webkit-print-color-adjust:exact;print-color-adjust:exact}
'''


def chrome():
    for c in [os.environ.get('CHROME'),
              '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
              shutil.which('google-chrome'), shutil.which('chromium'), shutil.which('chromium-browser')]:
        if c and os.path.exists(c):
            return c
    sys.exit('No encontré Chrome. Define la variable CHROME con la ruta del ejecutable.')


def documento(fragmento, titulo):
    """Envuelve el fragmento en un HTML completo, como lo hace el artefacto al publicarse."""
    cuerpo = re.sub(r'^\s*<title>.*?</title>\s*', '', fragmento, count=1, flags=re.S)
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<title>{titulo}</title>\n</head>\n<body>\n{cuerpo}\n</body>\n</html>\n')


def pagina_impresion(fragmento, extra):
    cuerpo = re.sub(r'^\s*<title>.*?</title>\s*', '', fragmento, count=1, flags=re.S)
    impresion = open(IMPRESION).read()
    return ('<!doctype html><html class="pm" data-theme="light"><head><meta charset="utf-8"></head><body>'
            + cuerpo + '<style>' + BASE + impresion + extra + '</style></body></html>')


def medir(ch, fragmento, ancho, tmp):
    js = ('<script>document.fonts.ready.then(()=>{const h=[...document.querySelectorAll(".deck>section")]'
          '.map(e=>Math.ceil(e.getBoundingClientRect().height));const p=document.createElement("pre");'
          'p.id="H";p.textContent=JSON.stringify(h);document.body.appendChild(p);});</script>')
    ruta = os.path.join(tmp, f'medir-{ancho}.html')
    open(ruta, 'w').write(pagina_impresion(fragmento, f'html.pm .deck>section{{width:{ancho}px}}') + js)
    salida = subprocess.run([ch, '--headless=new', '--disable-gpu', f'--window-size={ancho},900',
                             '--virtual-time-budget=8000', '--dump-dom', 'file://' + ruta],
                            capture_output=True, text=True).stdout
    m = re.search(r'<pre id="H">([^<]*)', salida)
    if not m:
        sys.exit('No pude medir las láminas: revisa que la fuente tenga <main class="deck"> con <section>.')
    return json.loads(m.group(1))


def titulos(fragmento):
    out = []
    for s in re.findall(r'<section\b.*?</section>', fragmento, flags=re.S):
        t = re.search(r'<(h1|h2)[^>]*>(.*?)</\1>', s, flags=re.S)
        out.append(re.sub(r'<[^>]+>|\s+', ' ', t.group(2)).strip()[:60] if t else '(sin título)')
    return out


def main():
    a = argparse.ArgumentParser()
    a.add_argument('fuente')
    a.add_argument('--salida', required=True)
    a.add_argument('--nombre', required=True)
    a.add_argument('--fuente-pdf')
    a.add_argument('--zoom-min', type=float, default=0.72)
    a.add_argument('--solo-html', action='store_true')
    o = a.parse_args()

    fragmento = open(o.fuente).read()
    m = re.search(r'<title>(.*?)</title>', fragmento, flags=re.S)
    titulo = m.group(1).strip() if m else o.nombre
    os.makedirs(o.salida, exist_ok=True)
    html_out = os.path.join(o.salida, o.nombre + '.html')
    open(html_out, 'w').write(documento(fragmento, titulo))
    print('HTML:', html_out)
    if o.solo_html:
        return

    ch = chrome()
    fpdf = open(o.fuente_pdf).read() if o.fuente_pdf else fragmento
    zooms = [z for z in ZOOMS if z >= o.zoom_min - 1e-9]
    tmp = tempfile.mkdtemp(prefix='exportar-')
    medidas = {z: medir(ch, fpdf, round(ANCHO / z), tmp) for z in zooms}
    n = len(medidas[zooms[0]])
    nombres = titulos(fpdf)
    reglas = (f'@page{{size:{ANCHO}px {ALTO}px;margin:0}}\n'
              'html.pm .deck>section{break-after:page;overflow:hidden}\n'
              'html.pm .deck>section:last-of-type{break-after:auto}\n')
    no_caben = []
    for i in range(n):
        z = next((z for z in zooms if medidas[z][i] * z <= ALTO - 8), None)
        if z is None:
            z = zooms[-1]
            no_caben.append((i + 1, nombres[i] if i < len(nombres) else '', round(medidas[z][i] * z)))
        w, h = round(ANCHO / z), int(ALTO / z) - 2
        reglas += (f'html.pm .deck>section:nth-of-type({i + 1})'
                   f'{{zoom:{z};width:{w}px;height:{h}px;min-height:{h}px}}\n')
        print(f'  lámina {i + 1:>2}: zoom {z:<4}  {nombres[i] if i < len(nombres) else ""}')
    if no_caben:
        print('\nNo caben en una página ni con el zoom mínimo (altura resultante en px, máximo 712):')
        for num, nom, alto in no_caben:
            print(f'  lámina {num}: {nom} → {alto}px')
        print('Divide esas láminas en la fuente del PDF (--fuente-pdf) o recorta texto. No generé el PDF.')
        sys.exit(2)
    final = os.path.join(tmp, 'final.html')
    open(final, 'w').write(pagina_impresion(fpdf, reglas))
    pdf_out = os.path.join(o.salida, o.nombre + '.pdf')
    subprocess.run([ch, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                    '--virtual-time-budget=8000', f'--print-to-pdf={pdf_out}', 'file://' + final],
                   capture_output=True)
    if not os.path.exists(pdf_out):
        sys.exit('Chrome no generó el PDF.')
    paginas = '?'
    if shutil.which('pdfinfo'):
        info = subprocess.run(['pdfinfo', pdf_out], capture_output=True, text=True).stdout
        mm = re.search(r'Pages:\s+(\d+)', info)
        paginas = mm.group(1) if mm else '?'
    print(f'PDF: {pdf_out} ({paginas} páginas, {n} láminas)')
    if paginas != '?' and int(paginas) != n:
        print('AVISO: el número de páginas no coincide con el de láminas; alguna se partió.')
        sys.exit(3)


if __name__ == '__main__':
    main()
