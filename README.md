# mis-skills

Colección de skills personalizadas para Claude Code.

## Skills

| Skill | Para qué sirve |
|-------|----------------|
| [centro-de-proyecto](skills/centro-de-proyecto/SKILL.md) | Crear, adoptar o abrir el repo centro de un proyecto: estado multi-repo, fuentes del cliente, delegación a agentes, commits/PR en repos ajenos. |
| [documentos-para-compartir](skills/documentos-para-compartir/SKILL.md) | Propuestas, informes, resúmenes, briefs y benchmarks para gente no técnica, con el diseño de cada proyecto, exportados a web, HTML y PDF (láminas 1280×720); también README de repositorios. |
| [desarrollo-modular-vertical](skills/desarrollo-modular-vertical/SKILL.md) | Desarrollo por módulos, verticales y versiones: iniciar, auditar, planificar, ajustar y cerrar. |
| [prompt-builder](skills/prompt-builder/SKILL.md) | Crear o revisar prompts de implementación para features, módulos o endpoints (sin implementar). |
| [reporte-daily](skills/reporte-daily/SKILL.md) | Reporte diario del daily (Hoy estoy en / Me frena / Necesito a), resumido y en lenguaje no técnico. ⚠️ Vive en claude.ai (ver abajo). |

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

> **Excepción: `reporte-daily`.** Está creada en claude.ai y se sincroniza sola en
> `~/.claude/skills/synced/`, así que **no** se enlaza (quedaría duplicada). Aquí se guarda
> como copia: si la editas, actualízala en claude.ai (Settings → Capabilities → Skills) y copia
> el cambio a este repo.

## Agregar una skill nueva

1. Crear `skills/<nombre>/SKILL.md`.
2. Añadirla a la tabla de arriba.
3. Enlazarla en `~/.claude/skills/` (ver Instalación).
4. Commit: `feat(<nombre>): add skill`.
