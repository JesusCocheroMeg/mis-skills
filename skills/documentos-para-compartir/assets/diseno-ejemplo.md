# Diseño · Proyecto Faro (ejemplo)

Estilo: pitch deck limpio (referencia de Pinterest «Funding Pitch deck»). Láminas blancas con un
degradé azul muy suave; portada, separadores y cierre en azul pleno; un solo color de acento y
números grandes. Letra Manrope. Sobrio y profesional, nada de neumorfismo ni efectos.

Lo que no gustó: el estilo neumórfico y los diseños oscuros con aspecto técnico.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap">
```

```css
:root{
  --page:#eef1f6; --slide:#ffffff; --slide-2:#eef3ff; --ink:#0f1a33; --muted:#5d6a85; --line:#dde3ee;
  --accent:#1f5bf0; --accent-ink:#ffffff; --accent-soft:#e6edff; --accent-2:#3d74ff;
  --font:"Manrope", "Helvetica Neue", system-ui, sans-serif;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --page:#0a0f1c; --slide:#121a2c; --slide-2:#16213b; --ink:#eaf0ff; --muted:#9aa7c4; --line:#25304a;
  --accent:#3a6dff; --accent-soft:#1b2a52; --accent-2:#6a92ff;
  --bad:#ff8b80; --bad-soft:#3a1d1c; --warn:#ffb866; --warn-soft:#3a2a17; --ok:#6fd49a; --ok-soft:#173023;
  --info:#a9bdf0; --info-soft:#1b2440; --tbd:#f0b061; --tbd-soft:#3a2c1a; color-scheme:dark}}
:root[data-theme="dark"]{
  --page:#0a0f1c; --slide:#121a2c; --slide-2:#16213b; --ink:#eaf0ff; --muted:#9aa7c4; --line:#25304a;
  --accent:#3a6dff; --accent-soft:#1b2a52; --accent-2:#6a92ff;
  --bad:#ff8b80; --bad-soft:#3a1d1c; --warn:#ffb866; --warn-soft:#3a2a17; --ok:#6fd49a; --ok-soft:#173023;
  --info:#a9bdf0; --info-soft:#1b2440; --tbd:#f0b061; --tbd-soft:#3a2c1a; color-scheme:dark}
```
