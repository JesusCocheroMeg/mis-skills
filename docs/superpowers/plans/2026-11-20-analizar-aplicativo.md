# analizar-aplicativo · Plan de construcción

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construir la skill `analizar-aplicativo` (modos mapa, profundizar y comparar), instalarla en
`~/.claude/skills/` y probarla en un proyecto ajeno de Jesús.

**Architecture:** Una skill de Claude Code en `mis-skills/skills/analizar-aplicativo/`: `SKILL.md` corto con el
flujo y las reglas duras, guías en `references/` que se leen según el modo, y `assets/plantilla.html` con el estilo
de las láminas de ARM. No hay código ejecutable salvo un script de verificación de la presentación generada.

**Tech Stack:** Markdown (skill), HTML + CSS + SVG en línea (plantilla), Python 3 sin dependencias (verificador).

**Spec:** `docs/superpowers/specs/2026-11-20-analizar-aplicativo-design.md`

## Global Constraints

- Español con tildes; términos técnicos e identificadores en su forma original.
- HTML local que abre con doble clic; sin librerías externas salvo Google Fonts (Inter, JetBrains Mono); diagramas en SVG en línea; modo claro y oscuro; legible a 375 px de ancho.
- Solo lectura sobre el aplicativo analizado; nunca escribir dentro de un repo ajeno.
- Nunca copiar el valor de un secreto, contraseña, llave ni dato personal real.
- Marcas de fuente: **comprobado** (con ruta), **deducido**, **por confirmar**.
- Ubicación: `explicaciones/` del centro del proyecto al que pertenece; si no pertenece a ninguno, `~/Desktop/Desarrollo/Analisis/<aplicativo>/`. Registro de conceptos: `~/Desktop/Desarrollo/Analisis/conceptos-aprendidos.md`.
- Nombres: `mapa-<aplicativo>.html` (sin fecha, se actualiza), `AAAA-MM-DD-<aplicativo>-<tema>.html`, `AAAA-MM-DD-comparar-<a>-<b>[-<tema>].html`.
- Commits en inglés con Conventional Commits; trabajo en la rama `docs/analizar-aplicativo-design` (worktree del scratchpad).

## Review Focus

1. **Repo con un `.env` o llaves en el código:** la presentación no debe contener ningún valor; el verificador (Tarea 1) lo detecta.
2. **Repo sin documentación ni README:** la skill igual produce el mapa, con más «deducido» y «por confirmar», sin inventar con tono seguro.
3. **Repo muy grande o monorepo:** reparte la lectura (lectores.md) y no se queda en la primera carpeta.
4. **Profundizar sin mapa previo:** avisa y ofrece hacer el mapa, o sigue con contexto mínimo.
5. **Mapa que ya existe y código que avanzó:** lo actualiza (no crea otro) y llena «Qué cambió».

---

### Task 1: Plantilla HTML y verificador

**Files:**
- Create: `skills/analizar-aplicativo/assets/plantilla.html`
- Create: `skills/analizar-aplicativo/scripts/verificar.py`

**Interfaces:**
- Produces: clases CSS `.slide`, `.box`, `.grid.g2/.g3`, `.flow/.step`, `.analogy`, `.scroll table`, `.tag.ok/.prop/.tbd/.idea`, marcas `.marca.comprobado/.deducido/.confirmar`, veredictos `.veredicto.sostiene/.limite/.frena`, `.diagram` (SVG con `.node`, `.node.b/.ok/.w`, `.arr`, `.arr.d`); marcadores `{{TITULO}}`, `{{CONTENIDO}}`.
- Produces: `python3 -I scripts/verificar.py <ruta.html> [--repo <ruta-repo>]` → sale 0 si pasa; 1 con la lista de fallas.

- [ ] **Step 1:** Escribir `plantilla.html` partiendo de los estilos de `ARM/arm-centro/explicaciones/2026-11-20-el-worker-de-armega.html`, más las clases de marcas y veredictos, y una sección de ejemplo de cada componente.
- [ ] **Step 2:** Escribir `verificar.py` con estas comprobaciones: tiene `<title>`; todo `<svg>` tiene `role="img"` y `aria-label`; no carga scripts externos; hay al menos una marca; si se pasa `--repo`, ningún valor de variables de los `.env*` del repo (de 8 o más caracteres) aparece en el HTML, ni cadenas con forma de llave (`sk-`, `AKIA`, `-----BEGIN`).
- [ ] **Step 3:** Probar el verificador: pasa sobre la plantilla; falla sobre una copia con un `<script src="https://...">` y sobre otra con un valor de un `.env` de prueba creado en un directorio temporal.
- [ ] **Step 4:** Abrir la plantilla (`open`) y revisar claro, oscuro y ancho de celular.
- [ ] **Step 5:** Commit `feat(analizar-aplicativo): add template and output checker`.

### Task 2: Guías de método

**Files:**
- Create: `skills/analizar-aplicativo/references/marcas.md`, `negocio.md`, `alcance-y-limites.md`, `seguridad.md`, `diagramas.md`, `lectores.md`

**Interfaces:**
- Consumes: clases de la Tarea 1 (cada guía muestra el HTML del componente que le toca).
- Produces: las guías que `SKILL.md` y las guías de modo citan por nombre de archivo.

- [ ] **Step 1:** `marcas.md`: cuándo va cada marca, que «comprobado» lleva la ruta (`archivo:línea` o documento), y el conteo final.
- [ ] **Step 2:** `negocio.md`: aplicativo propio (leer brief, decisiones, verticales, centro; señalar donde documento y código no coinciden) y ajeno (deducir de modelos de datos, rutas, pantallas, textos, roles, nombres de estados).
- [ ] **Step 3:** `alcance-y-limites.md`: tabla objetivo · cómo está construido · límite · cuándo se llega · qué haría falta · veredicto; con el ejemplo de la cola en PostgreSQL de ARMEGA.
- [ ] **Step 4:** `seguridad.md`: qué revisar (ingreso, permisos, aislamiento, secretos, datos sensibles, dependencias, entradas sin validar), cómo redactar un riesgo (qué, dónde, por qué importa; nunca el valor ni un paso a paso para explotarlo) y la regla del centro privado o público.
- [ ] **Step 5:** `diagramas.md`: cuatro tipos (flujo del usuario, arquitectura de piezas, flujo de datos, secuencia de un proceso), cuándo usar cada uno y su esqueleto SVG con las clases de la plantilla.
- [ ] **Step 6:** `lectores.md`: cuándo repartir (más de ~300 archivos de código o más de un repo), los tres encargos (negocio; piezas y datos; seguridad) y el formato de hallazgo que devuelven (afirmación, marca, ruta).
- [ ] **Step 7:** Commit `feat(analizar-aplicativo): add method references`.

### Task 3: Guías de los tres modos

**Files:**
- Create: `skills/analizar-aplicativo/references/mapa.md`, `profundizar.md`, `comparar.md`

**Interfaces:**
- Consumes: guías de la Tarea 2; plantilla de la Tarea 1.

- [ ] **Step 1:** `mapa.md`: las 11 secciones del diseño en orden, qué va en cada una, más la cabecera con fecha y commit analizado y la sección «Qué cambió desde la última vez» al actualizar.
- [ ] **Step 2:** `profundizar.md`: la forma de la lámina del worker (analogía, paso a paso con diagrama, herramientas y porqué, dónde vive, qué del negocio sostiene, alternativas, seguridad, alcance y límites, qué mirar y qué preguntar, para aprender); qué hacer si no hay mapa; agregar su enlace en la sección 9 del mapa.
- [ ] **Step 3:** `comparar.md`: las secciones del flujo de comparar del diseño y la lista «qué no debe perderse en un reemplazo»; enlazarlo desde los mapas de ambos.
- [ ] **Step 4:** Commit `feat(analizar-aplicativo): add mode guides`.

### Task 4: SKILL.md, instalación y frontera con centro-de-proyecto

**Files:**
- Create: `skills/analizar-aplicativo/SKILL.md`
- Modify: `README.md` (fila en la tabla de skills)
- Modify: `skills/centro-de-proyecto/SKILL.md` (descripción: remitir a `analizar-aplicativo` para «analiza», «profundiza», «compara» y «cómo está hecho X del aplicativo»; sus láminas también anotan conceptos en el registro)

- [ ] **Step 1:** `SKILL.md` con frontmatter `name: analizar-aplicativo` y una descripción en español que se active con «analiza este aplicativo/proyecto/repo», «profundiza en…», «compara X con Y», «cómo está hecho / cómo funciona por dentro», «qué tan seguro es», «aguanta…», y que diga que no es para documentos a otros (`documentos-para-compartir`) ni para contenido de redes (`revision-tecnica`). Cuerpo: elegir modo, ubicar el proyecto y su centro, qué guía leer en cada paso, reglas duras (solo lectura, nada de secretos, marcas, registro de conceptos, preguntas y pendientes cuando hay centro), verificar con `verificar.py`, guardar, indexar y abrir.
- [ ] **Step 2:** Agregar la fila al README y la línea a `centro-de-proyecto`.
- [ ] **Step 3:** Instalar: `ln -sfn "<repo mis-skills principal>/skills/analizar-aplicativo" ~/.claude/skills/analizar-aplicativo`. Mientras la rama no se una, el enlace apunta al worktree; al unir, se rehace hacia la carpeta principal.
- [ ] **Step 4:** Verificar: `ls -l ~/.claude/skills/analizar-aplicativo/SKILL.md` existe y una sesión nueva lista la skill.
- [ ] **Step 5:** Commit `feat(analizar-aplicativo): add skill`.

### Task 5: Registro de conceptos con carga inicial

**Files:**
- Create: `~/Desktop/Desarrollo/Analisis/conceptos-aprendidos.md` (fuera del repo; dato personal)

- [ ] **Step 1:** Leer las secciones «Para aprender» de `ARM/arm-centro/explicaciones/*.html` y sacar cada concepto con una línea y su enlace a la lámina.
- [ ] **Step 2:** Escribir el registro como tabla: concepto · explicación corta · dónde se enseñó · fecha. Sin duplicados.
- [ ] **Step 3:** Verificar que incluye al menos worker, cola, cron, RLS, idempotente y pg-boss.

### Task 6: Prueba en el proyecto ajeno

**Files:**
- Create: `~/Desktop/Desarrollo/Analisis/<aplicativo>/mapa-<aplicativo>.html` y `README.md`

- [ ] **Step 1:** Anotar `git status --porcelain` del repo ajeno antes de empezar.
- [ ] **Step 2:** En una sesión nueva (o subagente sin este contexto), pedir «analiza este aplicativo» sobre el repo, para que la skill se use como la usará Jesús.
- [ ] **Step 3:** Correr `python3 -I scripts/verificar.py <mapa> --repo <repo>` → sale 0.
- [ ] **Step 4:** Comprobar que `git status --porcelain` del repo ajeno no cambió.
- [ ] **Step 5:** Abrir el mapa y revisarlo con Jesús contra los objetivos del diseño; anotar lo que falle y ajustar las guías.
- [ ] **Step 6:** Commit de los ajustes `fix(analizar-aplicativo): ...` y push de la rama.
