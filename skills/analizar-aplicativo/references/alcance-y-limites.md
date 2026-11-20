# ¿La construcción alcanza para lo que se quiere lograr?

Pone frente a frente **lo que el aplicativo quiere lograr** y **cómo está construido**, y dice hasta dónde llega.
Es la sección que más ayuda a Jesús a opinar.

## La tabla

| Lo que quiere lograr | Cómo está construido | Límite | Cuándo se llega | Qué haría falta | Veredicto |
|---|---|---|---|---|---|

- **Lo que quiere lograr:** objetivos del negocio, en sus palabras (de los documentos, o deducidos del producto).
  Incluye los de escala («300 asesores a la vez»), los de producto («cada cliente arma su lógica») y los de
  operación («que nada se pierda si la IA falla»).
- **Cómo está construido:** la decisión técnica que lo sostiene, con su marca.
- **Límite:** qué deja de funcionar o se vuelve caro, y por qué.
- **Cuándo se llega:** en números si se puede (usuarios, clientes, filas, trabajos por segundo). Si no hay forma de
  estimarlo, «sin medir» y por confirmar.
- **Qué haría falta:** el siguiente paso y su costo aproximado (bajo, medio, alto), no una solución completa.
- **Veredicto:**
  - `<span class="veredicto sostiene">Lo sostiene</span>`: alcanza con margen para lo previsto.
  - `<span class="veredicto limite">Con límite</span>`: alcanza ahora y hay un punto conocido donde deja de alcanzar.
  - `<span class="veredicto frena">Lo frena</span>`: la construcción va en contra del objetivo hoy.

## Ejemplo (ARMEGA, cola de trabajos)

| Lo que quiere lograr | Cómo está construido | Límite | Cuándo se llega | Qué haría falta | Veredicto |
|---|---|---|---|---|---|
| Trabajos largos sin colgar la app (transcribir, cargas, IA) | Cola pg-boss dentro de la misma PostgreSQL | La cola comparte la base con las ventas; con miles de trabajos por segundo compite | Muy lejos del arranque (~300 asesores) | Mover la cola a un servicio administrado; solo cambia `@arm/db/jobs` (costo bajo) | Lo sostiene |

## Cómo encontrar los límites

Mira estos lugares típicos: una sola base para todo, tareas programadas con `setInterval` o cron dentro de la app,
consultas sin paginar o sin índice, archivos guardados en el disco del servidor, sesiones en memoria, integraciones
directas sin reintento, lógica de negocio fija en el código cuando el negocio pide configurarla, un solo proveedor sin
plan si falla, permisos solo en la pantalla y no en el servidor.

## Dónde va

- **Mapa:** los 4 a 8 objetivos principales.
- **Profundizar:** solo los de la pieza o el tema.
- **Comparar:** una tabla por cada aplicativo, con las mismas filas para que se puedan comparar.
