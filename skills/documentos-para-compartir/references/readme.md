# README de un repositorio

Un README no es una presentación: es un archivo `README.md` en la raíz del repositorio, que GitHub
(o GitLab) muestra en la portada del proyecto. No lleva láminas, `diseno.md` ni exportación. Lo que sí
aplica de la skill es la redacción: tiene que entenderlo alguien que llega sin contexto.

## Dos lectores, en ese orden

1. **Alguien no técnico** (cliente, jefe, alguien que evalúa el proyecto) lee solo el principio:
   qué es, para quién, qué problema resuelve y cómo se ve. Sin comandos ni jerga.
2. **Quien lo va a instalar o tocar** sigue leyendo: requisitos, instalación, uso, configuración.

## Estructura

```markdown
# Nombre del proyecto

Una frase: qué hace y para quién («Agenda citas de un consultorio por WhatsApp, sin llamar»).

![Captura de la pantalla principal](docs/captura.png)   ← si hay interfaz y existe la imagen

## Qué hace
3–5 viñetas de lo que puede hacer una persona con la aplicación, en lenguaje de usuario.

## Estado
Qué funciona hoy y qué falta (una tabla corta o viñetas). Sin promesas con fecha si no están decididas.

## Cómo empezar
Requisitos (con versión) → instalar → configurar → ejecutar. Cada paso, un bloque de código
que se pueda copiar y pegar tal cual.

## Configuración
Tabla de variables de entorno: nombre · para qué sirve · ejemplo. Nunca valores reales.

## Cómo está organizado
Las carpetas principales, una línea cada una. Un diagrama ```mermaid solo si aclara algo
(GitHub lo dibuja).

## Pruebas, despliegue, contribuir
Solo las secciones que el proyecto realmente tenga.
```

Quita las secciones que no apliquen; un README corto y cierto es mejor que uno largo de plantilla.

## Verdad

- **Lee el código antes de escribir**: `package.json`, `pyproject.toml`, `Makefile`, `docker-compose`,
  `.env.example`, la carpeta de rutas o pantallas. Cada función que menciones tiene que existir.
- **Prueba los comandos** que pongas en «Cómo empezar» cuando sea seguro (instalar, compilar,
  pruebas). Si no puedes probar uno (necesita credenciales, toca producción), márcalo con
  `<!-- por confirmar -->` y dilo al entregar.
- Revisa que los enlaces relativos (`docs/…`, imágenes) apunten a archivos que existen.
- Sin secretos, tokens, URLs internas ni datos de clientes. Si el repo es público o del cliente,
  revisa que tampoco aparezcan en los ejemplos.
- Si ya hay un README, mejóralo conservando lo que esté bien y avisa de lo que quitaste.

## Entregar

- Muestra el diff, no el archivo entero, si ya existía.
- El commit sigue las reglas del repo (Conventional Commits: `docs: …`). Si el repo es del cliente o
  del equipo, el commit y el PR van con la skill `centro-de-proyecto`.
- Si además piden una versión para enviar (al cliente, a gerencia), esa sí se hace como documento
  de láminas con el resto de la skill, partiendo del mismo contenido.
