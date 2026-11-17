---
name: plane-tareas
description: Úsala siempre que crees, actualices o cierres una tarea (work item) en Plane, o cuando Jesús pida registrar tiempo u horas, poner fechas, asignar responsable o pasar una tarea a Done. Pone fecha de inicio (día en que empezó) y de fin (un día después), asigna a Jesús como responsable, y registra el tiempo en segundos con un script que verifica el resultado, porque el MCP de Plane lo hace mal.
---

# Tareas de Plane

Jesús lleva sus tareas en Plane (la instancia de `PLANE_BASE_URL`). Cada tarea que crees o cierres debe quedar con
**fechas, responsable y tiempo** correctos. Él revisa en Plane y se frustra cuando el tiempo sale en 0
o las fechas faltan, así que nada se da por hecho sin leerlo de vuelta.

## Reglas

1. **Fechas:** `start_date` = día en que se empezó el trabajo; `target_date` = **un día después**
   (si inicia hoy, cierra mañana). Si la tarea es de días atrás, toma el día de inicio de la bitácora,
   del commit o pregúntalo; no uses la fecha de hoy por defecto.
2. **Responsable:** Jesús (el dueño de la API key), salvo que él diga otra persona.
3. **Tiempo:** lo dice Jesús (p. ej. «ponle 30 min»). Si no lo dijo, **pregunta**; no lo inventes.
   La fecha del registro es el día de inicio de la tarea.
4. **Al cerrar:** estado del grupo `completed` (en la mayoría de proyectos se llama «Done»).

## Por qué hay un script

El MCP de Plane (`plane-mcp-server`) **no sirve para el tiempo**:

- `work_log create` falla con `logged_date: This field is required` (no expone ese campo).
- `work_log list` falla al leer `created_by` en cuanto hay registros.
- En este Plane, `duration` va en **segundos**, aunque la descripción del MCP diga minutos. Si
  mandas `30`, Plane guarda 30 segundos y la pantalla muestra 0.

Por eso el tiempo (y, si quieres, todo el cierre) se hace con `scripts/plane.py`, que recibe minutos,
convierte a segundos, no duplica registros y al final imprime cómo quedó la tarea.

## Cómo usarlo

El script lee las credenciales del MCP en `~/.claude.json` (nunca las imprimas):

```bash
S=~/.claude/skills/plane-tareas/scripts/plane.py

python3 $S ver PREMIOS-18                       # estado, fechas, responsable y tiempo
python3 $S cerrar PREMIOS-18 2026-11-06 30 --desc "Qué se hizo"   # Done + fechas + responsable + 30 min
python3 $S fechas PREMIOS-18 2026-11-06         # solo fechas (y responsable si falta)
python3 $S tiempo PREMIOS-18 30 --fecha 2026-11-06 --desc "…"     # solo tiempo
```

- Crear la tarea sí puede hacerse con el MCP (`workitem create`), pero pasando `start_date`,
  `target_date` y `assignees` desde el principio; luego el tiempo con el script.
- Si el proyecto tiene el registro de tiempo apagado, el script lo prende y lo avisa.
- Si un registro quedó mal (por ejemplo `30` en vez de `1800`), corrígelo con un `PATCH` a
  `.../work-items/<id>/worklogs/<log_id>/` con `{"duration": <segundos>}`, no crees otro encima.

## Al terminar

Muestra a Jesús la salida de `ver` (estado, fechas, responsable y minutos) en una tabla corta. Si algo
no cuadra, dilo; no digas «listo» sin haberlo leído de vuelta.
