# Marcas de fuente

Jesús usa la presentación para opinar y decidir. Si una deducción suena igual de segura que algo comprobado, decide
mal. Por eso **toda afirmación que importe lleva una marca**.

| Marca | Cuándo | Cómo se escribe |
|---|---|---|
| **comprobado** | Lo viste: código, esquema, configuración, dependencia, documento del proyecto | `<span class="marca comprobado">comprobado</span> <span class="fuente">ruta/archivo.ts:42</span>` |
| **deducido** | Lo infieres de varias señales, pero nada lo dice directo | `<span class="marca deducido">deducido</span>` + en una frase de qué lo deduces |
| **por confirmar** | Solo alguien que conozca el aplicativo o el negocio puede decirlo | `<span class="marca confirmar">por confirmar</span>` + la pregunta concreta |

## Reglas

- **Comprobado siempre lleva fuente**: `archivo:línea`, ruta de documento o nombre de la dependencia con su versión.
  Sin fuente, no es comprobado.
- **El «porqué» de una decisión técnica** es comprobado solo si está escrito (una decisión, un ADR, un comentario, un
  commit). Si no, es deducido: «probablemente se escogió X porque…».
- **El negocio de un aplicativo ajeno** casi siempre es deducido. Está bien: dilo.
- **No marques lo obvio** (que un archivo existe). Marca lo que Jesús podría usar para decidir.
- **Lo por confirmar** se escribe como pregunta que se pueda hacer tal cual: «¿Quién radica la portabilidad ante el
  ABD y cuándo?», no «confirmar el proceso».
- En tablas, la marca va en su propia columna o al final de la celda.

## Conteo final

La última sección («Fuentes y marcas») dice cuántas afirmaciones hay de cada tipo y qué se leyó. Si más de la mitad
es deducido, dilo arriba, en la portada: «Este mapa es sobre todo deducido; conviene validarlo con alguien del
equipo».
