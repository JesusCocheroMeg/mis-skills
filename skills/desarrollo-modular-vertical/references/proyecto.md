# Nivel de proyecto: DoD, alcance global, plataforma y revisión de PR

Se lee en los escenarios **K** (arrancar proyecto) y **L** (revisar PR), y al diseñar (D) o
cerrar (I) para consultar los cuidados del alcance global.

---

## K. Preguntas para arrancar el proyecto

Antes de preguntar: si no hay repo o carpeta `docs/`, preguntá primero dónde vivirá la
documentación (en el repo del código o en un centro, ver skill `centro-de-proyecto`).

Se hacen de a pocas, en el registro con que habla el usuario (tú o vos), con la herramienta de
preguntas si existe y, si no, en el chat. Lo que el usuario ya dijo no se pregunta de nuevo: se
confirma en una línea. Se recomienda una opción solo en preguntas técnicas (DoD, cuidados, plataforma); el
alcance de negocio lo decide el usuario sin recomendación. Las respuestas llenan los tres
archivos; nada se inventa.

**Alcance final** (llena `docs/alcance-global.md`):

1. ¿Qué tendrá que hacer el producto completo, aunque hoy entregues solo una parte?
2. ¿Para cuándo es la primera entrega (el MVP) y qué entra en ella? Ayudá a recortarla a lo
   mínimo que ya le sirve a alguien; lo que sale va a la tabla de capacidades futuras, no se pierde.
3. Recorré con el usuario esta lista y marcá cuáles podrían llegar algún día:
   - Varios idiomas o países (textos, monedas, fechas, zonas horarias)
   - Varias empresas o clientes en la misma instalación (multi-tenant)
   - Muchos más usuarios o datos (escala)
   - App móvil o trabajo sin conexión
   - Integraciones con otros sistemas (API pública, webhooks, MCP)
   - IA sobre los datos (asistente, búsqueda por significado)
   - Requisitos legales o de auditoría (datos personales, retención, trazabilidad)
   - Cambio de proveedor (nube, base, IA, pagos)
4. Para cada una marcada: ¿qué cuidado barato evita rehacer después? (ver ejemplos abajo).

**Definition of Done** (llena `docs/definition-of-done.md`):

5. ¿Quién aprueba los PR? ¿Hay carpetas que solo puede aprobar una persona?
6. ¿Qué tipos de cambio vas a distinguir? Proponé los cuatro de la DoD base y ajustalos.
7. ¿Qué se le exige a cada tipo? Partí de la DoD base y preguntá qué sobra o qué falta
   (cobertura mínima, prueba de punta a punta, captura de pantalla, aprobación de diseño…).
8. ¿Dónde viven los repos (GitHub, GitLab, otro)? Define la plantilla de PR y los checks.

**Plataforma** (llena `docs/plataforma.md`; se recomienda opción en todas, son técnicas):

9. Stack: lenguaje, framework, base de datos, nube, IA si aplica. Para cada pieza, el porqué en
   una línea, contrastado con el alcance global (que escale hasta donde se quiere llegar sin
   rehacerse). Si ya hay código, se documenta lo que hay y solo se pregunta lo que falta.
10. Pruebas: framework de unitarias y de punta a punta, y cobertura mínima si se quiere una.
11. CI/CD: ¿qué ambientes habrá (desarrollo, pruebas, producción)? ¿Qué dispara cada despliegue
    (merge a `main`, etiqueta, aprobación manual en el pipeline)? ¿Cómo se revierte?
12. Métricas de uso: ¿con qué herramienta? (proponé una que respete el cambio de proveedor y los
    datos personales). Eventos base: usuarios activos por día/semana, inicio de sesión y uso de
    cada función. ¿Quién mira el tablero y cada cuánto?

Al terminar: los tres archivos escritos, y una **propuesta** (no instalada) de automatización:
plantilla de PR con las casillas por tipo, checks de CI (pruebas, tipos, lint, commits) y reglas
por carpeta (por ejemplo: si cambió el núcleo y ningún archivo de prueba, falla), **pipeline de
despliegue por ambiente** (CD), protección de rama y dueños por carpeta. Se instala solo con
aprobación.

---

## Plantilla: `docs/plataforma.md`

```md
# Plataforma — <proyecto>

**Acordada:** <fecha> · Cambiar una pieza del stack es una decisión del usuario.

## Stack

| Pieza | Elegida | Por qué | Escala hasta |
|-------|---------|---------|--------------|
| Backend | <…> | <una línea> | <qué del alcance global soporta sin rehacerse> |
| Frontend | <…> | | |
| Base de datos | <…> | | |
| Nube / hosting | <…> | | |

## Pruebas

- Unitarias: <framework> · Punta a punta: <framework> · Cobertura mínima: <n % o «no se exige»>
- Se ejecutan en el CI en cada PR; un PR con pruebas en rojo no se fusiona.

## Despliegue (CI/CD)

| Ambiente | Se despliega cuando | Aprobación | Cómo se revierte |
|----------|---------------------|------------|------------------|
| Pruebas | merge a `main` | automática | redesplegar la versión anterior desde el pipeline |
| Producción | <etiqueta / aprobación en el pipeline> | <persona> | <…> |

Nada se despliega a mano. Secretos solo en el gestor de secretos del pipeline o de la nube.

## Métricas de uso

**Herramienta:** <…> · **Tablero:** <enlace> · **Lo revisa:** <persona, cada cuánto>

| Evento | Cuándo se emite | Propiedades (sin datos personales) |
|--------|-----------------|------------------------------------|
| `sesion_iniciada` | al entrar un usuario | `tenant`, `rol` |
| `<modulo>.<accion>` | al usar una función | <…> |

Nombres en `modulo.accion`, en minúsculas. Cada vertical que agrega una función agrega su fila.
```

---

## Plantilla: `docs/alcance-global.md`

```md
# Alcance global — <proyecto>

**Primera entrega:** <fecha y qué entra> · **Acordado:** <fecha>

El producto se entrega por partes pero se diseña para el alcance completo. Lo de esta tabla
**no se construye** hasta que entre a una versión; sus cuidados se cumplen desde hoy.

| ID | Capacidad futura | Cuándo podría llegar | Cuidados desde hoy | Estado |
|----|------------------|----------------------|--------------------|--------|
| G1 | Varios idiomas | después de la v1 | Ningún texto de pantalla escrito en el código: todo sale de un archivo de traducciones; fechas y monedas con `Intl`; nunca armar frases concatenando textos | Acordado |
| G2 | Varias empresas | v1 | `tenant_id` en todas las tablas y primero en los índices; ninguna consulta sin filtro de empresa | Acordado |
| G3 | Escala | cuando el monitoreo lo pida | App sin estado; lo pesado detrás de una cola con interfaz propia; lecturas pesadas por su propia conexión | Acordado |
| G4 | Cambios de base sin dolor | siempre | Migraciones solo aditivas (agregar, copiar, cambiar el código, después borrar); nunca renombrar o borrar una columna en el mismo paso en que deja de usarse | Acordado |

Estados: Propuesto · Acordado · En una versión · Descartado.
```

Un cuidado es **barato**: se cumple escribiendo el código de otra forma, no construyendo otra
cosa. Si cumplirlo cuesta trabajo real, es una decisión para el usuario.

---

## Plantilla: `docs/definition-of-done.md` (DoD base)

```md
# Definition of Done — <proyecto>

**Acordada:** <fecha> · **Aprueba los PR:** <persona> · **Dueños por carpeta:** <carpeta → persona>

Un PR se aprueba cuando cumple todas las casillas de **su tipo**. El tipo se decide por lo que
toca, no por lo que dice el título.

## Tipos

| Tipo | Se reconoce por | Ejemplos |
|------|-----------------|----------|
| Trivial | Cumple las cuatro condiciones del ajuste trivial; no toca lógica | Un texto, un color, un error de tipeo |
| Arreglo | Corrige un comportamiento sin agregar uno nuevo | `fix:` |
| Función | Agrega o cambia comportamiento; suele cerrar una vertical | `feat:` |
| Sensible | Toca esquema o migraciones, permisos, autenticación, datos personales, dependencias nuevas o infraestructura | Cualquier prefijo |

Si un PR cae en dos tipos, se le exige el más estricto. Si no hay documentación del módulo para
comprobar las condiciones del ajuste trivial, el PR no es trivial: es un arreglo.

## Casillas por tipo

| Casilla | Trivial | Arreglo | Función | Sensible |
|---------|:-------:|:-------:|:-------:|:--------:|
| Checks automáticos en verde (pruebas, tipos, lint, commits) | ✓ | ✓ | ✓ | ✓ |
| Prueba que habría detectado el error | | ✓ | | |
| Prueba de cada función nueva o cambiada, incluido el camino que falla | | | ✓ | ✓ |
| Documentación actualizada en el mismo PR (vertical, tabla de estado, guía de uso) | | si cambia algo visible | ✓ | ✓ |
| Decisiones nuevas registradas (hay decisión cuando el cambio altera algo que un documento afirma, como un tope, el esquema o un contrato, o elige entre alternativas) | | | ✓ | ✓ |
| Cuidados del alcance global respetados | ✓ | ✓ | ✓ | ✓ |
| Seguridad: entradas validadas, permisos en el servidor, sin secretos en el código o los logs | | ✓ | ✓ | ✓ |
| Prueba de permisos y de aislamiento de datos | | | si toca datos | si toca datos o permisos |
| Evento de uso emitido y registrado en `plataforma.md` | | | ✓ | si agrega una función |
| Se despliega por el pipeline, sin pasos a mano | | | | si toca infraestructura |
| Migración aditiva y reversible | | | | si hay migración |
| Aprobación del dueño de la carpeta | | | | ✓ |
```

---

## L. Informe de revisión de PR

El informe tiene estas partes, en este orden:

```md
## Revisión · <título o rama del PR>

**Tipo:** <Trivial | Arreglo | Función | Sensible> — <evidencia: archivos tocados, líneas, prefijo>
**DoD usada:** <docs/definition-of-done.md | DoD base de la skill (el proyecto no tiene una)>
**Veredicto:** <Aprobar | Aprobar con observaciones | Pedir cambios>

| Casilla | Resultado | Evidencia |
|---------|-----------|-----------|
| <casilla del tipo> | Cumple / No cumple / Sin verificar | <archivo:línea, salida del comando o del CI> |

### Lo que bloquea
<Cada «No cumple», con qué hacer para cumplirlo. Si no hay, «nada».>

### Documentación contra código
<Para cada documento que el cambio debía tocar: qué dice y qué hace el código. Contradicciones
primero. Si todo coincide, decilo.>

### Alcance global
<Los cuidados que el diff toca y si los cumple. Si no toca ninguno, decilo.>

### Observaciones
<Lo que no bloquea: mejoras, deuda que deja, algo para el roadmap.>
```

**Casillas que no aplican:** si el proyecto no tiene `docs/alcance-global.md`, esa casilla queda
«No aplica» (no bloquea ni baja el veredicto) y la recomendación de hacer el Escenario K va en
Observaciones. La falta de la línea en `verticals/ajustes-menores.md` de un PR trivial es una
observación, no un bloqueo.

**Veredicto:** «Pedir cambios» si alguna casilla de su tipo es «No cumple» o la documentación
contradice el código. «Aprobar con observaciones» si todo cumple pero hay «Sin verificar» que el
usuario puede comprobar o notas que no bloquean. «Aprobar» solo con todas las casillas en «Cumple».
