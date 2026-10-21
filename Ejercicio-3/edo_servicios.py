from datetime import datetime, timedelta, timezone
from urllib.error import HTTPError, URLError



class ValidarServicio:
    def __init__(self, sitios):
        self.sitios = sitios

    def obtenerFechaActual(self, zona_horaria=timezone.utc):
        return datetime.now(zona_horaria)

    def obtenerFechaUltimaPublicacion(self, zona_horaria=timezone.utc):
        fecha_actual = self.obtenerFechaActual(zona_horaria)
        fecha_ultima_publicacion = fecha_actual - timedelta(hours=24)
        return fecha_ultima_publicacion

    def verificarRespuesta(self, sitio):
        return sitios

    def ejecutar(self):
        


if __name__ == "__main__":

