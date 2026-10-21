# Ejercicio - 1

Ejercicio como parte de la evaluación.

## Contexto

Una tarea programada corre cada 10 minutos en una Mac mini que funciona como servidor. Su log muestra, ciclo tras ciclo, estas tres líneas:

```code
2026-10-14 12:08:47 --- ciclo inicio ---
Failed to authenticate: OAuth session expired and could not be refreshed
2026-10-14 12:08:48 --- ciclo fin (exit 0) ---
```

El tablero de monitoreo marca la tarea en verde.

Responde:

- **A)** ¿Qué está pasando y cómo averiguarías desde cuándo?
- **B)** ¿Qué harías hoy para arreglarlo?
- **C)** ¿Qué cambiarías para que una tarea que corre pero no hace nada nunca vuelva a aparecer en verde?

## Propuesta de solución

- **A)** La tarea inicio y se ejecuto, sin embargo no pudo autenticarse porque la sesión OAuth expiró y no se pudo renovar. Además, devolvió un código tipo 0, posiblemente un código de error que todo está bien. POsiblemente al devolver 1 significaria error al intentar levantar el servidor, esto se tendria que validar revisando los demás logs al momento de levantar el servidor de manera exitosa y sin problema de la sesión.

- **B)** Revisaria la configuación de OAuth y renovaría la sesión o dado el caso que se requiera, autoriazaria la sesión. Posteriormente volveira a ejecutar la tarea manualmente para observar el comportamiento, validar la autenticación y complete su operación y/o flujo.

- **C)** Trataria de implementar un mensaje de errores en los logs para que sea más detallado, por ejemplo, fallo en la autenticación, fallo al levantar la aplicación x, etc. Además, trabajaria para que el tablero hiciera una doble validación minutos después para conocer el estado de la ejecución después de su ciclo de inicio.