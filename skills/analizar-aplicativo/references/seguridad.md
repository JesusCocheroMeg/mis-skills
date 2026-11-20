# Seguridad

No es una auditoría formal ni un pentest. Es **lo que se ve en el código y la configuración**, explicado para que
Jesús entienda el riesgo y sepa qué preguntar.

## Qué revisar

| Tema | Preguntas |
|---|---|
| Ingreso | ¿Cómo entra la gente? ¿Contraseñas con hash (bcrypt, argon2, scrypt)? ¿Límite de intentos? ¿Sesiones que vencen? |
| Permisos | ¿Se comprueban en el servidor o solo en la pantalla? ¿Hay un lugar central o cada ruta lo hace a su manera? |
| Aislamiento | Si hay varias empresas o clientes, ¿qué impide que uno vea lo de otro? (RLS, filtro por `tenant_id`, bases separadas) |
| Secretos | ¿Están en variables de entorno o escritos en el código? ¿Hay `.env` subido al repo? |
| Datos sensibles | ¿Qué datos personales guarda (cédulas, teléfonos, audios)? ¿Se ven en logs? |
| Entradas | ¿Se valida lo que llega (Zod, Joi, class-validator)? ¿Hay SQL armado con texto? ¿Subidas de archivos sin límite? |
| Dependencias | ¿Versiones muy viejas o abandonadas en piezas críticas? |
| Exposición | CORS abierto, rutas de administración sin protección, errores que muestran detalles internos |

## Cómo redactar un riesgo

**Qué pasa · dónde · por qué importa · qué preguntar o hacer.** Ejemplo:

> Las contraseñas se comparan en texto plano <span class="marca comprobado">comprobado</span>
> <span class="fuente">src/auth/login.js:31</span>. Si alguien obtiene una copia de la base, tiene todas las
> contraseñas. Pregunta: ¿hay plan para migrarlas a hash?

## Lo que nunca se escribe

- **El valor de un secreto**, una contraseña, una llave, un token o una cadena de conexión. Se dice «hay una llave de
  X escrita en `archivo:línea`», nunca cuál es.
- **Datos personales reales** que aparezcan en semillas, pruebas o volcados.
- **Un paso a paso para explotar** un riesgo. Basta con el qué y el porqué.

El verificador (`scripts/verificar.py --repo`) revisa que no se haya colado ningún valor de los `.env`.

## Dónde se guarda

La presentación va al centro del proyecto si su repo es **privado**. Compruébalo antes de escribir riesgos de
seguridad (por ejemplo `gh repo view <dueño>/<repo> --json isPrivate`). Si el centro es público o no se puede
comprobar, la sección de seguridad va en un archivo aparte en `~/Desktop/Desarrollo/Analisis/<aplicativo>/` y el
mapa solo la enlaza.
