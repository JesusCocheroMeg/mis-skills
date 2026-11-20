# Diagramas

Un diagrama entra cuando muestra algo que en texto costaría un párrafo: un recorrido, cómo se conectan las piezas,
por dónde viaja un dato. No decores con diagramas.

## Los cuatro tipos

| Tipo | Cuándo | Forma |
|---|---|---|
| **Flujo del usuario** | Cómo vive el negocio quien lo usa (sección 2 del mapa) | Cajas de izquierda a derecha con el rol arriba; flechas con la acción |
| **Arquitectura de piezas** | Qué piezas hay y cómo se hablan (sección 3) | Cajas por pieza (app, API, worker, base, servicios externos); flechas con el protocolo o el dato |
| **Flujo de datos** | Por dónde pasa un dato sensible o importante | Igual que arquitectura, resaltando el camino con `.node.b` |
| **Secuencia de un proceso** | Cómo trabaja una pieza paso a paso (profundizar) | Cajas con reintento o error en `.node.w` y flecha punteada `.arr.d` |

## Reglas

- SVG en línea dentro de `<div class="scroll" style="border:0">`, con `class="diagram"`, `viewBox`, `role="img"` y un
  `aria-label` que cuente el diagrama en una frase. El verificador lo exige.
- Usa solo las clases de la plantilla (`.node`, `.node.b`, `.node.ok`, `.node.w`, `.lbl`, `.sm`, `.arr`, `.arr.d`)
  para que funcione en claro y oscuro. Nada de colores escritos a mano.
- Máximo ~8 cajas. Si hacen falta más, es otro diagrama o es tema para profundizar.
- Etiquetas cortas: nombre de la pieza en `.lbl` y una línea de qué hace en `.sm`.
- Debajo del diagrama, el paso a paso en texto (`.flow` con `.step`), para quien no lo lea bien en el celular.

## Esqueleto

```html
<div class="scroll" style="border:0">
<svg class="diagram" viewBox="0 0 940 300" role="img" aria-label="La app deja trabajos en la cola y el worker los procesa">
  <defs>
    <marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="head"/></marker>
    <marker id="ahw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="headw"/></marker>
  </defs>
  <rect class="node" x="10" y="100" width="190" height="80" rx="14"/>
  <text class="lbl" x="105" y="135" text-anchor="middle">App</text>
  <text class="sm" x="105" y="157" text-anchor="middle">atiende a la persona</text>
  <rect class="node b" x="300" y="100" width="200" height="80" rx="14"/>
  <text class="lbl" x="400" y="135" text-anchor="middle">Cola</text>
  <text class="sm" x="400" y="157" text-anchor="middle">en PostgreSQL</text>
  <path class="arr" d="M200,140 L298,140"/>
</svg>
</div>
```

Si hay más de un SVG en la página, los `id` de los `marker` deben ser únicos (`ah2`, `ahw2`…) o definirse una sola
vez en el primer SVG.
