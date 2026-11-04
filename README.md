# mis-skills

Colección de skills personalizadas para Claude Code.

## Skills

| Skill | Para qué sirve |
|-------|----------------|
| [centro-de-proyecto](skills/centro-de-proyecto/SKILL.md) | Crear, adoptar o abrir el repo centro de un proyecto: estado multi-repo, fuentes del cliente, delegación a agentes, commits/PR en repos ajenos. |
| [desarrollo-modular-vertical](skills/desarrollo-modular-vertical/SKILL.md) | Desarrollo por módulos, verticales y versiones: iniciar, auditar, planificar, ajustar y cerrar. |
| [prompt-builder](skills/prompt-builder/SKILL.md) | Crear o revisar prompts de implementación para features, módulos o endpoints (sin implementar). |
| [reporte-daily](skills/reporte-daily/SKILL.md) | Reporte diario del daily (Hoy estoy en / Me frena / Necesito a), resumido y en lenguaje no técnico. |

## Estructura

```
skills/
  <nombre-skill>/
    SKILL.md          # definición de la skill (frontmatter name + description)
    references/       # material de apoyo opcional
```

## Instalación

Claude Code carga las skills desde `~/.claude/skills/`. Para usar este repo como fuente de verdad:

```bash
for s in skills/*/; do
  ln -sfn "$PWD/$s" ~/.claude/skills/$(basename "$s")
done
```

> **Nota: `reporte-daily`.** También existe en claude.ai y se sincroniza en
> `~/.claude/skills/synced/`, pero ahí no se carga en Claude Code, así que se enlaza como las
> demás. Si la editas, copia el cambio a claude.ai (Settings → Capabilities → Skills).

## Agregar una skill nueva

1. Crear `skills/<nombre>/SKILL.md`.
2. Añadirla a la tabla de arriba.
3. Enlazarla en `~/.claude/skills/` (ver Instalación).
4. Commit: `feat(<nombre>): add skill`.
