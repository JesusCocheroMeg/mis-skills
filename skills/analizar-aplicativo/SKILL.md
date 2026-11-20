---
name: analizar-aplicativo
description: >-
  Analiza un aplicativo o proyecto de software (propio o ajeno) y le arma a Jesús una presentación HTML con
  diagramas que le explica el negocio (qué resuelve, para quién, cómo y por qué) y lo técnico (piezas, por qué cada
  tecnología, alternativas, seguridad, riesgos) unidos, si la construcción alcanza para lo que se quiere lograr y sus
  límites, qué preguntar y decidir, y los conceptos que aún no conoce. Tres modos: mapa («analiza este aplicativo /
  proyecto / repo», «hazme el mapa de crm-conex», «actualiza el mapa»), profundizar («profundiza en el worker / en la
  seguridad / en Ventas», «cómo funciona por dentro X», «por qué usa Y», «aguanta 3 clientes como CXD?») y comparar
  («compara Ventas de crm-conex con ARMEGA», «X frente a Y»). Es para que Jesús entienda, opine y decida; no para
  documentos que se envían a otros (eso es documentos-para-compartir) ni para revisar contenido de redes (eso es
  revision-tecnica).
---

# Analizar un aplicativo

Jesús quiere **entender un aplicativo para opinar y decidir con criterio, y aprender lo que todavía no sabe**. Esta
skill lee el aplicativo (el código, los datos, la configuración y los documentos) y le arma una presentación HTML que
une dos capas:

- **Negocio:** qué problema resuelve, para quién, cómo lo resuelve y por qué así.
- **Técnica:** piezas y cómo se conectan, por qué cada tecnología y qué alternativas había, seguridad y riesgos.
- **El hilo:** cada pieza técnica dice qué parte del negocio sostiene.

Y siempre responde: **¿la construcción alcanza para lo que se quiere lograr?** y **qué mirar y qué preguntar**.

## 1. Elegir el modo

| Pide | Modo | Guía |
|---|---|---|
| «Analiza…», «hazme el mapa de…», «actualiza el mapa» | **Mapa**: el aplicativo completo | `references/mapa.md` |
| «Profundiza en…», «cómo funciona por dentro…», «por qué usa…», «aguanta…» | **Profundizar**: un tema | `references/profundizar.md` |
| «Compara X con Y», «X frente a Y» | **Comparar**: lado a lado | `references/comparar.md` |

Si no es claro, escoge el más probable y dilo en una línea.

## 2. Ubicar el aplicativo y su proyecto

1. **La ruta del repo o repos.** Si Jesús da un nombre, búscalo en `~/Desktop/Desarrollo/` (y subcarpetas como
   `Aplicativos git/`). Si da un enlace de GitHub, clónalo en el scratchpad de la sesión (nunca en sus carpetas), con
   `--depth 50`. Si hay varias coincidencias, pregunta cuál.
2. **¿Pertenece a un proyecto con centro?** Un centro es la carpeta privada del proyecto (por ejemplo `ARM/arm-centro`
   con `explicaciones/`, `decisiones/`, `preguntas.md`, `pendientes.md`). Un aplicativo ajeno ligado a un proyecto
   (crm-conex → ARM, porque ARM lo reemplaza) **pertenece a ese proyecto**. Si dudas, pregunta.
3. **¿Es propio o ajeno?** Propio: Jesús lo construye y hay documentos de diseño. Ajeno: lo recibió. Cambia cómo se
   lee el negocio (`references/negocio.md`).
4. **¿Ya hay presentaciones?** Busca `mapa-<aplicativo>.html` y otras del mismo aplicativo en la ubicación de abajo.

### Dónde se guarda

| Caso | Carpeta |
|---|---|
| Pertenece a un proyecto con centro | `<centro>/explicaciones/` y su fila en `<centro>/explicaciones/README.md` (qué explica · estado «Solo análisis») |
| No pertenece a ninguno | `~/Desktop/Desarrollo/Analisis/<aplicativo>/` con un `README.md` de índice |

**Nunca dentro del repo analizado.** Antes de escribir riesgos de seguridad en un centro, comprueba que su repo es
privado (`references/seguridad.md`).

## 3. Leer

- Proyecto chico: lee tú. Proyecto grande (más de ~300 archivos de código, varios repos o monorepo con varias apps):
  reparte entre tres lectores en paralelo (`references/lectores.md`).
- Orden: documentos y centro (si es propio) → estructura y dependencias → modelo de datos → rutas y pantallas →
  procesos de fondo e integraciones → configuración y despliegue → pruebas.
- Anota el commit base: `git -C <repo> rev-parse --short HEAD` y la rama.
- Anota `git -C <repo> status --porcelain` al empezar; al terminar debe ser igual. **Solo lectura**: no instales
  dependencias, no corras migraciones ni el aplicativo, no edites nada.

## 4. Armar la presentación

- Parte de `assets/plantilla.html`: reemplaza `{{TITULO}}` (nombre corto de 2 a 4 palabras) y `{{CONTENIDO}}` con las
  secciones `<section class="slide">` que pide la guía del modo.
- Guías de método que aplican en los tres modos:
  - `references/marcas.md`: toda afirmación que importe lleva **comprobado** (con ruta), **deducido** o **por
    confirmar**.
  - `references/negocio.md`: leer o deducir el negocio y el hilo negocio ↔ técnica.
  - `references/alcance-y-limites.md`: la tabla de objetivos frente a construcción, con veredicto.
  - `references/seguridad.md`: qué revisar y qué no escribir nunca.
  - `references/diagramas.md`: tipos de diagrama y esqueleto SVG.
- **Escribe para Jesús:** español claro, con tildes, frases cortas, términos técnicos con su nombre original y
  explicados la primera vez. Cada pieza o tema importante cierra con «qué mirar y qué preguntar». Las decisiones
  abiertas van con una recomendación y su porqué.

### Aprender sin repetir

El registro está en `~/Desktop/Desarrollo/Analisis/conceptos-aprendidos.md` (tabla: concepto · explicación corta ·
dónde se enseñó · fecha).

- Antes de escribir «Para aprender», léelo. Los conceptos que ya están se nombran en una línea con su enlace; solo
  los nuevos se enseñan completos (qué es, ejemplo de la vida diaria, por qué importa aquí).
- Al terminar, agrega los conceptos nuevos al registro, con la ruta de la presentación.
- Si el archivo no existe, créalo con el encabezado de la tabla.

## 5. Verificar y entregar

1. `python3 -I <carpeta de esta skill>/scripts/verificar.py <presentación.html> --repo <ruta del repo>` debe decir
   `OK` (en comparar, córrelo una vez por cada repo). Si falla, corrige y repite.
2. Comprueba que `git status --porcelain` del repo analizado no cambió.
3. Guarda, agrega su fila al índice de la carpeta y, si es profundizar o comparar, su enlace en la sección 9 del mapa.
4. **Si pertenece a un proyecto con centro:** las preguntas **por confirmar** que necesitan a otra persona van a
   `<centro>/preguntas.md`, y la presentación se anota en `<centro>/pendientes.md` › «Por revisar a mano», siguiendo
   el formato que ya tengan esos archivos. Sin centro, se quedan en la presentación.
5. Ábrela con `open <ruta>`.
6. Responde corto: la ruta completa, lo más importante que encontró (3 a 5 puntos, incluidos los veredictos «lo
   frena» y los riesgos serios), cuántas afirmaciones quedaron por confirmar y los temas que sugiere profundizar.

## Reglas duras

- Solo lectura sobre el aplicativo analizado; nunca escribir dentro de su repo.
- Nunca copiar el valor de un secreto, contraseña, llave, token ni dato personal real; nunca un paso a paso para
  explotar un riesgo.
- No sonar seguro cuando se adivina: sin marca no hay afirmación importante.
- No es auditoría formal ni pentest; no corrige el aplicativo, no abre PR, no crea tareas en gestores, no registra
  decisiones del proyecto.
- Para compartir con otra persona, se pasa a `documentos-para-compartir`, sin los hallazgos sensibles.
