#!/usr/bin/env python3
"""Tareas de Plane: fechas, responsable y tiempo, bien puestos y verificados.

Uso:
  plane.py ver     PROJ-N
  plane.py tiempo  PROJ-N MINUTOS [--fecha AAAA-MM-DD] [--desc TEXTO] [--forzar]
  plane.py fechas  PROJ-N INICIO          # fin = INICIO + 1 día
  plane.py cerrar  PROJ-N INICIO MINUTOS [--desc TEXTO]

Reglas que aplica (pedidas por Jesús):
  - Fecha de inicio = día en que se empezó; fecha de fin = un día después.
  - Responsable: el dueño de la API key (Jesús) si la tarea no tiene a nadie.
  - Tiempo: en Plane `duration` va en SEGUNDOS.
    El script recibe MINUTOS y convierte (30 min -> 1800). Antes de crear, revisa que
    no exista ya un registro igual; después, lo vuelve a leer y lo muestra.

Credenciales: ~/.claude.json -> mcpServers.plane.env (PLANE_BASE_URL, PLANE_WORKSPACE_SLUG,
PLANE_API_KEY), o variables de entorno con esos nombres. La clave nunca se imprime.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


def credenciales() -> tuple[str, str, str]:
    env = {k: os.environ.get(k) for k in ("PLANE_BASE_URL", "PLANE_WORKSPACE_SLUG", "PLANE_API_KEY")}
    if not all(env.values()):
        try:
            cfg = json.loads((Path.home() / ".claude.json").read_text())
            env = {**cfg["mcpServers"]["plane"]["env"], **{k: v for k, v in env.items() if v}}
        except (OSError, KeyError, json.JSONDecodeError):
            sys.exit("No encuentro las credenciales de Plane (~/.claude.json -> mcpServers.plane.env).")
    return env["PLANE_BASE_URL"].rstrip("/"), env["PLANE_WORKSPACE_SLUG"], env["PLANE_API_KEY"]


BASE, WS, KEY = credenciales()


def api(metodo: str, ruta: str, cuerpo: dict | None = None):
    url = f"{BASE}/api/v1{ruta}"
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(url, datos, {"X-API-Key": KEY, "Content-Type": "application/json"}, method=metodo)
    try:
        with urllib.request.urlopen(req) as r:
            texto = r.read().decode()
            return json.loads(texto) if texto else None
    except urllib.error.HTTPError as e:
        sys.exit(f"Plane respondió {e.code} en {metodo} {ruta}: {e.read().decode()[:300]}")


def tarea(ident: str) -> dict:
    return api("GET", f"/workspaces/{WS}/work-items/{ident.upper()}/")


def ruta_tarea(t: dict) -> str:
    return f"/workspaces/{WS}/projects/{t['project']}/work-items/{t['id']}"


def registros(t: dict) -> list[dict]:
    return api("GET", ruta_tarea(t) + "/worklogs/") or []


def fecha(texto: str) -> dt.date:
    try:
        return dt.date.fromisoformat(texto)
    except ValueError:
        sys.exit(f"Fecha inválida: {texto} (usa AAAA-MM-DD).")


def mostrar(ident: str) -> None:
    t = tarea(ident)
    estados = {s["id"]: s["name"] for s in api("GET", f"/workspaces/{WS}/projects/{t['project']}/states/")["results"]}
    miembros = {m["id"]: m.get("display_name") or m.get("email") for m in api("GET", f"/workspaces/{WS}/members/")}
    logs = registros(t)
    total = sum(w["duration"] for w in logs)
    print(f"{ident.upper()} · {t['name']}")
    print(f"  Estado:      {estados.get(t['state'], t['state'])}")
    print(f"  Inicio/fin:  {t.get('start_date') or '—'} → {t.get('target_date') or '—'}")
    print(f"  Responsable: {', '.join(miembros.get(a, a) for a in t.get('assignees') or []) or '— (sin responsable)'}")
    print(f"  Tiempo:      {total // 60} min en {len(logs)} registro(s)")
    for w in logs:
        print(f"    - {w['logged_date']}: {w['duration'] // 60} min ({w['duration']} s) {(w.get('description') or '')[:60]}")


def registrar_tiempo(ident: str, minutos: int, dia: dt.date, desc: str, forzar: bool) -> None:
    if minutos <= 0:
        sys.exit("Los minutos deben ser mayores que 0.")
    t = tarea(ident)
    segundos = minutos * 60
    igual = [w for w in registros(t) if w["duration"] == segundos and w["logged_date"] == dia.isoformat()]
    if igual and not forzar:
        print(f"Ya hay un registro de {minutos} min el {dia} en {ident.upper()}: no lo duplico (usa --forzar si es otro).")
    else:
        api("POST", ruta_tarea(t) + "/worklogs/", {"duration": segundos, "logged_date": dia.isoformat(), "description": desc})
    proyecto = api("GET", f"/workspaces/{WS}/projects/{t['project']}/")
    if not proyecto.get("is_time_tracking_enabled"):
        api("PATCH", f"/workspaces/{WS}/projects/{t['project']}/", {"is_time_tracking_enabled": True})
        print("Activé el registro de tiempo del proyecto (estaba apagado).")


def poner_fechas_y_responsable(ident: str, inicio: dt.date, cerrar: bool) -> None:
    t = tarea(ident)
    cambios: dict = {"start_date": inicio.isoformat(), "target_date": (inicio + dt.timedelta(days=1)).isoformat()}
    if not t.get("assignees"):
        cambios["assignees"] = [api("GET", "/users/me/")["id"]]
    if cerrar:
        estados = api("GET", f"/workspaces/{WS}/projects/{t['project']}/states/")["results"]
        hecho = next((s for s in estados if s["group"] == "completed"), None)
        if not hecho:
            sys.exit("El proyecto no tiene un estado del grupo «completed».")
        cambios["state"] = hecho["id"]
    api("PATCH", ruta_tarea(t) + "/", cambios)


def main() -> None:
    p = argparse.ArgumentParser(description="Fechas, responsable y tiempo de tareas de Plane.")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("ver").add_argument("tarea")
    s = sub.add_parser("tiempo")
    s.add_argument("tarea")
    s.add_argument("minutos", type=int)
    s.add_argument("--fecha", default=dt.date.today().isoformat())
    s.add_argument("--desc", default="")
    s.add_argument("--forzar", action="store_true")
    s = sub.add_parser("fechas")
    s.add_argument("tarea")
    s.add_argument("inicio")
    s = sub.add_parser("cerrar")
    s.add_argument("tarea")
    s.add_argument("inicio")
    s.add_argument("minutos", type=int)
    s.add_argument("--desc", default="")
    a = p.parse_args()

    if a.cmd == "tiempo":
        registrar_tiempo(a.tarea, a.minutos, fecha(a.fecha), a.desc, a.forzar)
    elif a.cmd == "fechas":
        poner_fechas_y_responsable(a.tarea, fecha(a.inicio), cerrar=False)
    elif a.cmd == "cerrar":
        inicio = fecha(a.inicio)
        poner_fechas_y_responsable(a.tarea, inicio, cerrar=True)
        registrar_tiempo(a.tarea, a.minutos, inicio, a.desc, forzar=False)
    mostrar(a.tarea)  # siempre se verifica leyendo de vuelta


if __name__ == "__main__":
    main()
