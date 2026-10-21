---
name: desarrollo-modular-vertical
description: Úsala cuando el usuario quiera iniciar un módulo, recuperar uno ya comenzado, auditar un prototipo, planificar una versión, diseñar o continuar una vertical, introducir un ajuste, revisar el avance o cerrar una vertical o versión. También ante menciones de módulos, verticales, versiones, decisiones, roadmap, alcance o implementación progresiva.
argument-hint: "[módulo, escenario o acción]"
---

# Desarrollo modular vertical

Pensar y documentar ampliamente; implementar **solo** la siguiente vertical aprobada.
Lo documentado no es alcance.

## Estructura obligatoria del módulo

`docs/modules/<module>/` tiene **exactamente estos archivos**. Ninguno más.

| Archivo | Dueño exclusivo de | Nunca contiene |
|---|---|---|
| `README.md` | entrada del módulo: reglas vigentes, **tabla de estado de las verticales**, siguiente paso | diseño, evidencia de pruebas |
| `vision.md` | propósito, responsabilidades, límites y capacidades futuras | avance, estados |
| `roadmap.md` | prioridades, ideas, bandeja de entrada y **deuda heredada** del prototipo | nada comprometido |
| `current-version.md` | alcance de la versión activa: qué entra, qué no, criterio de cierre | estados de verticales |
| `decisions.md` | las decisiones y el estado de cada una | estado de verticales o del código |
| `verticals/<ID>.md` | **ciclo completo de una vertical**: definición, diseño, criterios de aceptación y cierre con evidencia | su propio estado — está en la tabla del README |

Global: `docs/modules/ESTADO.md` — panel de módulos y dependencias.

**Un archivo fuera de esta lista es una excepción y hay que justificarla** (por ejemplo, un
contrato de frontera entre dos módulos, o `verticals/ajustes-menores.md` como bitácora de
ajustes triviales — ver Escenario H). No existen `changelog.md`, `audit.md` ni
`verticals/INDEX.md`: la evidencia de cierre vive en el archivo de la vertical, la deuda
heredada en `roadmap.md`, y el estado en la tabla del `README.md`.

**Plantillas obligatorias:** `references/plantillas.md`. Leelo **antes** de crear o
reestructurar cualquiera de estos archivos. Se copian sus encabezados tal cual: no se
inventan secciones ni se renombran.

**Estados de una vertical:** 💡 Idea · 📋 Definida · 🎨 En diseño · 👍 Diseño aprobado ·
🔨 En implementación · ✅ Implementada · ⛔ Bloqueada · ❌ Descartada.

## Dueño único de cada dato

Cada dato tiene **un único documento dueño**; los demás lo enlazan. Replicar un dato es la
causa número uno de documentación que miente.

Si dos documentos se contradicen, **gana el dueño del dato** y el otro se corrige en el mismo
cambio. **Excepción:** si Git o el código demuestran que el dueño se equivoca, gana la
evidencia — se corrige el dueño y se explica por qué. Nunca resuelvas una contradicción en
silencio: informala en el diagnóstico.

## Lectura mínima para reconstruir el estado

1. `docs/modules/ESTADO.md`
2. `docs/modules/<module>/README.md` — reglas, tabla de verticales y siguiente paso

Más `git log --oneline -5`, `git status` y la rama actual. Eso es todo el estado.

**Si el repo es un centro** (su `README.md` tiene `## Manifiesto`, ver skill `centro-de-proyecto`):
`docs/modules/` vive en el centro y el código en los repos del manifiesto. La lectura de git
(rama, `git status`, últimos commits) se hace en **cada repo del manifiesto que toca la
vertical**, submódulos incluidos (`git -C <ruta> …`), no solo en el centro.

`vision.md`, `roadmap.md`, `current-version.md` y `decisions.md` son **consulta bajo
demanda**: se abren para decidir o diseñar algo concreto, nunca para saber cómo va el módulo.
Son los más grandes y los que menos cambian; leerlos por rutina agota el contexto sin aportar
estado. `decisions.md` empieza con una tabla-índice: leé la tabla y bajá solo a la decisión
que te importa.

No confíes únicamente en la conversación. Revisá también cambios sin confirmar, código
relacionado y planes o especificaciones ya generados.

## Paso 1: detectar el módulo

Por argumentos, solicitud actual, documentación existente, rama, archivos modificados o
código relacionado. Si hay varios candidatos, presentá las evidencias y elegí el más
directamente relacionado con la solicitud.

## Paso 2: clasificar el escenario

| # | Se usa cuando | Produce | Prohibido | Superpower |
|---|---|---|---|---|
| **A. Módulo nuevo** | no hay código ni documentación suficiente | `vision.md`, `roadmap.md`, una primera versión pequeña en `current-version.md` y el `README.md` con sus verticales en `📋 Definida` | escribir código | `brainstorming` |
| **B. Auditar prototipo** | hay código anterior a esta metodología | cada parte clasificada en conservar / ajustar / reubicar / reconstruir / eliminar, en la sección «Deuda heredada» de `roadmap.md`, fechada | modificar código; borrar el prototipo sin auditarlo | — |
| **C. Planificar versión** | hay visión y roadmap, pero no versión activa clara | `current-version.md`: objetivo, qué entra, qué no, criterio de cierre y las verticales | comprometer una versión sin dividirla en verticales | — |
| **D. Diseñar vertical** | la vertical existe y no tiene diseño aprobado | `verticals/<ID>.md` con diseño y criterios de aceptación; entidades, endpoints, permisos, validaciones, riesgos y regresiones; decisiones nuevas en `decisions.md` | escribir código | `brainstorming` |
| **E. Planificar vertical** | el diseño está aprobado y no hay plan | plan por tareas: objetivo, archivos, cambios, pruebas, resultado esperado, commit sugerido | implementar; salir del alcance de la vertical activa | `writing-plans` |
| **F. Implementar** | diseño **y** plan aprobados | la primera tarea incompleta, sus pruebas ejecutadas, el diff revisado y un commit pequeño | adelantar tareas; refactorizar fuera del alcance | `test-driven-development`, `subagent-driven-development` |
| **G. Continuar vertical** | la vertical ya está en desarrollo | la siguiente tarea pendiente, tras confirmar la última completada contra Git y las pruebas | repetir tareas hechas, salvo que la evidencia muestre un error | — |
| **H. Ajuste posterior** | cambia algo ya diseñado, implementado o en curso | análisis de impacto, decisión registrada, diseño actualizado y un plan corto | tratarlo como una instrucción aislada; implementar antes de aprobar | — |
| **I. Cerrar vertical** | todas las tareas están implementadas | **dos escrituras y ninguna más**: la fila del `README.md` pasa a `✅ Implementada` con fecha y commit; el archivo de la vertical gana su sección «Cierre» con la evidencia (en un centro, con el commit de cada repo tocado; y si el centro tiene `## Documentación general`, una tercera escritura permitida: la fila en `pendientes.md` → «Por llevar a la documentación general») | declarar el cierre sin pruebas ejecutadas | `verification-before-completion`, `requesting-code-review` |
| **J. Cerrar versión** | todas las verticales comprometidas están cerradas | diff completo contra la base, verificaciones repetidas, migraciones y documentación confirmadas, rama y PR | dejar archivos accidentales | `finishing-a-development-branch` |

**Vertical pequeña (atajo a D+E):** aplicá el atajo solo si se cumplen **las cuatro**
condiciones:

1. No crea ni modifica entidades de datos ni contratos/endpoints consumidos por otro módulo.
2. No requiere diseño de permisos/RBAC nuevo.
3. Objetivo y criterios de aceptación caben en menos de 10 líneas sin ambigüedad.
4. Se implementa en un commit o una tanda corta de commits directamente relacionados, sin
   descomponerla en tareas independientes.

Si las cuatro se cumplen: en un solo paso escribí en `verticals/<ID>.md` el objetivo, los
criterios de aceptación (lista corta) y los archivos/cambios — sin invocar `brainstorming` ni
`writing-plans`, sin la tabla completa de entidades/endpoints/permisos/validaciones/riesgos.
Sigue el ciclo normal de estados del `README.md` (📋→🎨→👍→🔨→✅): a diferencia del ajuste
trivial, sigue siendo una vertical con vida propia — solo el diseño y el plan se resuelven
juntos y livianos, y necesitan la aprobación del usuario igual que D y E por separado. Si
alguna condición no se cumple, son D y E completos tal como están descritos arriba.

En **G**, antes de escribir verificá que `HEAD` siga donde estaba (`git log --oneline -3`):
otra sesión pudo haber avanzado en paralelo y el estado que leíste ya venció.

**Ajuste trivial (excepción a H):** aplicá el camino corto solo si se cumplen **las cuatro**
condiciones:

1. No cambia la firma de ninguna función, endpoint o contrato consumido por otro módulo.
2. No cambia el comportamiento descrito en el diseño aprobado de la vertical activa.
3. No agrega, quita ni modifica un criterio de aceptación.
4. Se resuelve en un commit y se explica en una frase.

Si las cuatro se cumplen: una línea en `verticals/ajustes-menores.md` (fecha · descripción ·
commit) e implementación directa — sin análisis de impacto, sin `decisions.md`, sin diseño
actualizado, sin plan. Si alguna no se cumple, es un ajuste completo: Escenario H tal como
está descrito arriba.

`verticals/ajustes-menores.md` es una bitácora, no una vertical con ciclo de vida: no entra en
la tabla de estados del `README.md`, no pasa por los estados 💡📋🎨👍🔨✅ y nunca se cierra (no
aplica el Escenario I). Solo crece.

En **I**, tocá `roadmap.md` o `current-version.md` **solo si cambió el alcance o una
prioridad**. Reflejar avance no es motivo. Y si la verificación técnica pasó pero el usuario
todavía no lo validó en el navegador, decilo en la fila del README: no la presentes como
validada.

## Paso 3: ideas futuras

Toda idea nueva se registra en `roadmap.md` como `💡 Idea` y no entra a la versión activa ni
se implementa dentro de otra tarea. Se promueve solo cuando fue analizada, aprobada, asignada
a una versión, convertida en vertical y tiene plan aprobado. Si es indispensable para un
criterio de aceptación vigente, hacé análisis de impacto antes de continuar.

## Paso 4: decisiones

Formato y estados: `references/plantillas.md`. Podés **proponer** decisiones; no podés
marcarlas como aprobadas sin evidencia de aprobación del usuario. No vuelvas a preguntar por
una decisión ya aprobada y documentada.

## Paso 5: diagnóstico

Antes de ejecutar una etapa nueva, presentá: módulo · escenario · versión activa · vertical
activa · rama · evidencias revisadas · último avance confirmado · **contradicciones
detectadas** · decisiones pendientes · siguiente acción · documentos a actualizar ·
superpower recomendada.

El campo de contradicciones **no se omite ni se deja vacío**: si no encontraste ninguna,
escribí "ninguna". Resolver una contradicción por criterio propio y seguir sin decirlo es el
modo en que la documentación pierde autoridad sin que nadie se entere.

Si la solicitud ya autoriza la siguiente acción y existen las aprobaciones requeridas,
continuá sin pedir una confirmación repetida.

## Reglas duras

- Sin requerimiento claro, no inventar reglas de negocio.
- **Sin diseño aprobado, no se programa. Sin plan aprobado, no se implementa.** Excepción: un
  ajuste trivial que cumple las cuatro condiciones del Escenario H.
- Una tarea, una responsabilidad. Un commit pequeño y coherente.
- No ampliar el alcance en silencio.
- Sin pruebas ejecutadas, no se afirma que algo terminó.
- Toda decisión nueva se documenta; toda idea futura se registra sin implementarse.
- Todo ajuste posterior exige análisis de impacto, salvo el ajuste trivial (Escenario H).
- **Cada dato tiene un único documento dueño.** El estado de una vertical vive solo en la
  tabla del `README.md`.
- **No crear archivos fuera de la estructura obligatoria** ni resucitar `changelog.md`,
  `audit.md` o `verticals/INDEX.md`.
- Al iniciar sesión, reconstruir el estado con la lectura mínima y con Git antes de continuar.
- En un centro, los agentes delegados en repos de código no escriben documentación: entregan
  cambios, commits y pruebas, y solo la sesión del centro escribe en `docs/modules/`.
