---
name: prompt-builder
description: Use when the user asks to create, revise, or rewrite implementation prompts for features, modules, endpoints, or any software task. Triggers on requests like "crea un prompt para...", "haz un prompt de...", "revisa el prompt de...", "necesito un prompt rápido para...". Never implements the functionality described.
---

# prompt-builder

Transforma solicitudes informales o resumidas en prompts claros, completos y listos para usar en otra sesión o agente de IA.

**Restricción absoluta:** Esta skill NUNCA implementa la funcionalidad descrita. Solo crea o revisa prompts y los guarda. Termina al guardar el archivo.

## Modos

| Modo | Cuándo usarlo |
|------|---------------|
| `create` | Módulo nuevo, varios endpoints, nueva entidad, frontend + backend, flujo completo |
| `revise` | Ya existe un prompt; el usuario quiere modificarlo, ampliarlo, reducirlo o actualizarlo |
| `quick` | Cambio puntual en funcionalidad existente; afecta pocos archivos; sin cambios arquitectónicos |

### Detección automática del modo

```dot
digraph modo {
    "¿El usuario indica la ruta de un prompt existente o pide revisar/corregir/ampliar?" [shape=diamond];
    "¿Es un cambio puntual en algo ya existente?" [shape=diamond];
    "revise" [shape=box];
    "quick" [shape=box];
    "create" [shape=box];

    "¿El usuario indica la ruta de un prompt existente o pide revisar/corregir/ampliar?" -> "revise" [label="sí"];
    "¿El usuario indica la ruta de un prompt existente o pide revisar/corregir/ampliar?" -> "¿Es un cambio puntual en algo ya existente?" [label="no"];
    "¿Es un cambio puntual en algo ya existente?" -> "quick" [label="sí"];
    "¿Es un cambio puntual en algo ya existente?" -> "create" [label="no"];
}
```

Si hay duda entre `create` y `quick`, usar `quick` cuando el cambio esté claramente delimitado.

## Proceso

### Modo create

1. Leer la solicitud.
2. Analizar brevemente el proyecto (README, package.json, estructura de src/, modelos, rutas relacionadas, prompts anteriores similares).
3. Identificar la capa afectada: backend / frontend / fullstack / base de datos / diseño / documentación / infraestructura.
4. Redactar el prompt completo con la estructura definida más abajo.
5. Decidir si generar uno o dos archivos (ver División de prompts).
6. Guardar en `docs/superpowers/promts/` con la convención de nombres.
7. Responder con el resumen de cierre. **No implementar nada.**

### Modo revise

1. Leer el archivo indicado.
2. Leer la solicitud de cambio.
3. Mantener lo que siga siendo válido.
4. Modificar, agregar o eliminar solo lo necesario.
5. Detectar contradicciones; priorizar la instrucción más reciente.
6. Revisar brevemente el estado actual del proyecto si es necesario.
7. Guardar como nueva versión (`-v2`, `-v3`, etc.) salvo que el usuario pida sobrescribir.
8. Responder con el resumen de cierre. **No implementar nada.**

### Modo quick

1. Leer la solicitud.
2. Revisar únicamente el módulo y archivos directamente relacionados.
3. Identificar el comportamiento actual y el cambio exacto requerido.
4. Redactar un prompt corto y preciso con la estructura de modo quick.
5. Guardar en `docs/superpowers/promts/`.
6. Responder con el resumen de cierre. **No implementar nada.**

## Ruta de almacenamiento

```
docs/superpowers/promts/
```

Si la carpeta no existe, crearla. Mantener exactamente este nombre.

## Convención de nombres

`YYYY-MM-DD-descripcion-corta.md`

- Minúsculas, guiones, sin espacios, sin tildes, sin caracteres especiales.
- Ejemplos: `2026-06-25-auth-backend.md`, `2026-06-25-fix-filtro-clientes.md`
- Revisiones: `2026-06-25-productos-backend-v2.md`, `-v3.md`, etc.

## División de prompts

- Crear **dos archivos** cuando backend y frontend sean trabajos claramente independientes.
- Crear **un solo archivo** cuando la tarea sea pequeña o tenga sentido implementarlos juntos.
- En modo `quick`, un solo archivo salvo que el cambio afecte ambas capas de forma independiente.

Ejemplos de nombres divididos:
- `2026-06-25-clientes-backend.md`
- `2026-06-25-clientes-frontend.md`

## Encabezado de cada archivo generado

```markdown
---
title: "Título del prompt"
created_at: "YYYY-MM-DD"
scope: "backend | frontend | fullstack | database | design | documentation | infrastructure"
mode: "create | revise | quick"
status: "draft"
source_prompt: ""
version: 1
---
```

En revisiones: `source_prompt` = ruta original, `version` se incrementa, `mode: revise`.

## Estructura del prompt — Modo create

Adaptar según la solicitud. Incluir las secciones que apliquen:

- **Título** — nombre claro de la tarea.
- **Contexto del proyecto** — stack, arquitectura y estado actual relacionado. Solo información confirmada.
- **Estado actual** — qué existe y desde dónde parte la implementación.
- **Objetivo** — qué debe lograr la tarea.
- **Alcance** — funcionalidades o ajustes incluidos.
- **Requisitos funcionales** — comportamiento esperado desde el negocio o usuario.
- **Requisitos técnicos** — stack, convenciones, estructura, librerías, patrones a reutilizar.
- **Reglas de negocio** — roles, estados, relaciones, validaciones, flujos, restricciones MVP.
- **Seguridad y permisos** — cuando aplique: autenticación, autorización, roles, 401/403.
- **Endpoints** — método, ruta, objetivo, body, params, respuesta, códigos HTTP, permisos. Solo los necesarios.
- **Interfaz** — rutas, páginas, componentes, formularios, tablas, paginación, estados vacíos, errores, responsive.
- **Validaciones y errores** — campos obligatorios, formatos, duplicados, recursos inexistentes.
- **Integración con lo existente** — servicios, middlewares, componentes, hooks, tipos a reutilizar. Pedir no duplicar lógica.
- **Pruebas** — casos exitosos, datos inválidos, permisos, paginación, seguridad. Cuando aplique.
- **Criterios de aceptación** — lista verificable y concreta.
- **Fuera de alcance** — qué no debe implementarse.
- **Validaciones finales** — solo comandos confirmados en el proyecto (typecheck, build, lint, tests). No inventar comandos.
- **Entrega esperada** — archivos creados/modificados, decisiones, migraciones, resultados reales, supuestos, limitaciones.

## Estructura del prompt — Modo quick

Más breve. Incluir:

- **Título** — nombre corto del ajuste.
- **Contexto breve** — qué funcionalidad ya existe.
- **Cambio requerido** — qué debe modificarse exactamente.
- **Comportamiento esperado** — cómo debe funcionar tras el cambio.
- **Módulos o archivos a revisar** — qué parte del proyecto inspeccionar. No inventar rutas exactas sin verificar.
- **Restricciones** — qué no debe alterarse (comportamiento actual, contratos de API, otros módulos, permisos).
- **Validaciones** — solo las necesarias.
- **Criterios de aceptación** — entre 3 y 8 criterios claros.
- **Validaciones finales** — typecheck/build/tests solo si existen en el proyecto.

No incluir secciones extensas de arquitectura, seguridad o pruebas si no son relevantes.

## Análisis permitido

La skill puede leer archivos del proyecto para obtener contexto:

- README.md, CLAUDE.md, documentación.
- package.json, tsconfig.json.
- Estructura de src/, modelos Prisma, rutas, servicios, componentes similares.
- Convenciones de nombres, variables de entorno documentadas.
- Pruebas existentes, prompts anteriores relacionados.

En modo `quick`, analizar únicamente el módulo afectado y archivos relacionados.

Cuando falte información no crítica: usar el contexto encontrado, mantener alcance conservador, incluir supuestos explícitos. Solo hacer una pregunta al usuario si falta un dato esencial que impida crear un prompt útil.

## Contexto MVP

Cuando el proyecto sea un MVP, diferenciar en el prompt:

- Necesario para el MVP.
- Opcional para el MVP.
- Futuro recomendable.
- Fuera de alcance.

## Reglas de redacción de los prompts generados

Los prompts deben estar escritos en español, ser claros y directos, adaptados al proyecto real. Deben:

- Pedir revisar el repositorio antes de modificarlo.
- Pedir reutilizar implementaciones existentes.
- Pedir no duplicar componentes, servicios o utilidades.
- Mantener compatibilidad con la arquitectura actual.
- Incluir seguridad y permisos cuando aplique.
- Incluir paginación cuando la solicitud la requiera.
- No afirmar que algo existe sin verificarlo.
- No inventar dependencias, rutas o modelos.
- Explicitar supuestos si son necesarios.

Pueden incluir ejemplos mínimos de payloads JSON, rutas, nombres de campos o estructuras de carpetas. No deben incluir componentes, controladores, servicios o migraciones completas.

## Restricciones absolutas

La skill NUNCA debe:

- Modificar código del proyecto.
- Crear componentes, endpoints, modelos o migraciones funcionales.
- Ejecutar el prompt generado.
- Crear un plan técnico de implementación separado.
- Modificar archivos fuera de `docs/superpowers/promts/` (salvo los propios de la skill).
- Continuar trabajando después de guardar el prompt.

## Respuesta de cierre

Después de guardar el archivo, responder únicamente con:

```
Skill: prompt-builder
Modo: [create | revise | quick]
Archivo: `nombre-del-archivo.md`
Ruta: `docs/superpowers/promts/nombre-del-archivo.md`
[Archivo original: `ruta-original` — solo en revisiones]
[Versión: N — solo en revisiones]
Resumen: [una o dos líneas describiendo el prompt generado]
```

No incluir el contenido completo del prompt en la respuesta si ya fue guardado, salvo que el usuario lo solicite explícitamente.

## Ejemplos de invocación

```
# Crear prompt de backend
"Usa prompt-builder en modo create para implementar gestión de clientes. CRUD, paginación y filtros."

# Crear backend y frontend por separado
"Usa prompt-builder para crear dos prompts del módulo de productos: uno de backend y uno de frontend."

# Revisar un prompt existente
"Usa prompt-builder en modo revise para revisar docs/superpowers/promts/2026-06-25-productos-backend.md. Agrega pruebas y paginación."

# Prompt rápido
"Usa prompt-builder en modo quick para crear un prompt que agregue la columna proveedor al listado de productos."

# Sobrescribir el archivo original
"Usa prompt-builder para actualizar el mismo archivo del prompt de clientes. Agrega endpoint para options y sobrescribe el archivo original."
```
