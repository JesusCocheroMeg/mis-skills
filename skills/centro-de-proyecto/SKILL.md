---
name: centro-de-proyecto
description: Úsala cuando el usuario quiera crear, adoptar o abrir el repo centro de un proyecto (su espacio privado junto a los repos de código), arrancar el día o pedir el estado de un proyecto con varios repos, guardar fuentes que entregó un cliente o equipo, delegar trabajo a agentes en otros repos del proyecto, o hacer commit o PR en un repo que es del cliente o del equipo. También cuando el usuario cuenta lo que pasó en un proyecto (una reunión, un mensaje del cliente, un cambio, un problema), pregunta qué sigue, quiere preparar o cerrar una reunión, necesita que le expliquen algo para avanzar o busca herramientas para el proyecto. También ante menciones de centro, manifiesto, fuentes, bitácora o documentación general.
argument-hint: "[crear | adoptar | abrir sesión | contar | reunión | explicar | delegar | fuentes]"
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

El centro también es la **memoria y el copiloto** del proyecto: Jesús cuenta lo que va pasando,
el centro lo guarda como historia y responde con lo que sigue (flujos 7 a 9).

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
| De dónde parte | en evaluación · desde cero · ya empezado · en equipo | en evaluación (propuesta que se está revisando, sin acceso al código): `propuesta.md`, `preguntas.md`, `reuniones/`, repos como `sin acceso`; ya empezado: `diagnostico.md`; en equipo: destino de documentación general |

Cotizaciones: la skill no las crea por su cuenta. Si el usuario ya trae una propuesta comercial,
vive en `propuesta.md` y se trata como cualquier otro documento del centro.

## Estructura

**Mínimo obligatorio:** `README.md` (con `## Manifiesto`), `decisiones/`, `bitacora.md`,
`pendientes.md`. `fuentes/` si hay material entregado.

**Según escenario, se propone, no se impone:** `contexto/` (cliente, personas, negocio, stack),
`preguntas.md` (preguntas abiertas para el cliente), `reuniones/` (una por reunión),
`guias/` (explicaciones para avanzar), `propuesta.md`, `hoja-de-ruta.md` + `fases/`,
`diagnostico.md` (ya empezado), `implementacion/`, `argumentos.md`, `docs/modules/` (si se usa
desarrollo vertical), `docs/superpowers/` (specs y planes).

**Dónde va cada cosa que cuenta el usuario:**

| Lo que llega | Va a |
|---|---|
| Algo que pasó, una idea, una duda propia, un riesgo | `bitacora.md` (tipo `hecho` · `idea` · `pregunta` · `observación` · `riesgo`) |
| Algo que se decidió | `decisiones/NNNN-...md` |
| Algo por hacer o por decidir | `pendientes.md` |
| Una duda que solo el cliente responde | `preguntas.md` |
| Una respuesta del cliente | `preguntas.md` (`[x] → respuesta (fecha, quién)`) y lo que cambie en `contexto/`; cita la reunión o el mensaje de donde salió |
| Quién es quién, cómo trabaja el cliente, contexto personal | `contexto/` |
| Una explicación de algo que hay que aprender | `guias/<tema>.md` |

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
4. Creá el mínimo más lo que el escenario sugiere.
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
3. Leé `pendientes.md`, las últimas entradas de `bitacora.md` y, si existen, `preguntas.md`,
   la reunión más próxima en `reuniones/` y `docs/modules/ESTADO.md`.
4. Entregá el diagnóstico:

   | Campo | Contenido |
   |---|---|
   | Repos | una línea por pieza: rama · cambios sin commit · último commit · faltante / sin acceso |
   | Dónde vamos | la historia reciente en dos o tres líneas, desde la bitácora |
   | En curso | lo que está en desarrollo según docs y ramas |
   | Pendientes | lo más importante de `pendientes.md` |
   | Próxima reunión | fecha, con quién y preguntas abiertas que llevar, o «ninguna» |
   | Por llevar a la documentación general | filas pendientes, o «nada» |
   | Contradicciones | entre docs y git, o «ninguna» — nunca se omite |
   | Siguiente paso | una propuesta |

### 4. Delegar en un repo
Solo sobre piezas `local` cuya ruta existe. Si la pieza es `sin acceso`, `solo docs externas` o
su ruta no existe, decilo y no delegues. El encargo al agente incluye:
- ruta absoluta y rama;
- las reglas del manifiesto para ese repo;
- «**No escribas documentación ni planes en este repo. Entregá qué cambiaste, los commits y las
  pruebas.**» La documentación la escribe solo la sesión del centro;
- si el dueño es `cliente` o `equipo`, el bloque de **revisión antes de commit** (flujo 5, pasos
  1–4) copiado tal cual, con los patrones bloqueados y las excepciones del manifiesto para ese
  repo, y «**No hagas push ni abras PR**». El agente delegado no carga esta skill: lo que no esté
  en el encargo, no lo sabe.

Esto vale para cualquier forma de delegar, incluidos los implementadores de
`subagent-driven-development`: su encargo por tarea lleva este mismo bloque.

Cuando el agente termina, la sesión del centro repite la revisión del flujo 5 sobre sus commits
antes de cualquier push o PR.

### 5. Revisión antes de commit, push o PR en un repo ajeno
Aplica a toda pieza con dueño `cliente` o `equipo`, la hagas vos o un agente delegado.

1. Listá los archivos:
   - commit: `git -C <ruta> diff --cached --name-only` (no uses `git commit -a`: stageá
     explícitamente y revisá lo stageado);
   - push o PR: `git -C <ruta> fetch` y `git -C <ruta> diff --name-only origin/<rama base>...HEAD`
     — cubre todo lo commiteado que todavía no está en el remoto.
2. **Bloqueá** si alguno coincide con: `docs/`, `CLAUDE.md`, `.claude/`, `AGENTS.md`,
   `docs/superpowers/`, `*plan*.md`, `*spec*.md`, `*design*.md`, o los patrones extra del
   manifiesto.
3. Si el manifiesto declara la ruta como excepción para ese repo, no bloquea.
4. Bloqueado en un commit: no lo hagas. Sacá esos archivos del stage, llevá su contenido al
   centro si sirve y avisá al usuario qué se bloqueó.
5. Bloqueado en un push o PR (ya está en commits locales): no hagas push ni PR. Un commit que
   borra el archivo **no alcanza**: el contenido sigue en el historial que se subiría. Avisá al
   usuario y proponé reescribir el historial local (`git rebase -i` no está disponible: usá
   `git reset --soft origin/<rama base>` y volvé a commitear sin esos archivos, o
   `git filter-branch`/`git filter-repo` sobre el rango). Reescribir historial requiere su
   aprobación. Si los commits ya están en el remoto, decilo: ya se expuso y lo decide el usuario.

Nunca resuelvas un bloqueo en silencio.

### 6. Llevar a la documentación general
Al cerrar una decisión o una vertical en un proyecto con destino de documentación general, agregá
una fila en `pendientes.md` → «Por llevar a la documentación general». Si el usuario lo pide,
prepará el texto para pegar. Cuando confirme que lo llevó, marcá «llevado AAAA-MM-DD». La
publicación es manual.

### 7. Contar lo que pasó
Cuando el usuario cuenta algo (reunión, mensaje, llamada, cambio, problema, cómo se siente con
el proyecto):
1. Leé el README, `pendientes.md`, `preguntas.md` y lo de `contexto/` que toque el tema.
2. Registrá cada pieza donde dice la tabla «Dónde va cada cosa». La historia siempre queda en
   `bitacora.md` con su fecha. Si una fecha es ambigua («el lunes»), anotala como supuesto en la
   respuesta.
3. Respondé con estas secciones, en este orden, y omití las que queden vacías:

   | Sección | Contenido |
   |---|---|
   | **Registré** | archivos tocados, una línea cada uno |
   | **Qué cambia** | impacto en plan, tiempos, riesgos o decisiones; contradicciones con lo anotado |
   | **Te propongo** | el siguiente paso concreto, con opciones y una recomendación |
   | **Para preguntar** | preguntas nuevas para el cliente (ya agregadas a `preguntas.md`) |
   | **Para saber** | conceptos o herramientas que necesita para avanzar, en dos o tres líneas cada uno, con enlace a `guias/` si se escribió una |

   Lo personal (dudas, ánimo, relación con el cliente) cuenta como contexto: se anota y pesa en
   la propuesta.

### 8. Reuniones
**Preparar:** creá `reuniones/AAAA-MM-DD-con-quien.md` con objetivo, agenda, las preguntas de
`preguntas.md` que corresponden a esa persona, lo que conviene contar o explicar, y lo que no se
debe decir todavía.
Si el usuario menciona una reunión con fecha que no tiene archivo, creala preparada sin
preguntar y decilo en «Registré».
**Cerrar:** cuando el usuario cuenta cómo fue, llená notas, acuerdos y pendientes del archivo
de la reunión y seguí el flujo 7.

### 9. Explicar o proponer herramientas
Cuando el usuario necesita entender algo para avanzar (una tecnología, una pasarela, un trámite,
un concepto del negocio del cliente) o pide herramientas:
1. Partí del contexto del proyecto: explicá lo que sirve **para esta decisión**, no el tema en
   general.
2. Datos que cambian (precios, tarifas, límites, requisitos legales): consultá la fuente oficial
   si hay herramienta de búsqueda. Si no hay o la fuente oficial no responde, usá fuentes
   secundarias citadas y marcá «por verificar» con dónde confirmarlo.
3. Para herramientas: dos o tres opciones comparadas en lo que importa al proyecto, y una
   recomendación.
4. Si la explicación sirve para después, guardala en `guias/<tema>.md` y enlazala desde
   `pendientes.md` o la reunión donde se usa.

## Reglas duras

- Nada del centro entra a un repo ajeno. Sin revisión (flujo 5), no hay commit, push ni PR en un
  repo `cliente` o `equipo`, aunque haya afán o el pedido diga «commit de todo».
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
