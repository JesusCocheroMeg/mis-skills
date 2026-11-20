# Modo mapa

Una presentación del aplicativo completo: negocio, piezas, seguridad, alcance y límites. Es la puerta de entrada;
los temas que pidan más detalle se profundizan aparte y se enlazan desde aquí.

Archivo: `mapa-<aplicativo>.html` (sin fecha). **Uno por aplicativo, se actualiza**; no se crea otro.

## Portada (`<section class="slide full">`)

- Eyebrow: `<Aplicativo> · Mapa · <fecha>`.
- Título: el nombre del aplicativo y en pocas palabras qué es.
- Lead: el aplicativo en dos frases (problema y para quién).
- Línea de base: **commit analizado** (`git rev-parse --short HEAD`, rama) y si es propio o ajeno.
- Aviso si más de la mitad es deducido (ver `marcas.md`).
- Leyenda de marcas y veredictos.
- Índice con enlaces a las secciones.

## Las 11 secciones

1. **El aplicativo en un minuto.** Problema, para quién, qué hace. Con una analogía si ayuda.
2. **Cómo lo vive quien lo usa.** Roles y flujos principales contados como los vive la persona. Diagrama de flujo
   del usuario (`diagramas.md`).
3. **Las piezas y cómo se conectan.** Diagrama de arquitectura. Por cada pieza: qué hace, dónde vive en el código
   y **qué parte del negocio sostiene** (`negocio.md`, «el hilo»).
4. **Tecnologías.** Tabla: tecnología y versión · para qué · por qué esta · alternativas. En un aplicativo propio, el
   porqué viene de las decisiones (comprobado); en uno ajeno, deducido.
5. **Datos.** Qué guarda (entidades principales y cómo se relacionan), qué datos sensibles tiene y cómo separa
   empresas o usuarios.
6. **Seguridad.** Resumen de `seguridad.md`: lo que está bien, los riesgos principales y qué preguntar. Si hay
   mucho, deja lo principal y sugiere profundizar.
7. **¿La construcción alcanza para lo que se quiere lograr?** La tabla de `alcance-y-limites.md` con 4 a 8 objetivos.
8. **Lo que conviene decidir o preguntar.** Decisiones abiertas, cada una con la recomendación y su porqué; preguntas
   por confirmar agrupadas por a quién se le hacen.
9. **Temas para profundizar.** Enlaces a las presentaciones ya hechas (profundizar y comparar) y una lista de las
   sugeridas, con una línea de por qué valen la pena.
10. **Para aprender.** Solo conceptos que **no** están en el registro de conceptos: qué es, ejemplo simple, por qué
    importa en este aplicativo. Los ya vistos, en una línea con enlace a donde se enseñaron.
11. **Fuentes y marcas.** Qué se leyó (carpetas, documentos), qué no se alcanzó a revisar, y el conteo de marcas.

Cada pieza o tema importante cierra con un bloque **qué mirar y qué preguntar**:

```html
<div class="preguntar"><h3>Qué mirar y qué preguntar</h3>
  <ul><li>Si alguien propone Redis, pregunta cuántos trabajos por segundo hay hoy.</li></ul></div>
```

## Al actualizar un mapa que ya existe

1. Lee el mapa anterior y su commit base. Compara (`git log --oneline <commit>..HEAD`, `git diff --stat`).
2. Rehaz las secciones que cambiaron; conserva los enlaces de la sección 9.
3. Agrega después de la portada una sección **«Qué cambió desde la última vez»**: fecha anterior, commits nuevos y
   lo que cambia para el negocio, las piezas, la seguridad o los límites.
4. Actualiza el commit base en la portada.

Si al abrir un mapa el código avanzó desde su commit base, avísale a Jesús y ofrece actualizarlo.
