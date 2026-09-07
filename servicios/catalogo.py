import json
from typing import List, Set, Optional
from modelos.juego import Juego

class CatalogoJuegos:
    def __init__(self):
        self._juegos: List[Juego] = []

    def cargar_desde_json(self, ruta_archivo: str) -> None:
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as file:
                datos = json.load(file)
                self._juegos = [
                    Juego(
                        id_juego=item['id'],
                        titulo=item['titulo'],
                        generos=item['generos'],
                        desarrollador=item['desarrollador'],
                        calificacion=item['calificacion'],
                        anio_publicacion=item['anioPublicacion'],
                        web=item.get('web', '')
                    )
                    for item in datos
                ]
            print(f"✅ Se cargaron exitosamente {len(self._juegos)} videojuegos.")
        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo '{ruta_archivo}'.")
        except json.JSONDecodeError:
            print(f"❌ Error: El archivo '{ruta_archivo}' no es un JSON válido.")

    # --- 1. BUSCAR VIDEOJUEGO ---
    def buscar_por_titulo(self, titulo: str) -> List[Juego]:
        palabras = titulo.strip().lower().split(" ")
        juegos_encontrados = self._juegos.copy()
        for palabra in palabras:
            for juego in juegos_encontrados[:]:
                if palabra not in juego.titulo.lower():
                    juegos_encontrados.remove(juego)
        return juegos_encontrados

    def obtener_por_titulo_exacto(self, titulo: str) -> Optional[Juego]:
        busqueda = titulo.strip().lower()
        for j in self._juegos:
            if j.titulo.lower() == busqueda:
                return j
        return None

    # --- 2. EXPLORAR POR GÉNERO ---
    def obtener_por_genero(self, genero: str) -> List[Juego]:
        return [j for j in self._juegos if j.tiene_genero(genero)]

    def obtener_todos_los_generos(self) -> List[str]:
        todos: Set[str] = set()
        for j in self._juegos:
            todos.update(j.generos)
        return sorted(list(todos))

    # --- 3. VER JUEGOS RELACIONADOS ---
    def obtener_relacionados(self, juego_base: Juego, limite: int = 5) -> List[Juego]:
        """Obtiene otros juegos que compartan al menos un género con el juego base."""
        candidatos = []
        for j in self._juegos:
            if j.id != juego_base.id:
                coincidencias = juego_base.generos_en_comun(j)
                if coincidencias > 0:
                    candidatos.append((j, coincidencias))

        # Ordenar por mayor cantidad de géneros compartidos y luego por calificación
        candidatos.sort(key=lambda item: (item[1], item[0].calificacion), reverse=True)
        return [j for j, _ in candidatos[:limite]]

    # --- 4. OBTENER RECOMENDACIONES ---
    def obtener_recomendaciones(self, juego_base: Juego, limite: int = 3) -> List[Juego]:
        """Obtiene recomendaciones priorizando similitud de géneros + mayor calificación."""
        relacionados = self.obtener_relacionados(juego_base, limite=limite * 2)
        # Filtramos o re-ordenamos por mejor nota
        recomendaciones = sorted(relacionados, key=lambda j: j.calificacion, reverse=True)
        return recomendaciones[:limite]

    # --- 5. VER TOP 10 ---
    def obtener_top_n(self, n: int = 10) -> List[Juego]:
        return sorted(self._juegos, key=lambda j: j.calificacion, reverse=True)[:n]