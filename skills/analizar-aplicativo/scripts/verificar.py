#!/usr/bin/env python3
"""Verifica una presentación de analizar-aplicativo antes de entregarla.

Uso: python3 -I verificar.py <presentacion.html> [--repo <ruta del repo analizado>]

Sale 0 si pasa. Sale 1 y lista las fallas si:
- no tiene <title>;
- algún <svg> no tiene role="img" y aria-label;
- carga un script externo (<script src=...>);
- no tiene ninguna marca de fuente (comprobado, deducido, por confirmar);
- aparece una cadena con forma de llave (sk-..., AKIA..., -----BEGIN ..., ghp_..., xox?-...);
- con --repo: aparece el valor de alguna variable de los archivos .env* del repo (valores de 8+ caracteres).
Nunca imprime el valor de un secreto: solo dice qué variable y de qué archivo.
"""
from __future__ import annotations

import os
import re
import sys

KEY_PATTERNS = [
    ("llave con prefijo sk-", r"\bsk-[A-Za-z0-9_-]{16,}"),
    ("llave de AWS", r"\bAKIA[0-9A-Z]{16}\b"),
    ("llave privada", r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    ("token de GitHub", r"\bgh[pousr]_[A-Za-z0-9]{20,}"),
    ("token de Slack", r"\bxox[abprs]-[A-Za-z0-9-]{10,}"),
]
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", ".next", "dist", "build", "vendor", ".turbo"}
PLACEHOLDER = re.compile(r"^(changeme|example|your[_-].*|xxx+|\*+|<.*>|\$\{.*\})$", re.I)


def env_values(repo: str):
    """Yields (archivo, variable, valor) de los .env* del repo, sin entrar a carpetas de dependencias."""
    for root, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if not name.startswith(".env"):
                continue
            path = os.path.join(root, name)
            try:
                with open(path, encoding="utf-8", errors="ignore") as fh:
                    lines = fh.readlines()
            except OSError:
                continue
            for line in lines:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                value = value.strip().strip('"').strip("'")
                if len(value) >= 8 and not PLACEHOLDER.match(value):
                    yield os.path.relpath(path, repo), key.replace("export ", "").strip(), value


def check(html: str, repo: str | None) -> list[str]:
    fails = []
    if not re.search(r"<title>\s*[^<\s][^<]*</title>", html, re.I):
        fails.append("Falta <title> con texto.")
    for i, svg in enumerate(re.findall(r"<svg\b[^>]*>", html, re.I), 1):
        if 'role="img"' not in svg or "aria-label=" not in svg:
            fails.append(f'El diagrama SVG n.º {i} no tiene role="img" y aria-label.')
    if re.search(r"<script\b[^>]*\bsrc\s*=", html, re.I):
        fails.append("Carga un script externo; la presentación debe ser autocontenida.")
    if not re.search(r'class="marca (comprobado|deducido|confirmar)"', html):
        fails.append("No tiene ninguna marca de fuente (comprobado, deducido o por confirmar).")
    for label, pattern in KEY_PATTERNS:
        if re.search(pattern, html):
            fails.append(f"Aparece algo con forma de {label}.")
    if repo:
        for path, key, value in env_values(repo):
            if value in html:
                fails.append(f"Aparece el valor de {key} de {path}.")
    return fails


def main(argv: list[str]) -> int:
    if not argv or argv[0] in {"-h", "--help"}:
        print(__doc__)
        return 0 if argv else 1
    html_path, repo = argv[0], None
    if "--repo" in argv:
        i = argv.index("--repo")
        if i + 1 >= len(argv):
            print("Falta la ruta después de --repo.")
            return 1
        repo = argv[i + 1]
    try:
        with open(html_path, encoding="utf-8") as fh:
            html = fh.read()
    except OSError as e:
        print(f"No se pudo leer {html_path}: {e}")
        return 1
    fails = check(html, repo)
    if fails:
        print("FALLA")
        for f in fails:
            print(f"- {f}")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
