---
name: centro-de-proyecto
description: Úsala cuando el usuario quiera crear, adoptar o abrir el repo centro de un proyecto (su espacio privado junto a los repos de código), arrancar el día o pedir el estado de un proyecto con varios repos, guardar fuentes que entregó un cliente o equipo, delegar trabajo a agentes en otros repos del proyecto, o hacer commit o PR en un repo que es del cliente o del equipo. También ante menciones de centro, manifiesto, fuentes o documentación general.
argument-hint: "[crear | adoptar | abrir sesión | delegar | fuentes]"
---

# Centro de proyecto

Un **centro** es un repo git privado de Jesús que vive en la carpeta del proyecto, al lado de los
repos de código. Ahí se piensa, se decide, se planea y se dirige; el código se toca en los repos
que el manifiesto declara. Lo que hay en el centro **nunca** termina en un repo ajeno.

```
<proyecto>/
├── <centro>/          ← este repo (en Nova: nova-plataforma)
├── <repo-de-codigo>/
└── <otro-repo>/
```

Esa disposición es la convención. Un repo en otra ruta es una excepción válida y se anota en el
manifiesto.

Esta skill define **dónde** está todo. **Cómo** se desarrolla un módulo es de
`desarrollo-modular-vertical`; las dos se usan juntas.

## Cómo reconocer un centro

Un repo es un centro si su `README.md` tiene la sección `## Manifiesto`. Si no la tiene y el
usuario quiere trabajar así, es el flujo **Crear** (repo nuevo) o **Adoptar** (repo existente).

El contexto puede ser **completo o parcial**: todos los repos clonados, solo algunos, solo
documentación o nada de código. Nunca asumas acceso a algo que el manifiesto no marca `local`.

## Escenarios

| Eje | Valores | Qué cambia |
|---|---|---|
| Para quién | empresa · cliente | cliente: dueño `cliente` en sus repos (revisión obligatoria) |
| De dónde parte | desde cero · ya empezado · en equipo | ya empezado: `diagnostico.md`; en equipo: destino de documentación general |

Cotizaciones y parte comercial: **fuera de alcance** de esta versión. No las propongas.

## Estructura

**Mínimo obligatorio:** `README.md` (con `## Manifiesto`), `decisiones/`, `bitacora.md`,
`pendientes.md`. `fuentes/` si hay material entregado.

**Según escenario, se propone, no se impone:** `propuesta.md`, `hoja-de-ruta.md` + `fases/`,
`diagnostico.md` (ya empezado), `implementacion/`, `argumentos.md`, `docs/modules/` (si se usa
desarrollo vertical), `docs/superpowers/` (specs y planes).

Cada proyecto puede agregar, quitar o renombrar lo no obligatorio, y es válido.

**Plantillas:** `references/plantillas.md`. Leelo antes de crear cualquiera de estos archivos.
Los encabezados `## Manifiesto`, `## Documentación general` y `## Gestor de tareas` se copian
tal cual.

## Manifiesto

Tabla en el `README.md` del centro, una fila por pieza del proyecto:
Pieza · Ruta · Dentro de · Disponibilidad · Dueño · Rama base · Contiene · Reglas.

- **Ruta** relativa al centro (`../erp-frontend`).
- **Dentro de:** el repo padre si es submódulo. Cada submódulo es su propia fila: suele ser donde
  vive el código real.
- **Disponibilidad:** `local` · `sin acceso` · `solo docs externas`.
- **Dueño:** `propio` · `empresa` · `cliente` · `equipo`.
- El manifiesto es el **único dueño de las reglas de cada repo** (ramas, PR, despliegue). Si una
  regla vive en otro lado (memoria, otro doc), se mueve al manifiesto y el otro lado lo enlaza.

Debajo van `## Documentación general` (dónde vive, quién la mantiene, cómo se actualiza) y
`## Gestor de tareas` (Plane, Jira…; solo anotado, la skill no lo consulta).

## Fuentes

- `fuentes/` guarda tal cual lo que entregó el cliente o el equipo.
- **No se edita.** Una versión nueva se agrega con fecha (`AAAA-MM-DD-nombre.ext`).
- `fuentes/README.md` es el índice: Archivo · Entregado por · Fecha · Resumen. Leé el índice y
  abrí solo lo necesario.
- Las conclusiones van a `decisiones/` y citan la fuente.
- Si una fuente trae credenciales o secretos: **no la guardes** en el repo y avisá.

## Flujos

### 1. Crear centro
1. Preguntá para quién es y de dónde parte, y el nombre.
2. Creá la carpeta del centro como hermana de los repos de código y `git init`.
3. Detectá los repos hermanos y sus submódulos (`.gitmodules`) y proponé el manifiesto; el
   usuario confirma dueño y reglas.
4. Creá el mínimo más lo que el escenario sugiere. Nada comercial.
5. Si hay material entregado, `fuentes/` con su índice.
6. Primer commit. El remoto debe ser privado del usuario: preguntá, no lo crees por tu cuenta.

### 2. Adoptar centro existente
No reestructures. Revisá qué falta del mínimo (normalmente el manifiesto y, si hay documentación
general, la sección «Por llevar a la documentación general» de `pendientes.md`), proponelo y
agregalo tras aprobación. Si hay tablas de repos o reglas de repos en otros documentos o en la memoria,
pasalas al manifiesto y dejá un enlace.

### 3. Abrir sesión (estado del proyecto)
1. Leé el manifiesto.
2. Por **cada** pieza `local`, submódulos incluidos:
   `git -C <ruta> branch --show-current`, `git -C <ruta> status --short`,
   `git -C <ruta> log --oneline -3`. Si la ruta no existe, reportala como **faltante**. En un
   repo con submódulos, `git -C <ruta> submodule status`: un `+` es un commit sin registrar en el
   padre.
3. Leé `pendientes.md` y, si existe, `docs/modules/ESTADO.md`.
4. Entregá el diagnóstico:

   | Campo | Contenido |
   |---|---|
   | Repos | una línea por pieza: rama · cambios sin commit · último commit · faltante / sin acceso |
   | En curso | lo que está en desarrollo según docs y ramas |
   | Pendientes | lo más importante de `pendientes.md` |
   | Por llevar a la documentación general | filas pendientes, o «nada» |
   | Contradicciones | entre docs y git, o «ninguna» — nunca se omite |
   | Siguiente paso | una propuesta |

### 4. Delegar en un repo
Solo sobre piezas `local`. Si la pieza es `sin acceso` o `solo docs externas`, decilo y no
delegues. El encargo al agente incluye:
- ruta absoluta y rama;
- las reglas del manifiesto para ese repo;
- «**No escribas documentación ni planes en este repo. Entregá qué cambiaste, los commits y las
  pruebas.**» La documentación la escribe solo la sesión del centro.

### 5. Revisión antes de commit o PR en un repo ajeno
Aplica a toda pieza con dueño `cliente` o `equipo`, la hagas vos o un agente delegado.

1. Listá los archivos:
   - commit: `git -C <ruta> diff --cached --name-only`
   - PR: `git -C <ruta> diff --name-only <rama base>...HEAD`
2. **Bloqueá** si alguno coincide con: `docs/`, `CLAUDE.md`, `.claude/`, `AGENTS.md`,
   `docs/superpowers/`, cualquier archivo de plan o spec, o los patrones extra del manifiesto.
3. Si el manifiesto declara la ruta como excepción para ese repo, no bloquea.
4. Bloqueado: no hagas el commit ni el PR. Sacá esos archivos del stage, llevá su contenido al
   centro si sirve, y avisá al usuario qué se bloqueó. Nunca lo resuelvas en silencio.

### 6. Llevar a la documentación general
Al cerrar una decisión o una vertical en un proyecto con destino de documentación general, agregá
una fila en `pendientes.md` → «Por llevar a la documentación general». Si el usuario lo pide,
prepará el texto para pegar. Cuando confirme que lo llevó, marcá «llevado AAAA-MM-DD». La
publicación es manual.

## Reglas duras

- Nada del centro entra a un repo ajeno. Sin revisión (flujo 5), no hay commit ni PR en un repo
  `cliente` o `equipo`, aunque haya afán o el pedido diga «commit de todo».
- Un pedido de «dejar el plan registrado» en un repo ajeno se cumple en el centro, no en el repo.
- Nunca delegues ni toques una pieza que no esté `local`.
- Las fuentes no se editan ni se sobrescriben.
- Credenciales y secretos no entran al centro.
- Las reglas de cada repo viven solo en el manifiesto.
- El diagnóstico revisa git en **todas** las piezas `local`, no solo en el repo actual.

| Pensamiento | Realidad |
|---|---|
| «El usuario pidió commit de todo» | «Todo» es el código. El plan va al centro. |
| «Es un solo archivo de docs, no pasa nada» | Es justo lo que no puede llegar al cliente. Bloqueá y avisá. |
| «Ya revisé el repo donde estoy» | El estado del proyecto es el de todas las piezas del manifiesto. |
