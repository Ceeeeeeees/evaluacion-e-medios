import json
import sys
from datetime import datetime, timedelta, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class ValidarServicio:
    def __init__(self, sitios):
        self.sitios = sitios

    def obtenerFechaActual(self, zona_horaria=timezone.utc):
        return datetime.now(zona_horaria)

    def obtener

    def verificar(self, sitio):
        base = sitio.strip().rstrip("/")
        if not base.startswith(("http://", "https://")):
            base = "https://" + base
        api = base + "/wp-json/wp/v2/posts?per_page=1"
        req = Request(api, headers={"User-Agent": "ValidadorWP/1.0"})
        with urlopen(req, timeout=10) as respuesta:
            if respuesta.status != 200:
                return f"HTTP {respuesta.status}"
            posts = json.load(respuesta)
        if not posts:
            return "no tiene notas publicadas"
        fecha = posts[0].get("date_gmt")
        if not fecha:
            return "la API no devolvió date_gmt"
        publicada = datetime.fromisoformat(fecha.replace("Z", "+00:00"))
        if publicada.tzinfo is None:
            publicada = publicada.replace(tzinfo=timezone.utc)
        edad = self.obtenerFechaActual(timezone.utc) - publicada
        if edad < timedelta(0):
            return "la fecha de la nota está en el futuro"
        if edad >= timedelta(hours=24):
            return f"la última nota tiene más de 24 horas ({publicada.isoformat()})"
        return None

    def ejecutar(self):
        fallos = []
        for sitio in self.sitios:
            try:
                motivo = self.verificar(sitio)
            except (HTTPError, URLError, TimeoutError, ValueError, json.JSONDecodeError) as e:
                motivo = str(e)
            if motivo:
                fallos.append((sitio, motivo))
        print(f"Sitios revisados: {len(self.sitios)} | Fallos: {len(fallos)}")
        for sitio, motivo in fallos:
            print(f"- {sitio}: {motivo}")
        if not fallos:
            print("Todos los sitios responden y tienen una nota reciente.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(f"Uso: python {sys.argv[0]} dominio1.com dominio2.com")
    ValidarServicio(sys.argv[1:]).ejecutar()
