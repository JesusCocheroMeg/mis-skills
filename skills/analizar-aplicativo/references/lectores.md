# Repartir la lectura en proyectos grandes

## Cuándo repartir

- Más de ~300 archivos de código (sin contar dependencias, compilados ni pruebas generadas), o
- más de un repo, o
- un monorepo con varias apps.

Si es más chico, lee tú mismo: repartir cuesta más de lo que ahorra.

## Los tres lectores

Lánzalos en paralelo (Agent tool, tipo `Explore` o `general-purpose`), en un solo mensaje. Cada uno recibe la ruta
del repo, si hay centro o documentos, y su encargo:

| Lector | Encargo |
|---|---|
| **Negocio** | Qué problema resuelve, para quién, roles, flujos principales, estados del proceso, vocabulario. Sigue `negocio.md` |
| **Piezas y datos** | Apps y servicios, cómo se comunican, tecnologías con versión, modelo de datos, procesos de fondo, integraciones, configuración de despliegue, pruebas |
| **Seguridad** | Lo de `seguridad.md`. Sin copiar ningún valor de secreto |

## Lo que devuelve cada lector

Una lista de hallazgos, uno por línea, con este formato:

```
- <afirmación> | comprobado|deducido|por confirmar | <ruta:línea o razón>
```

Más una lista corta de **preguntas por confirmar** y de **dónde no alcanzó a mirar**.

## Al juntar

- Si dos lectores se contradicen, ve tú al archivo y decide. Lo que no se pueda decidir queda por confirmar.
- Lo que un lector no alcanzó a mirar va en «Fuentes y marcas» como no revisado.
- Los lectores no escriben archivos; solo tú armas la presentación.
