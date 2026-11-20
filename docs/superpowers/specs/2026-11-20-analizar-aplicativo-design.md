# Diseño · skill `analizar-aplicativo`

- **Fecha:** 2026-11-20
- **Pide:** Jesús
- **Estado:** aprobado por Jesús el 2026-11-20 (con el modo comparar)

## Intención

Jesús quiere **entender un aplicativo para opinar y decidir con criterio, y aprender lo que todavía no sabe**.
Hoy lo consigue pidiendo láminas pieza por pieza (ejemplo: la del worker de ARMEGA del 2026-11-20, en
`ARM/arm-centro/explicaciones/2026-11-20-el-worker-de-armega.html`). La skill hace eso de forma ordenada para un
aplicativo entero, sea suyo (ARMEGA) o ajeno (crm-conex, el repo de un cliente).

El resultado es una **presentación HTML con diagramas, para él**, que cubre dos capas unidas por un hilo:

- **Negocio:** qué problema resuelve, para quién, cómo lo resuelve (flujos como los vive quien lo usa) y por qué
  así.
- **Técnica:** piezas y cómo se conectan, por qué cada pieza y cada tecnología, alternativas, seguridad, riesgos y
  conceptos para aprender.
- **El hilo:** cada pieza técnica dice qué parte del negocio sostiene («el worker existe porque hay que bloquear a
  quien lleva 60 días sin entrar, aunque no intente entrar»).

## Objetivos

1. **Modo mapa** («analiza este aplicativo»): una presentación del aplicativo completo.
2. **Modo profundizar** («profundiza en el worker / en la seguridad / en Ventas»): una presentación por tema,
   enlazada desde el mapa.
3. **Modo comparar** («compara Ventas de crm-conex con Ventas de ARMEGA»; agregado el 2026-11-20): pone lado a lado
   dos aplicativos, o el mismo tema en dos aplicativos: qué resuelve cada uno, cómo, qué hace mejor cada uno, qué
   del primero no debe perderse si el segundo lo reemplaza, y la tabla de alcance y límites de ambos. Usa los
   mapas de los dos si existen.
4. **Análisis de alcance y límites:** para cada objetivo del negocio, si la construcción lo **sostiene**, lo
   **sostiene con límite** o lo **frena**; en qué punto se llega al límite (usuarios, clientes, datos) y qué haría
   falta para superarlo. Los principales en el mapa; los de cada pieza al profundizar.
5. **Para opinar y decidir:** cada pieza cierra con «qué mirar y qué preguntar» y con un juicio (qué está bien,
   qué es riesgo, qué está abierto y qué recomienda la skill, con su porqué).
6. **Honestidad sobre la fuente:** toda afirmación lleva una marca: **comprobado** (lo vio en código, esquema,
   configuración o documento, con la ruta), **deducido** (lo infiere) o **por confirmar** (pregunta para alguien
   que conozca el aplicativo).
7. **Aprender sin repetir:** un registro de conceptos ya explicados. Un concepto nuevo se enseña completo (qué es,
   ejemplo simple, por qué importa aquí); uno ya registrado se nombra con una línea y su enlace a donde se
   explicó.
8. **Funciona en los dos casos:**
   - **Aplicativo propio:** lee primero lo escrito (brief, decisiones, verticales, centro del proyecto), lo cruza
     con el código y señala dónde no coinciden.
   - **Aplicativo ajeno:** deduce el negocio desde el código, la base de datos, las pantallas y los textos, y
     marca lo deducido.

## No objetivos

- No es para enviar a otros. Si Jesús quiere compartir una versión, se le pasa a `documentos-para-compartir`, sin
  los hallazgos sensibles.
- No es una auditoría de seguridad formal ni un pentest: señala riesgos visibles en el código y la configuración.
- No corrige el aplicativo, no abre PR, no crea tareas, no registra decisiones en el proyecto.
- No critica contenido para redes (eso es `revision-tecnica`).

## Anti-objetivos (fallaría aunque funcione)

- Que suene igual de segura cuando adivina que cuando comprobó.
- Que sea un inventario de herramientas sin el porqué ni la relación con el negocio.
- Que repita cada vez los mismos conceptos básicos.
- Que copie secretos, contraseñas, llaves o datos personales reales a la presentación.
- Que escriba dentro de un repo ajeno.

## Restricciones

- Español con tildes; términos técnicos e identificadores en su forma original.
- HTML local que se abre con doble clic, sin servidor. Estilo de las láminas de ARM (tarjetas, paleta azul de la
  maqueta, modo claro y oscuro, legible en el celular). Diagramas en SVG dentro del HTML, sin librerías externas.
- Solo lectura sobre el aplicativo analizado.
- Las skills viven en `mis-skills/skills/<nombre>/` y se enlazan en `~/.claude/skills/` (ver README del repo).

## Enfoques considerados

| Enfoque | A favor | En contra |
|---|---|---|
| **A · Skill nueva `analizar-aplicativo`** (elegida) | Sirve para propios y ajenos; no se cruza con otras skills; se apoya en ellas (lee el centro si existe, pasa a `documentos-para-compartir` para compartir) | La más grande de construir |
| B · Modo de `documentos-para-compartir` | Reusa diseño y exporte a PDF | Esa skill es para otros; mezcla tono, profundidad y hallazgos sensibles |
| C · Parte de `centro-de-proyecto` | Ya conoce fuentes y decisiones | Deja por fuera el repo ajeno suelto, que Jesús pidió |

Jesús eligió **A** el 2026-11-20. También eligió el esquema **mapa y luego profundizar** frente a «todo en una»
(queda superficial o muy larga) y «solo por tema» (pierde cómo encaja todo).

## Cómo funciona

### Flujo del modo mapa

1. **Ubicar el aplicativo:** ruta del repo o repos, y si hay centro de proyecto o documentos del negocio.
2. **Leer:** estructura, dependencias, esquema de datos, rutas y pantallas, configuración, procesos de fondo,
   pruebas, documentos. En proyectos grandes reparte la lectura entre agentes en paralelo (negocio, piezas y
   datos, seguridad) que devuelven hallazgos con su marca y su ruta; la skill junta y resuelve contradicciones.
3. **Armar el mapa** con estas secciones:
   1. El aplicativo en un minuto (problema, para quién, qué hace).
   2. Cómo lo vive quien lo usa: flujos principales (diagrama).
   3. Las piezas y cómo se conectan (diagrama de arquitectura), cada una con qué parte del negocio sostiene.
   4. Tecnologías: qué, para qué, por qué y alternativas (si es propio, desde las decisiones; si es ajeno,
      deducido).
   5. Datos: qué guarda y cómo separa (empresas, usuarios).
   6. Seguridad: cómo entra la gente, permisos, secretos, datos sensibles; riesgos visibles.
   7. ¿La construcción alcanza para lo que se quiere lograr? (tabla de objetivos, cómo está construido, límite,
      qué haría falta, y el veredicto sostiene / con límite / frena).
   8. Lo que conviene decidir o preguntar (con la recomendación).
   9. Temas para profundizar (enlaces a las presentaciones ya hechas y a las sugeridas).
   10. Para aprender (solo conceptos nuevos; los ya vistos, en una línea con enlace).
   11. Fuentes y marcas (qué se leyó; cuántas afirmaciones comprobadas, deducidas y por confirmar).
4. **Guardar, actualizar el registro de conceptos, indexar y abrir** (ver «Dónde queda»).

### Flujo del modo profundizar

Lee el mapa existente (si no hay, lo avisa y ofrece hacerlo primero, o profundiza igual con un contexto mínimo).
Explica el tema con la forma de la lámina del worker: la idea con una analogía, cómo trabaja paso a paso
(diagrama), herramientas y por qué, dónde vive en el código, qué del negocio sostiene, alternativas, seguridad,
alcance y límites de esa pieza, qué mirar y qué preguntar, para aprender. Agrega su enlace en la sección 9 del
mapa.

### Flujo del modo comparar

Lee o arma un contexto mínimo de cada lado (usa sus mapas si existen). Secciones: qué resuelve cada uno, cómo lo
resuelve (flujos lado a lado, diagrama), piezas y tecnologías lado a lado, alcance y límites de cada uno, qué hace
mejor cada uno, qué no debe perderse en un reemplazo (lista para verificar), qué mirar y qué preguntar, para
aprender. Se guarda como `AAAA-MM-DD-comparar-<a>-<b>[-<tema>].html` y se enlaza desde los mapas de ambos.

### Dónde queda (decisión de Claude, Jesús puede cambiarla)

- **Si el aplicativo tiene centro de proyecto:** en el `explicaciones/` del centro, con nombre
  `AAAA-MM-DD-mapa-<aplicativo>.html` o `AAAA-MM-DD-<aplicativo>-<tema>.html`, y su fila en el índice de esa
  carpeta (en ARM: `arm-centro/explicaciones/README.md`).
- **Si no tiene:** en `~/Desktop/Desarrollo/Analisis/<aplicativo>/`, con un `README.md` de índice. Nunca dentro del
  repo analizado.
- **Registro de conceptos:** un solo archivo personal para todos los aplicativos,
  `~/Desktop/Desarrollo/Analisis/conceptos-aprendidos.md`: concepto, explicación corta y enlace a la presentación
  donde se enseñó. No va en `mis-skills` porque es dato personal, no parte de la skill.

### Decisiones de Claude tras la revisión (Jesús puede cambiarlas)

1. **Frontera con `centro-de-proyecto`:** «analiza», «profundiza» y «cómo funciona / cómo está hecho X del
   aplicativo» son de esta skill. El centro sigue con las láminas para decidir algo del proyecto. Se agrega una
   línea a la descripción de `centro-de-proyecto` que remite a esta skill, y las láminas del centro también anotan
   sus conceptos en el registro.
2. **Ubicación por proyecto, no por repo:** un aplicativo ajeno ligado a un proyecto con centro (crm-conex → ARM)
   va al `explicaciones/` de ese centro. Solo lo que no pertenece a ningún proyecto va a
   `~/Desktop/Desarrollo/Analisis/<aplicativo>/`.
3. **Hallazgos sensibles:** `arm-centro` es un repo privado en GitHub (verificado el 2026-11-20), así que los
   riesgos se escriben ahí. Se describe el riesgo y su ubicación, nunca el valor del secreto ni un paso a paso para
   explotarlo. Si el centro de otro proyecto fuera público, la sección de seguridad va a
   `~/Desktop/Desarrollo/Analisis/` y el mapa la enlaza.
4. **Preguntas y pendientes:** en un proyecto con centro, lo «por confirmar» que necesita a otra persona va a su
   `preguntas.md`, y cada presentación nueva se anota en `pendientes.md` › «Por revisar a mano», como ya se hace en
   ARM. Sin centro, se queda en la presentación.
5. **Un mapa por aplicativo, que se actualiza:** se mantiene el mismo archivo (`mapa-<aplicativo>.html`, sin fecha
   en el nombre). Lleva la fecha y el commit del código en que se basó, y una sección «Qué cambió desde la última
   vez». Al abrirlo, la skill avisa si el código avanzó desde ese commit. Las presentaciones de profundizar sí
   llevan fecha.
6. **Registro de conceptos con carga inicial:** la primera vez se llena una sola vez con los conceptos de las
   láminas que ya existen en `arm-centro/explicaciones/`, para que el primer mapa de ARMEGA no vuelva a enseñar
   RLS, cola o pg-boss.

### Piezas de la skill

```
skills/analizar-aplicativo/
  SKILL.md                     # cuándo se usa, los dos modos, el flujo y las reglas duras
  references/
    mapa.md                    # secciones del mapa y qué va en cada una
    profundizar.md             # forma de la presentación por tema
    comparar.md                # forma de la presentación lado a lado
    negocio.md                 # cómo deducir el negocio en un aplicativo ajeno y leerlo en uno propio
    alcance-y-limites.md       # cómo armar la tabla de objetivos frente a construcción
    marcas.md                  # comprobado, deducido, por confirmar: cuándo se usa cada una
    seguridad.md               # qué revisar y qué no copiar nunca
    diagramas.md               # tipos de diagrama en SVG y cuándo usar cada uno
    lectores.md                # el encargo de cada agente lector en proyectos grandes
  assets/
    plantilla.html             # estilos de las láminas de ARM y componentes (tarjetas, tablas, marcas, diagramas)
```

## Lo que queda al constructor

- La redacción exacta de `SKILL.md` y de su descripción para que se active bien (y no choque con
  `documentos-para-compartir`, `centro-de-proyecto` ni `revision-tecnica`).
- Cuándo un proyecto es «grande» para repartir entre agentes.
- El detalle de la plantilla y de los tipos de diagrama.
- Cómo probar la skill: correrla sobre ARMEGA (`ARM/desarrollo/arm-plataforma`, propio) y sobre crm-conex (ajeno)
  y revisar el resultado con Jesús.
- Agregarla al README de `mis-skills` y enlazarla en `~/.claude/skills/`.
