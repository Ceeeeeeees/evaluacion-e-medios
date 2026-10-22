# Ejercicio - 3

Ejercicio como parte de la evaluación.

## Contexto

Escribe un script en Python de **máximo 60 líneas** que reciba una lista de dominios de sitios WordPress y verifique, para cada uno, que:

1. El sitio responde.
2. Su nota más reciente tiene menos de 24 horas.

La API pública de WordPress está disponible en:

```code
/wp-json/wp/v2/posts?per_page=1
```

El script debe imprimir un resumen con los sitios que fallan. Adjunta el script o compártelo mediante un enlace a un gist.