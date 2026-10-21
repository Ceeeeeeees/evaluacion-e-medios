# Evaluación técnica

Esta evaluación contiene tres ejercicios sobre diagnóstico de tareas programadas, manejo de secretos y automatización con Python.

## Ejercicio 1 — Diagnóstico

Una tarea programada corre cada 10 minutos en una Mac mini que funciona como servidor. Su log muestra, ciclo tras ciclo, estas tres líneas:

```text
2026-10-14 12:08:47 --- ciclo inicio ---
Failed to authenticate: OAuth session expired and could not be refreshed
2026-10-14 12:08:48 --- ciclo fin (exit 0) ---
```

El tablero de monitoreo marca la tarea en verde.

Responde:

- **a)** ¿Qué está pasando y cómo averiguarías desde cuándo?
- **b)** ¿Qué harías hoy para arreglarlo?
- **c)** ¿Qué cambiarías para que una tarea que corre pero no hace nada nunca vuelva a aparecer en verde?

## Ejercicio 2 — Secretos

Descubres que la contraseña de la base de datos de producción está escrita en un archivo de log que varias personas pueden leer, y que el proceso la sigue escribiendo en cada corrida.

Describe, en orden, los pasos que darías durante:

1. La primera hora.
2. La primera semana.

## Ejercicio 3 — Script

Escribe un script en Python de **máximo 60 líneas** que reciba una lista de dominios de sitios WordPress y verifique, para cada uno, que:

1. El sitio responde.
2. Su nota más reciente tiene menos de 24 horas.

La API pública de WordPress está disponible en:

```text
/wp-json/wp/v2/posts?per_page=1
```

El script debe imprimir un resumen con los sitios que fallan. Adjunta el script o compártelo mediante un enlace a un gist.
