# Nivel de proyecto: DoD, alcance global y revisión de PR

Se lee en los escenarios **K** (arrancar proyecto) y **L** (revisar PR), y al diseñar (D) o
cerrar (I) para consultar los cuidados del alcance global.

---

## K. Preguntas para arrancar el proyecto

Se hacen de a pocas (con la herramienta de preguntas si existe), con una opción recomendada
primero. Las respuestas llenan los dos archivos; nada se inventa.

**Alcance final** (llena `docs/alcance-global.md`):

1. ¿Qué tendrá que hacer el producto completo, aunque hoy entregues solo una parte?
2. ¿Para cuándo es la primera entrega y qué entra en ella?
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

Al terminar: los dos archivos escritos, y una **propuesta** (no instalada) de automatización:
plantilla de PR con las casillas por tipo, checks de CI (pruebas, tipos, lint, commits) y reglas
por carpeta (por ejemplo: si cambió el núcleo y ningún archivo de prueba, falla), protección de
rama y dueños por carpeta. Se instala solo con aprobación.

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

Si un PR cae en dos tipos, se le exige el más estricto.

## Casillas por tipo

| Casilla | Trivial | Arreglo | Función | Sensible |
|---------|:-------:|:-------:|:-------:|:--------:|
| Checks automáticos en verde (pruebas, tipos, lint, commits) | ✓ | ✓ | ✓ | ✓ |
| Prueba que habría detectado el error | | ✓ | | |
| Prueba de cada función nueva o cambiada, incluido el camino que falla | | | ✓ | ✓ |
| Documentación actualizada en el mismo PR (vertical, tabla de estado, guía de uso) | | si cambia algo visible | ✓ | ✓ |
| Decisiones nuevas registradas | | | ✓ | ✓ |
| Cuidados del alcance global respetados | ✓ | ✓ | ✓ | ✓ |
| Seguridad: entradas validadas, permisos en el servidor, sin secretos en el código o los logs | | ✓ | ✓ | ✓ |
| Prueba de permisos y de aislamiento de datos | | | si toca datos | ✓ |
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

**Veredicto:** «Pedir cambios» si alguna casilla de su tipo es «No cumple» o la documentación
contradice el código. «Aprobar con observaciones» si todo cumple pero hay «Sin verificar» que el
usuario puede comprobar o notas que no bloquean. «Aprobar» solo con todas las casillas en «Cumple».
