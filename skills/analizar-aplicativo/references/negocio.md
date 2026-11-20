# Leer el negocio de un aplicativo

La capa de negocio responde: **qué problema resuelve, para quién, cómo lo resuelve y por qué así**. Es lo que da
sentido a la capa técnica: cada pieza técnica debe poder decir qué parte del negocio sostiene.

## Aplicativo propio (hay documentos)

1. **Busca lo escrito, en este orden:** centro del proyecto (README, bitácora, preguntas, pendientes, decisiones,
   `explicaciones/`), brief o visión, `docs/decisiones/` o ADR, documentos de módulos y verticales, README del repo,
   `CLAUDE.md`.
2. **Saca de ahí:** el problema y los dolores, quién lo usa (roles), los flujos principales, las decisiones y sus
   porqués, lo que está fuera del alcance.
3. **Crúzalo con el código.** Lo valioso es señalar donde **no coinciden**: una decisión que dice una cosa y un código
   que hace otra, un módulo documentado que no existe, código sin documento. Cada diferencia va como hallazgo, con
   las dos fuentes.
4. **No repitas los documentos:** resúmelos y enlázalos.

## Aplicativo ajeno (no hay documentos o son pocos)

Deduce el negocio de estas señales, de la más fuerte a la más débil:

| Señal | Qué dice | Dónde mirar |
|---|---|---|
| Modelo de datos | Las cosas que importan al negocio y cómo se relacionan | Esquema (Prisma, migraciones, modelos del ORM, SQL), colecciones |
| Estados y transiciones | El proceso del negocio (venta: nueva → validada → instalada) | Enums, columnas `status`/`estado`, tablas de estados, switch en controladores |
| Roles y permisos | Quién hace qué | Middleware de permisos, tablas de roles, condiciones en el front |
| Rutas y pantallas | Lo que la gente hace en el día | Router del front, endpoints, menús |
| Textos de la interfaz | El vocabulario del negocio | Etiquetas, mensajes, traducciones |
| Integraciones | Con quién habla y por qué | Llamadas HTTP, SDK, colas, tareas programadas |
| Reportes y exportes | Qué se mide | Consultas grandes, generación de Excel o PDF |

**Cuenta los flujos como los vive la persona**: «El asesor registra la venta, back office la valida, y luego…», no
«el endpoint POST /sales inserta en la tabla».

Todo lo deducido lleva su marca (ver `marcas.md`), y las dudas que solo el negocio resuelve van como
**por confirmar**, escritas como preguntas.

## El hilo negocio ↔ técnica

Para cada pieza técnica, escribe una línea: **«existe porque el negocio necesita…»**. Si no encuentras para qué
existe una pieza, eso también es un hallazgo (código muerto, algo a medio construir o una necesidad que nadie
escribió).
