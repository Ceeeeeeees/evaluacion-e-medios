from datetime import datetime, timedelta, timezone
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
import json

class ValidarServicio:
    def __init__(self, sitios):
        self.sitios = sitios

    def obtenerFechaActual(self, zona_horaria=timezone.utc):
        return datetime.now(zona_horaria)

    def obtenerPublicaciones(self, sitio):
        url = f"{sitio.rstrip('/')}/wp-json/wp/v2/posts?per_page=1"
        try:
            with urlopen(url, timeout=10) as respuesta:
                if respuesta.status != 200:
                    return None
                return json.load(respuesta)
        except (HTTPError, URLError, TimeoutError, ValueError):
            return None

    def obtenerFechaPublicacion(self, publicacion):
        fecha_texto = publicacion.get("modified_gmt") or publicacion.get("date_gmt")
        try:
            return datetime.fromisoformat(fecha_texto).replace(tzinfo=timezone.utc)
        except (TypeError, ValueError):
            return None

    def verificarFechaPublicacion(self, fecha_publicacion):
        return self.obtenerFechaActual() - fecha_publicacion < timedelta(hours=24)

    def verificarEdoSitio(self, sitio):
        publicaciones = self.obtenerPublicaciones(sitio)
        if publicaciones is None:
            print(f"{sitio}: no responde")
            return False
        if not publicaciones:
            print(f"{sitio}: responde, pero no tiene publicaciones")
            return False

        fecha_publicacion = self.obtenerFechaPublicacion(publicaciones[0])
        if fecha_publicacion is None:
            print(f"{sitio}: la fecha de publicación no es válida")
            return False

        tiene_nota_reciente = self.verificarFechaPublicacion(fecha_publicacion)
        estado = "tiene una nota de menos de 24 horas" if tiene_nota_reciente else "no tiene una nota de menos de 24 horas"
        print(f"{sitio}: responde y {estado}")
        return tiene_nota_reciente

    def recorrerSitios(self, sitios):
        lista_sitios_respondieron = []
        lista_sitios_no_respondieron = []

        if not sitios:
            return lista_sitios_respondieron, lista_sitios_no_respondieron

        for sitio in sitios:
            if self.verificarEdoSitio(sitio):
                lista_sitios_respondieron.append(sitio)
            else:
                lista_sitios_no_respondieron.append(sitio)

        return lista_sitios_respondieron, lista_sitios_no_respondieron

    def generarReporte(self, sitios_fallan, sitios_respondieron):
        print("\nResumen de sitios que respondieron:")
        print("\n".join(sitios_respondieron) if sitios_respondieron else "Ninguno")
        print("\nResumen de sitios que fallan:")
        print("\n".join(sitios_fallan) if sitios_fallan else "Ninguno")
        return sitios_fallan, sitios_respondieron

    def ejecutar(self):
        sitios_respondieron, sitios_fallan = self.recorrerSitios(self.sitios)
        return self.generarReporte(sitios_fallan, sitios_respondieron)

if __name__ == "__main__":
    sitios = [
        "https://wordpress.org",
    ]
    ValidarServicio(sitios).ejecutar()