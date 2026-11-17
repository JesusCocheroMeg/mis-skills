#!/usr/bin/env python3
"""Crea la fuente de un documento nuevo con los componentes y el diseño del proyecto.

Uso:
  python3 nuevo_documento.py --salida RUTA/_fuente/documento.html --titulo "Informe de seguridad" \
      [--diseno RUTA/diseno.md] [--marca "Proyecto Faro"]

Del diseno.md toma el primer bloque ```html (enlaces a fuentes de Google Fonts) y todos los bloques
```css (variables de color, letra y reglas propias). Si no hay diseno.md, usa los valores por defecto
de assets/componentes.css.

Deja una portada y una lámina de ejemplo para reemplazar.
"""
import argparse, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
COMPONENTES = os.path.join(AQUI, '..', 'assets', 'componentes.css')


def main():
    a = argparse.ArgumentParser()
    a.add_argument('--salida', required=True)
    a.add_argument('--titulo', required=True)
    a.add_argument('--diseno')
    a.add_argument('--marca', default='')
    a.add_argument('--tipo', choices=['informe', 'propuesta', 'corto'], default='informe',
                   help='informe: portada + «En un minuto»; propuesta y corto: solo portada')
    o = a.parse_args()
    if os.path.exists(o.salida):
        sys.exit(f'Ya existe {o.salida}: edítalo en vez de crearlo de nuevo.')

    links, css_diseno = '', ''
    if o.diseno:
        d = open(o.diseno).read()
        h = re.search(r'```html\n(.*?)```', d, flags=re.S)
        links = h.group(1).strip() if h else ''
        css_diseno = '\n'.join(c.strip() for c in re.findall(r'```css\n(.*?)```', d, flags=re.S))
    componentes = open(COMPONENTES).read()
    marca = f'<div class="brand"><i></i>{o.marca}</div>\n    ' if o.marca else ''
    minuto = '''  <!-- En un minuto -->
  <section class="slide">
    <div class="head">
      <p class="eyebrow">En un minuto</p>
      <h2>Lo esencial <span class="hl">de este documento</span></h2>
    </div>
    <div class="grid g3">
      <div class="card"><span class="label">Qué pasa</span><h3>…</h3><p>…</p></div>
      <div class="card"><span class="label">Qué significa</span><h3>…</h3><p>…</p></div>
      <div class="card accent"><span class="label">Qué sigue</span><h3>…</h3><p>…</p></div>
    </div>
    <span class="num">02</span>
  </section>

''' if o.tipo == 'informe' else ''
    html = f'''<title>{o.titulo}</title>

<meta name="claude:viewport-fit-sides" content="cover">
{links}
<style>
{componentes}
/* Diseño del proyecto */
{css_diseno}
</style>
<main class="deck" lang="es">

  <!-- Portada -->
  <section class="slide section cover">
    {marca}<div class="head">
      <h1>{o.titulo}</h1>
      <p class="lead">Una frase que diga de qué trata y para qué sirve.</p>
    </div>
    <p class="eyebrow">Fecha · Preparado por …</p>
    <span class="num">01</span>
  </section>

{minuto}
</main>
'''
    os.makedirs(os.path.dirname(os.path.abspath(o.salida)), exist_ok=True)
    open(o.salida, 'w').write(html)
    print('Fuente creada:', o.salida)


if __name__ == '__main__':
    main()
