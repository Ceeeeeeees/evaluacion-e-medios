# Ejercicio - 2

Ejercicio como parte de la evaluación.

## Contexto

Descubres que la contraseña de la base de datos de producción está escrita en un archivo de log que varias personas pueden leer, y que el proceso la sigue escribiendo en cada corrida.

Describe, en orden, los pasos que darías durante:

1. La primera hora.
2. La primera semana.

## Propuesta de solución

- **Durante la primer hora**
    1. Notificar al equipo de seguridad, a las personas responsables de la BD y del proceso sobre el hallazgo.
    2. IDentificar el log, la base de datos, la cuenta, sus privilegios    comprometidos, así como los sistemas que hacen uso de la misma.
    3. Detener temporalmente el proceso que registra la contraseña.
    4. Restringir y poner en cautiverio el log, asímismo, solo permitir que personal estricto pueda acceder a él.
    5. IDentificar las cuentas que tenian acceso al log.
    6. Rotar la contraseña de la bd de forma manual.
    7. Verificar que la conexión hacia la BD funcione y que no aparezca la contraseña en los log.

- **Durante la primer semana**

    1. Comunicar al equipo de desarrollo sobre el hallazgo para que se realice una modificación sobre el proceso o lógica que registraba la contraseña.
    2. De existir indicios de explotación limitar la conectividad a la BD.
    3. Proponer una politica de uso y gestión de secretos.