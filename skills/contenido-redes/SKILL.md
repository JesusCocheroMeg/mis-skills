---
name: contenido-redes
description: >-
  Úsala cuando Jesús quiera crear contenido para sus redes sociales sobre programación y desarrollo
  de software: buscar ideas de videos en lo que ha hecho («revisa lo que hice esta semana», «saca
  ideas de mi bitácora»), escribir o mejorar un guion, un gancho, un título, una descripción o un
  carrusel, planear el calendario, adaptar un video a otra red (TikTok, Reels, Shorts, YouTube,
  LinkedIn, X), revisar si un caso se puede contar sin exponer clientes o anotar métricas. También
  ante menciones de mi-contenido, canal, video, reel, short, guion, gancho, hook o pilares.
---

# Contenido para redes

Videos y publicaciones sobre programación y desarrollo hechos **a partir de casos reales que Jesús
resolvió**. Lo que lo diferencia de mil canales de programación es que lo vivió: el problema, la
decisión y el resultado son suyos. Un guion sin caso real detrás no sirve, aunque suene bien.

**Objetivo actual:** aportar y hacer crecer las redes. **No se promocionan servicios** (nada de
«contrátame», «escríbeme para tu proyecto» ni enlaces a la web en el cierre) salvo que Jesús diga lo
contrario. Si en el centro hay una decisión que lo cambie, manda la decisión.

## Dónde vive

El centro del contenido es `mi-contenido/centro/` (si no existe, ofrece crearlo con la skill
`centro-de-proyecto`). Archivos que esta skill lee y actualiza:

| Archivo | Uso |
|---|---|
| `fuentes.md` | rutas de los espacios de Jesús que se pueden **leer** (nunca escribir) |
| `marca.md` | tono, pilares, temas que sí y que no, frases propias |
| `ideas/` | banco de ideas con estado: idea · guion · grabado · editado · publicado |
| `guiones/` | un archivo por video: `AAAA-MM-DD-<slug>.md` |
| `calendario.md` | qué sale, dónde y cuándo |
| `metricas.md` | resultados por video y lo que se aprendió |
| `bitacora.md` | lo que va pasando, con fecha |

Si falta `marca.md`, propón uno corto antes del primer guion y pide que lo apruebe.

## 1. Buscar ideas en los espacios de Jesús

1. Lee `fuentes.md`. Si no existe o falta una ruta, pregúntala y guárdala.
2. Busca en el periodo pedido (por defecto, la última semana): bitácoras, `mi-daily`, decisiones,
   commits (`git log --since`), pendientes y riesgos resueltos.
3. Lo que da buen video: un bug que costó encontrar, una decisión con un antes y un después, un
   error que Jesús cometió, una herramienta que ahorró tiempo, una cifra concreta (minutos, pesos,
   usuarios), algo que contradice lo que todos creen, o cómo explicó algo técnico a alguien no técnico.
4. Entrega cada idea así y guárdala en `ideas/`:

```
### <título de trabajo>
- Fuente: <ruta del archivo> (<fecha>)
- Caso: <qué pasó, en 1–2 líneas>
- Lección: <lo que se lleva quien lo ve>
- Gancho posible: <primera frase>
- Pilar · formato: <pilar> · <corto vertical | carrusel | video largo | hilo>
- Privacidad: ok | anonimizar <qué> | no usable (<por qué>)
- Estado: idea
```

Ordena las ideas de mejor a peor según la fuerza del gancho y lo concreto del caso, y di cuál
grabarías primero.

## 2. Privacidad antes que todo

Las fuentes tienen trabajo de empresas y clientes. Antes de que un caso pase a guion:

- **Se quitan:** nombres de empresas, clientes, compañeros y productos que no sean públicos; código
  propietario; datos, capturas, URLs internas, IPs, credenciales y cifras de negocio ajenas.
- **Se cuenta en general:** «en un CRM para un contact center» y no «en Conex de MEG.IA».
- **Lo público de Jesús sí se puede usar:** lo que ya está en https://jesuscochero.dev.
- Si el caso solo se entiende con un detalle privado, marca la idea como «no usable» o pregunta.
- En pantalla: código reescrito como ejemplo propio, nunca copiado del repo de un cliente.

## 3. Escribir el guion

Lee `references/ganchos-y-guiones.md` antes de escribir el primero de la conversación. Estructura
de un video corto (30–60 s, unas 80–150 palabras):

| Parte | Tiempo | Qué hace |
|---|---|---|
| Gancho | 0–3 s | una frase que abre una pregunta o una tensión; nada de saludos |
| Contexto | 3–10 s | el problema real, con un detalle concreto |
| Giro | — | lo que no funcionó o lo que nadie espera |
| Solución | — | qué hizo Jesús y por qué, en pasos simples |
| Cierre | últimos 3–5 s | la lección en una frase, o un remate que conecte con el gancho |

Formato del archivo de guion:

```
# <título>
Fuente: <ruta> (<fecha>) · Pilar: <pilar> · Red: <red> · Duración: <s>

## Gancho (3 opciones)
1. …
2. …
3. …

## Guion
| Se dice | En pantalla |
|---|---|
| … | texto grande / código / cara / captura propia |

## Texto de la publicación
<2–4 líneas + 3–5 hashtags específicos>

## Títulos (para YouTube o portada)
1. … 2. … 3. …
```

Reglas de escritura: frases cortas para decir en voz alta, en el español de Jesús (Colombia,
cercano, sin jerga innecesaria); un término técnico se explica la primera vez con una comparación;
una sola idea por video; cifras concretas cuando las hay. Lee el guion como si fuera audio: si una
frase no se entiende al oído, se reescribe.

## 4. Revisar antes de entregar

- [ ] El gancho funciona sin contexto previo y no promete algo que el video no da.
- [ ] Hay un caso real con fuente; nada inventado.
- [ ] Pasa la revisión de privacidad de la sección 2.
- [ ] Una sola idea; nada sobra para la duración elegida.
- [ ] El cierre no vende servicios (salvo decisión en contra).
- [ ] Se actualizó el estado en `ideas/` y, si aplica, `calendario.md`.

## 5. Adaptar y medir

- **Adaptar:** el mismo caso sirve para varias redes; cambia gancho, duración y texto, no el caso
  (ver tabla de redes en la referencia).
- **Medir:** cuando Jesús pase resultados, anótalos en `metricas.md` (vistas, retención si la hay,
  comentarios, seguidores) con una línea de aprendizaje: qué gancho, tema o formato funcionó. Al
  proponer ideas nuevas, apóyate en esos aprendizajes y dilo.
