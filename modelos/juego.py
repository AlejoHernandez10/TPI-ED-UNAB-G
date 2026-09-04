from typing import List

class Juego:
    def __init__(self, id_juego: int, titulo: str, generos: List[str], desarrollador: str, calificacion: float, anio_publicacion: int, web: str = ""):
        self._id = id_juego
        self._titulo = titulo
        self._generos = generos
        self._desarrollador = desarrollador
        self._calificacion = calificacion
        self._anio_publicacion = anio_publicacion
        self._web = web

    @property
    def id(self) -> int:
        return self._id

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def generos(self) -> List[str]:
        return self._generos

    @property
    def desarrollador(self) -> str:
        return self._desarrollador

    @property
    def calificacion(self) -> float:
        return self._calificacion

    @property
    def anio_publicacion(self) -> int:
        return self._anio_publicacion

    @property
    def web(self) -> str:
        return self._web

    def tiene_genero(self, genero_buscado: str) -> bool:
        genero_limpio = genero_buscado.strip().lower()
        return any(g.lower() == genero_limpio for g in self._generos)

    def generos_en_comun(self, otro_juego: 'Juego') -> int:
        """Devuelve la cantidad de géneros/tags que comparte con otro juego."""
        mis_generos = {g.lower() for g in self._generos}
        otros_generos = {g.lower() for g in otro_juego.generos}
        return len(mis_generos.intersection(otros_generos))

    def __repr__(self) -> str:
        generos_str = ", ".join(self._generos)
        return f"{self._titulo} ({self._anio_publicacion}) - [{generos_str}] | ⭐ {self._calificacion}"