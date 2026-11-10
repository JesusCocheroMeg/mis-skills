# Componentes

Todos están en `assets/componentes.css` y usan las variables del diseño (`--accent`, `--ink`,
`--muted`, `--line`, `--slide`…). Funcionan en celular (se apilan) y en el PDF (`impresion.css` fuerza
la grilla de escritorio).

## Lámina

```html
<section class="slide" id="ancla-opcional">
  <div class="head">
    <p class="eyebrow">Sección</p>
    <h2>Título que dice la conclusión <span class="hl">con la parte clave resaltada</span></h2>
    <p>Bajada de una o dos líneas.</p>
  </div>
  … contenido …
  <span class="num">03</span>
</section>
```

- Lámina de color pleno (portada, cierre, separadores): `class="slide section"`; portada: `section cover`.
  Dentro: `<div class="brand"><i></i>Marca</div>`, `<p class="lead">…</p>`.
- `.hl` resalta texto con el acento. `.tbd` marca un dato por confirmar.

## Tarjetas

```html
<div class="grid g3">   <!-- g2 · g3 · g4 -->
  <div class="card"><span class="label">Etiqueta</span><h3>Título</h3><p>Texto</p></div>
  <div class="card accent"><span class="dot">✓</span><h3>Destacada</h3><p>…</p></div>
  <div class="card soft">…</div>
  <div class="card alert"><span class="label">Alerta</span>…</div>
</div>
```

- `.dot` = cuadrito con número o símbolo. `.big` = número grande (`<div class="big">600<small>mil</small></div>`).
- `.card .pill` dentro de una tarjeta queda alineada a la izquierda.

## Filas (definiciones, glosario, requisitos)

```html
<div class="rows">
  <div><b>Término</b><span>Explicación</span></div>
  <div class="key"><b>Destacado</b><span>…</span></div>
</div>
```

## Comparación (antes / después, ellos / nosotros)

```html
<div class="cmp">
  <div class="h"><span></span><span>Sin ajustar</span><span class="us">Con lo que ya tienen</span></div>
  <div><b>Fila</b><span class="them">$ 10 – 14 M</span><span class="us-cell">≈ $ 7 – 10,5 M</span></div>
</div>
```

## Estados (qué está afectado)

```html
<div class="status">
  <div class="h"><span>Qué</span><span>Estado</span><span>Detalle</span></div>
  <div><b>Sitio web</b><span><span class="pill p-bad">Comprometido</span></span><span class="t">…</span></div>
</div>
```

Pills: `p-bad` · `p-warn` · `p-ok` · `p-info`. Tabla de 4 columnas (evidencia): `class="status ev"`;
fila resaltada: `<div class="hot">`.

## Línea de tiempo (hasta 5 hitos)

```html
<div class="tl">
  <div><span class="pt">1</span><span class="when">11 oct</span><h3>…</h3><p>…</p></div>
</div>
```

## Pasos y acciones

```html
<ol class="steps-list">
  <li><div><h3>Pausar publicaciones</h3><p>…</p><span class="who">Responsable:</span></div></li>
</ol>
```

## Notas, listas y botones

- Nota: `<div class="note"><span class="dot">i</span><p><b>Ojo:</b> …</p></div>`
- Etiquetas: `<div class="chips"><span>…</span></div>`
- Índice con enlaces: `<ol class="agenda"><li><a href="#ancla"><b>Tema</b><span>detalle</span></a></li></ol>`
- Botón: `<a class="cta" href="…">…</a>` (`cta ghost` = con borde); enlace a perfil: `<a class="li-btn">`.
- Barras: `.bars > .bar-row` con `<div class="track"><div class="fill" style="width:60%">…</div></div>`.
- Opciones de precio: `.card.opt` (`.opt.accent` la recomendada) con `.price`, `ul` y `.flag`.
- Dos columnas texto/visual: `<div class="split">`.
- Código o señales técnicas (solo anexo): `.mono`, `.code`, `.code-inline`.
- Texto chico: `.small`.
