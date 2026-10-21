# Plantillas obligatorias

Estos son los esqueletos de los **seis** archivos del módulo. Los encabezados `##` se copian
tal cual: **no se inventan secciones, no se renombran, no se reordenan**. Si un módulo
necesita algo que no cabe en ninguna sección, es señal de una decisión sin registrar, no de
una sección nueva.

Todo dato repetido en dos archivos es un defecto: se retira la copia y se deja el enlace.

---

## `README.md` — la puerta del módulo

Es el único archivo que se lee para saber cómo va el módulo. Objetivo: **una pantalla**.
La tabla de verticales es su corazón y es la **fuente única de su estado**.

```md
# <Nombre del módulo>

<Qué es y de qué es dueño, en dos o tres líneas. Qué consume de otros módulos y en qué
dirección.>

Código: `<ruta/al/feature/>`

## Estado (<AAAA-MM-DD>)

| | |
|---|---|
| **Visión** | [`vision.md`](vision.md) — aprobada <fecha> |
| **Versión activa** | [`current-version.md`](current-version.md) — <vX.Y>, <n> verticales |
| **Decisiones** | [`decisions.md`](decisions.md) — <n> registradas, <n> aprobadas |
| **Roadmap** | [`roadmap.md`](roadmap.md) — <fases o ideas vigentes> |
| **Código** | <qué tan implementado está y si es mock> |

## Verticales

**Fuente única del estado.** Si otro documento contradice esta tabla, esta tabla gana. El
diseño, los criterios de aceptación y la evidencia de cierre están en el archivo de cada una.

| ID | Vertical | Estado | Diseño aprobado | Plan | Cerrada | Bloqueada por |
|----|----------|--------|-----------------|------|---------|---------------|
| [V1](verticals/V1-<slug>.md) | <título> | ✅ Implementada | <fecha> | [plan](<ruta>) | <fecha> (`<commit>`) | — |
| [V2](verticals/V2-<slug>.md) | <título> | 📋 Definida | — | — | — | <módulo · vertical> |

Estados: 💡 Idea · 📋 Definida · 🎨 En diseño · 👍 Diseño aprobado · 🔨 En implementación ·
✅ Implementada · ⛔ Bloqueada · ❌ Descartada.

<Si una vertical pasó la verificación técnica pero el usuario todavía no la validó en el
navegador, marcala con ⚠️ en su fila y decilo acá en una línea. No la presentes como validada.>

## Reglas vigentes

<Las tres o cuatro reglas que gobiernan el módulo y que un agente rompería sin saberlo:
naming engañoso, dirección de las dependencias, qué no se toca.>

## ➡️ Siguiente paso

<Una acción concreta, con el archivo que hay que abrir para ejecutarla.>
```

---

## `vision.md` — para qué existe el módulo

Casi nunca cambia. No registra avance ni estados.

```md
# Visión — <Módulo>

**Estado:** <Vigente | Reemplazada por …> · **Aprobada:** <fecha>

## Propósito

<Qué problema del negocio resuelve. Sin hablar de pantallas.>

## Responsabilidades

<De qué datos y qué reglas es dueño este módulo.>

## Límites

<Qué NO le corresponde y de qué otro módulo es. Explícito: es lo que evita que crezca de más.>

## Relación con otros módulos

<Qué consume, qué expone y en qué dirección. Si hay un contrato de frontera, enlazalo.>

## Capacidades futuras

<Lo que el módulo podrá hacer algún día. No es compromiso: el compromiso vive en
`current-version.md`.>
```

---

## `roadmap.md` — lo que podría entrar y la deuda que ya existe

Nada de acá está comprometido. Lo comprometido está en `current-version.md`.

```md
# Roadmap — <Módulo>

## Capacidades por estado

| ID | Capacidad | Estado | Prioridad | Versión estimada | Depende de |
|----|-----------|--------|-----------|------------------|------------|
| F1 | <título> | 💡 Idea | Alta | v0.2 | — |

Estados: 💡 Idea · 📋 Definida · 👍 Aprobada · 🔨 En una versión · ✅ Entregada · ❌ Descartada.

## Bandeja de entrada

<Ideas crudas, sin analizar, con la fecha en que aparecieron. Entran acá para no perderse.>

## Deuda heredada (auditoría del <AAAA-MM-DD>)

Foto **fechada** del código anterior a esta metodología. No describe el estado actual: sirve
para convertir el prototipo en verticales. Cuando una fila se resuelve, se tacha con el commit
que la cerró.

| Parte | Qué pasa | Veredicto | Se resuelve en |
|-------|----------|-----------|----------------|
| `<archivo o componente>` | <datos simulados, función incompleta, patrón divergente> | Conservar / Ajustar / Reubicar / Reconstruir / Eliminar | <vertical o "sin asignar"> |
```

---

## `current-version.md` — el único compromiso

```md
# <vX.Y> — <Módulo>

**Estado:** <En curso | Cerrada el …> · **Comprometida:** <fecha>

## Objetivo

<Una frase: qué queda funcionando al terminar la versión.>

## Entra

| ID | Vertical | Por qué entra |
|----|----------|---------------|
| V1 | <título> | <capacidad del roadmap que cubre> |

Su estado está en la tabla del [`README.md`](README.md), no acá.

## No entra

| Qué | Por qué queda fuera | Cuándo se retoma |
|-----|---------------------|------------------|
| <capacidad> | <motivo o bloqueo> | <versión o "sin fecha"> |

## Criterio de cierre

<Qué tiene que ser verdad para declarar la versión terminada. Verificable, no aspiracional.>
```

---

## `decisions.md` — por qué el código es así

Empieza con una **tabla-índice** para poder consultarlo sin leerlo entero.

```md
# Decisiones — <Módulo>

| ID | Decisión (una línea) | Estado | Fecha | Afecta |
|----|----------------------|--------|-------|--------|
| DEC-01 | <qué se decidió, en una línea> | ✅ Aprobada | <fecha> | <vX.Y · V1> |

Estados: 📝 Propuesta · ⏳ Pendiente de aprobación · ✅ Aprobada · ♻️ Reemplazada por DEC-nn ·
❌ Descartada.

---

## DEC-01 — <título>

**Estado:** ✅ Aprobada · **Fecha:** <fecha> · **Afecta:** <versión o vertical>

**Decisión.** <Qué se hace. En imperativo y concreto.>

**Consecuencia.** <Qué obliga o impide de acá en adelante.>
```

**Campos obligatorios: cinco** — ID, estado, fecha, decisión y consecuencia.

Agregá **Contexto**, **Alternativas** y **Motivo** solo cuando hubo una alternativa real que
se descartó y alguien podría querer revivirla. Una decisión obvia con tres párrafos de
justificación inventada es ruido que se paga en cada lectura.

Nunca marques ✅ Aprobada sin evidencia de aprobación del usuario.

---

## `verticals/<ID>-<slug>.md` — el ciclo completo de una vertical

Un solo archivo cuenta toda la historia de la vertical. **No declara su propio estado**: eso
está en la tabla del `README.md`. Las secciones se agregan a medida que la vertical avanza.

```md
# <ID> — <título>

Estado: ver la tabla de [`../README.md`](../README.md).

## Qué resuelve

<El problema concreto, con evidencia: archivo:línea, capacidad del roadmap o decisión que
la originó.>

## Alcance

**Entra:** <lista corta.>
**No entra:** <lo que se aplaza, con el motivo.>

## Diseño

**Aprobado:** <fecha> · <enlace a la especificación si existe>

<Entidades, endpoints, permisos, validaciones. Componentes y patrones reutilizados, con la
ruta. Riesgos y regresiones posibles. Decisiones que abrió, por ID.>

## Criterios de aceptación

- [ ] <Verificable y comprobable por alguien más. Incluí el recorrido que falla, no solo el
      que funciona.>

## Plan

<Enlace al plan aprobado. Si no hay plan, esta sección dice "sin plan aprobado".>

## Cierre

**Fecha:** <AAAA-MM-DD> · **Commits:** `<sha>`, `<sha>`

**Qué se implementó.** <Archivos tocados y qué cambió en cada uno.>

**Evidencia de verificación.**

| Comprobación | Resultado |
|---|---|
| lint | <salida resumida> |
| typecheck | <salida resumida> |
| build | <salida resumida> |
| pruebas | <cuántas, cuáles> |
| greps de criterio | <qué se buscó y qué devolvió> |

**Validación humana:** <Pendiente | Validada por el usuario el …>. La verificación técnica no
la reemplaza.

**Pendientes que deja.** <Lo que quedó abierto, y adónde se movió: roadmap, otra vertical o
una decisión nueva. Si no dejó nada, decilo.>
```

Esta sección «Cierre» es la que reemplaza al viejo `changelog.md`. La marca de cierre (fecha y
commit) va **también** en la fila del README, y nada más de esto se copia allá.
