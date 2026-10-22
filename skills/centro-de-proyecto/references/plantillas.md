# Plantillas del centro

Esqueletos de los archivos que la skill crea. Se basan en `nova-plataforma`, el primer centro.
Los encabezados `##` del README del centro (`## Manifiesto`, `## Documentación general`,
`## Gestor de tareas`) se copian **tal cual**: la skill y `desarrollo-modular-vertical` los
buscan por nombre. El resto se adapta al proyecto.

---

## `README.md` — la puerta del centro

Dueño de: qué es el proyecto, el manifiesto de repos, los destinos de documentación general, el
gestor de tareas y cómo se trabaja. Es el **único dueño de las reglas de cada repo**.

```md
# <Nombre del proyecto>

<Qué es el proyecto, para quién (empresa o cliente) y de dónde parte (desde cero, ya empezado,
en equipo), en dos o tres líneas.>

Este repo es el **centro** del proyecto: el espacio privado de Jesús para pensar, decidir,
planear y dirigir el trabajo en los repos de código. No se sube a los repos del cliente ni del
equipo.

## Manifiesto

Modo: separado

| Pieza | Ruta | Dentro de | Disponibilidad | Dueño | Rama base | Contiene | Reglas |
|---|---|---|---|---|---|---|---|
| <centro> | `.` | | local | propio | main | este centro | — |
| <repo-front> | `../<repo-front>` | | local | cliente | main | frontend (React + Vite) | PR en borrador hacia `develop` |
| <repo-back> | `../<repo-back>` | | local | cliente | main | backend y orquestación | no integrar a `main` sin confirmación |
| <submódulo> | `../<repo-back>/<submódulo>` | <repo-back> | local | cliente | main | microservicio de autenticación | — |
| <otro-sistema> | — | | sin acceso | cliente | — | CRM del cliente | — |

- **Disponibilidad:** `local` (clonado y accesible) · `sin acceso` (existe, no lo tenemos) ·
  `solo docs externas` (solo se conoce por documentación).
- **Dueño:** `propio` · `empresa` · `cliente` · `equipo`. En `cliente` y `equipo` aplica la
  revisión antes de commit o PR.
- **Excepciones a la revisión:** <repo> tiene `docs/` como parte legítima del proyecto. (Borrar
  la línea si no hay.)
- **Patrones bloqueados extra:** <repo>: `<patrón>`. (Borrar la línea si no hay.)

## Documentación general

| Dónde | Qué contiene | Quién la mantiene | Cómo se actualiza |
|---|---|---|---|
| <Docmost / repo / Notion> | <documentación técnica del código> | <equipo> | a mano, desde este centro |

## Gestor de tareas

<Plane / Jira / ninguno>, proyecto <nombre>. Convención: <una tarea por vertical con subtareas por
tarea del plan>. (Solo anotado: la skill no lo consulta.)

## Contenido

| Archivo | Qué contiene |
|---|---|
| [decisiones/](decisiones/) | Decisiones tomadas, una por archivo |
| [bitacora.md](bitacora.md) | Ideas y observaciones sueltas, con fecha |
| [pendientes.md](pendientes.md) | Lo que falta definir, el trabajo por hacer y quién se encarga |
| [fuentes/](fuentes/README.md) | Material entregado por el cliente o el equipo, sin editar |

## Cómo se trabaja

1. Una idea u observación se anota en `bitacora.md`. No hace falta pulirla.
2. Si se aprueba, se escribe como decisión en `decisiones/` y se actualiza el documento que
   corresponda.
3. Lo que deba llegar a la documentación general se anota en `pendientes.md`, sección «Por llevar
   a la documentación general».
```

### Variante modo integrado

Cambia la presentación, la línea de modo y las rutas; el resto del README es igual.

```md
Esta carpeta es el **centro** del proyecto: donde se piensa, decide, planea y dirige el trabajo
de este repo. Se comparte con quien vea el repo; lo personal va en `privado/`, que git ignora.

## Manifiesto

Modo: integrado — carpeta `centro/` en <repo>, decidido por <quién> el AAAA-MM-DD

| Pieza | Ruta | Dentro de | Disponibilidad | Dueño | Rama base | Contiene | Reglas |
|---|---|---|---|---|---|---|---|
| centro | `.` | <repo> | local | <propio/empresa> | main | este centro (carpeta) | commits `docs(centro):` |
| frontend | `../frontend` | <repo> | local | <propio/empresa> | main | frontend | — |
| backend | `../backend` | <repo> | local | <propio/empresa> | main | backend | — |
```

El dueño de todas las filas es el del repo. La rama base sale de git, no se asume `main`. En la
tabla «Contenido» se agregan:

```md
| `.gitignore` | Deja `privado/` fuera de git |
| `privado/` | Solo en esta máquina: lo personal y lo que nadie debe ver todavía |
```

### `.gitignore` del centro (solo integrado)

```
privado/
```

### `privado/bitacora.md` (solo integrado)

Misma plantilla que `bitacora.md`. Encabezado: `# Bitácora privada` y la línea «Solo en esta
máquina: git la ignora. Lo personal y lo que nadie debe ver todavía.»

---

## `fuentes/README.md` — índice de fuentes

Dueño de: qué material se recibió, de quién y cuándo. Los archivos de `fuentes/` **no se
editan**; una versión nueva se agrega con fecha en el nombre.

```md
# Fuentes

Material entregado por el cliente o el equipo, tal como llegó. No se edita: una versión nueva se
agrega con fecha (`AAAA-MM-DD-nombre.ext`). Las conclusiones van a `decisiones/` y citan la fuente.

| Archivo | Entregado por | Fecha | Resumen |
|---|---|---|---|
| [2026-10-21-requerimientos.pdf](2026-10-21-requerimientos.pdf) | <persona, empresa> | 2026-10-21 | <una línea> |
```

---

## `bitacora.md`

Dueño de: la historia del proyecto (lo que pasó) y las ideas, observaciones y riesgos sueltos.
La entrada más reciente arriba.

```md
# Bitácora

La historia del proyecto: lo que pasó, ideas, observaciones y riesgos. La entrada más reciente va
arriba. No hace falta pulirlas: si una idea se aprueba, pasa a `decisiones/`.

**Tipos:** hecho · idea · observación · pregunta · riesgo
**Estados (no aplica a hechos):** nueva · en discusión · aprobada · descartada

## Plantilla

    ## AAAA-MM-DD · Tipo · Tema
    Descripción.
    - Propuso: nombre
    - Estado: nueva

---
```

---

## `pendientes.md`

Dueño de: lo que falta definir, el trabajo por hacer, quién se encarga y qué falta llevar a la
documentación general.

```md
# Pendientes

## Decisiones por tomar

| Pendiente | Responsable sugerido | Estado |
|---|---|---|

## Trabajo por hacer

| Trabajo | Tarea en el gestor | Estado |
|---|---|---|

## Por llevar a la documentación general

| Qué | Origen | Destino | Estado |
|---|---|---|---|
| <decisión o vertical cerrada> | [0003](decisiones/0003-...) | <Docmost> | pendiente · llevado AAAA-MM-DD |
```

---

## `decisiones/README.md` y formato de decisión

Dueño de: el índice de decisiones. Cada decisión es su propio archivo `NNNN-titulo-corto.md`. Una
decisión no se borra: si cambia, se escribe otra que la reemplaza.

```md
# Decisiones

Un archivo por decisión, numerado: `NNNN-titulo-corto.md`. Una decisión no se borra: si cambia, se
escribe una nueva que la reemplaza y se marca la anterior como "Reemplazada por NNNN".

## Plantilla

    # NNNN · Título

    - **Estado:** propuesta | aprobada | reemplazada por NNNN
    - **Fecha:** AAAA-MM-DD
    - **Decide:** quién aprueba
    - **Fuente:** <archivo de fuentes/ que la origina, si aplica>

    ## Contexto
    Qué problema hay y por qué hay que decidir.

    ## Decisión
    Qué se decidió, en una o dos frases.

    ## Alternativas descartadas
    Qué otras opciones había y por qué no.

    ## Consecuencias
    Qué cambia, qué trabajo genera y qué riesgos quedan.

## Índice

| # | Decisión | Estado |
|---|---|---|
```

---

## `preguntas.md`

Dueño de: las preguntas que solo el cliente puede responder y sus respuestas.

```md
# Preguntas para <cliente>

Marcar `[x]` cuando se resuelva y anotar la respuesta y la fecha. Cada reunión toma las preguntas
de aquí.

## <Tema: negocio / cómo trabajan / urgencia / técnico…>
- [ ] <pregunta>
- [x] <pregunta> → <respuesta> (AAAA-MM-DD, <quién>)
```

---

## `reuniones/AAAA-MM-DD-con-quien.md`

Dueño de: una reunión, antes y después.

```md
# Reunión con <persona> — <día AAAA-MM-DD, hora> (<medio>)

**Objetivo:** <qué tiene que salir de esta reunión>.

## Agenda
1. <tema>

## Preguntas que llevo
- <de preguntas.md>

## Qué contar / qué no decir todavía
- <...>

## Notas
-

## Acuerdos
-

## Pendientes que salen
- [ ]
```

---

## `guias/<tema>.md`

Dueño de: una explicación para avanzar en el proyecto.

```md
# <Tema>

**Para qué la necesito en este proyecto:** <una línea>.

## Lo esencial
<lo mínimo para decidir o trabajar>

## Opciones (si es una herramienta)
| Opción | A favor | En contra | Costo |
|---|---|---|---|

## Recomendación
<una>

## Por verificar
- <dato> → <dónde confirmarlo>
```
