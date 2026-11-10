---
name: documentos-para-compartir
description: >-
  Crea documentos para compartir con clientes, jefes o personas no técnicas —propuestas, cotizaciones
  presentadas, informes (de seguridad, de avance, de diagnóstico), resúmenes de reunión, explicaciones,
  planes— con buen diseño y fáciles de entender, como láminas exportadas a web (artefacto), HTML y PDF.
  El diseño lo define cada proyecto (diseno.md) o el pedido. Úsala siempre que Jesús pida armar,
  «montar», «hacer bonito», exportar o ajustar un documento o presentación para enviarle a alguien
  (aunque no diga «documento»: «hazme el informe para el cliente», «pásalo a PDF», «la propuesta para el
  cliente», «un resumen que entienda gerencia»), y también cuando pida cambios a uno ya hecho con
  esta skill («cambia la cifra y exporta de nuevo»).
---

# Documentos para compartir

Documentos que otra persona va a leer sin que Jesús esté al lado para explicarlos: un cliente, un
gerente o alguien no técnico. Tienen que entenderse solos, verse profesionales y decir la verdad con
hechos. Se arman como **láminas** (secciones `<section class="slide">`) y salen de una sola fuente:

| Salida | Para qué | Cómo |
|---|---|---|
| **Web** (artefacto privado) | revisarlo en el navegador o compartir un enlace | Artifact tool con la fuente |
| **HTML** | un archivo que se abre en cualquier lado | `scripts/exportar.py` |
| **PDF** | enviar por WhatsApp o correo, imprimir | `scripts/exportar.py` (láminas de 1280×720) |

**Formatos:** por defecto los tres. Decide según el pedido (si solo va por WhatsApp, el PDF es lo
importante; si es para revisar juntos, la web) y dilo en una línea. Si Jesús pide uno concreto o
algo más (Word, PowerPoint, Markdown, un doc editable), hazlo con la skill o herramienta que
corresponda a ese formato, partiendo del mismo contenido.

## 1. Antes de escribir

1. **Para quién y para qué.** Quién lo lee, qué tiene que entender y qué decisión o acción se espera.
   Si no está claro en la conversación, pregúntalo en una línea.
2. **Fuentes.** Lee lo que exista del tema: notas de reunión, bitácora, cotizaciones, documentos
   previos al mismo cliente. Si el proyecto tiene un centro (skill `centro-de-proyecto`), los
   documentos van en `<centro>/presentaciones/<slug>/`; si no, pregunta dónde.
3. **Términos ya usados.** Si ya se le envió algo a esa persona, usa las mismas palabras y cifras
   (por ejemplo, «diagnóstico de arranque» y no «Etapa 0» si así se le dijo). Dos documentos que se
   contradicen restan confianza.
4. **Diseño.** Ver sección 2.
5. **Estructura.** En documentos de más de 3 láminas, propón la lista (título y una línea cada una)
   antes de construir, salvo que el pedido ya la traiga o sea un ajuste: es más barato corregir un
   índice que 15 láminas. En uno corto (resumen, nota), constrúyelo directo.
6. **Huecos.** Si a las fuentes les falta algo que el documento necesita (fechas, responsables, una
   cifra), pregúntalo antes si Jesús está en la conversación. Si no se puede preguntar, márcalo con
   `<span class="tbd">por confirmar</span>` y dilo al entregar. Nunca lo inventes.

## 2. Diseño

El diseño es del proyecto, no de la skill. Orden de prioridad:

1. Lo que diga el pedido para este documento (un color, una referencia, «más sobrio»).
2. `diseno.md` del proyecto, junto a los documentos (en un centro: `<centro>/presentaciones/diseno.md`).
3. Si no hay ninguno: pide una referencia (captura, enlace de Pinterest, una marca) o propone 2–3
   direcciones descritas en una línea cada una, y crea el `diseno.md` con la elegida para que el
   siguiente documento del proyecto salga igual. Las imágenes de Pinterest suelen no cargar con
   WebFetch: si no puedes verla, pide una captura.

Formato de `diseno.md`: ver `assets/diseno-ejemplo.md` (pitch deck azul, Manrope). Lleva
una descripción del estilo, un bloque ```html con la fuente de Google Fonts y un bloque ```css con las
variables (`--accent`, `--ink`, `--slide`…, modo claro y oscuro) y reglas propias. Un cambio de
diseño pedido para un solo documento va en el `<style>` de ese documento, no en `diseno.md`, salvo
que Jesús diga que es para todo el proyecto.

Antes de publicar la primera vez en una conversación, carga la skill `artifact-design` (contrato de
la página: título, tokens de color, modo oscuro, ancho de celular).

## 3. Construir

```
<slug>/
├── _fuente/documento.html     ← fuente única (web y HTML)
├── _fuente/impresion.html     ← solo si hubo que dividir láminas para el PDF
├── _fuente/publicacion.md     ← URL del artefacto, para actualizar siempre el mismo enlace
├── <Nombre-Del-Documento>.html
└── <Nombre-Del-Documento>.pdf
```

1. Crea la fuente con los componentes y el diseño (`--tipo informe` agrega la lámina «En un
   minuto»; `--tipo corto` deja solo la portada):
   `python3 scripts/nuevo_documento.py --salida <slug>/_fuente/documento.html --titulo "…" --diseno <diseno.md> --marca "…" --tipo corto`
   Si el documento ya existe con otra organización (por ejemplo, hecho antes de esta skill), sigue la
   que tiene en vez de reorganizarlo.
2. Reemplaza las láminas de ejemplo. Los componentes disponibles (tarjetas, filas, comparaciones,
   línea de tiempo, estados, pasos, notas, números grandes) están en `references/componentes.md`:
   úsalos antes de inventar CSS nuevo, porque ya funcionan en celular y en el PDF.
3. Redacta con `references/redaccion.md`. Es lo que más pesa: un documento lindo que no se entiende
   no sirve.
4. Numera las láminas (`<span class="num">NN</span>`) y revisa que las referencias internas
   («ver página 10») apunten bien. Si quitas o agregas láminas, renumera.

## 4. Exportar y verificar

```bash
python3 scripts/exportar.py <slug>/_fuente/documento.html --salida <slug> --nombre <Nombre-Del-Documento>
```

- Elige por lámina el zoom más grande con el que cabe en 1280×720, para que la letra no quede chica.
- Si una lámina no cabe (sale con código 2 y la lista), no la achiques más: copia la fuente a
  `_fuente/impresion.html`, divide esas láminas en dos (repartiendo tarjetas o filas, con un título
  que siga el hilo) y exporta con `--fuente-pdf <slug>/_fuente/impresion.html`. La web queda con la
  lámina entera, porque se lee con scroll. Mantén las dos fuentes iguales en todo lo demás.
- **Verifica**: `pdftotext <pdf> - | grep -n "<texto cambiado>"` para confirmar que el cambio está, y
  mira como imagen (`pdftoppm -f N -l N -r 60 -png <pdf> <scratchpad>/pagina`) las láminas que tocaste
  o que tienen tablas. Las imágenes van al scratchpad, nunca junto al documento.
- Opciones de los scripts: `python3 scripts/<script>.py --help`.
- **Publica** la web con el Artifact tool desde `_fuente/documento.html`; guarda la URL en
  `_fuente/publicacion.md` y, en cambios posteriores, publica con esa `url` para no crear enlaces nuevos.

## 5. Cambios posteriores

Cada cambio va a la fuente (y a `impresion.html` si existe), y luego se exportan **todos** los
formatos que ya existían, no solo el que se estaba mirando. Si cambia una cifra, recalcula todo lo
que depende de ella (totales, rangos, porcentajes, tiempos) y di qué números cambiaron y cuáles no.
Si cambia un término, búscalo en todo el documento (`grep`) y en otros documentos enviados al mismo
cliente, y ofrece cambiarlo también allá.

## 6. Entregar

Responde corto:
- qué cambió o qué contiene (las láminas en una línea cada una si es nuevo);
- cuántas páginas tiene el PDF y qué verificaste;
- dónde están los archivos y, si se publicó, el enlace web, recordando que el artefacto es **privado**: para que
  otra persona lo abra hay que compartirlo desde el menú «Compartir»; si no, que envíe el PDF;
- lo que quedó «por confirmar», si hay;
- cuánto toma leerlo (≈ 20–30 s por lámina), útil para el mensaje con el que lo va a enviar.

Si Jesús pide el mensaje para enviarlo, da pautas (qué decir, qué evitar) y 2–3 opciones redactadas.
