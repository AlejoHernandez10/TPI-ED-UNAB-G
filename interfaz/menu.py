import os
from typing import List
from modelos.juego import Juego

class InterfazConsola:
    
    @staticmethod
    def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def pausar():
        input("\nPresione ENTER para continuar...")

    @staticmethod
    def mostrar_menu_principal() -> str:
        InterfazConsola.limpiar_pantalla()
        print("========================================")
        print("            🎮 NEXTGAME")
        print("========================================")
        print("1. Buscar videojuego")
        print("2. Explorar por género")
        print("3. Ver juegos relacionados")
        print("4. Obtener recomendaciones")
        print("5. Ver Top 10")
        print("0. Salir")
        print("----------------------------------------")
        return input("Seleccione una opción: ").strip()

    # --- Métodos de Entrada ---
    @staticmethod
    def pedir_texto(mensaje: str) -> str:
        return input(f"\n{mensaje}: ").strip()

    @staticmethod
    def seleccionar_genero(generos: List[str]) -> str:
        """Muestra los géneros numerados y permite seleccionar por número o texto."""
        print("\nGéneros disponibles:")
        for idx, g in enumerate(generos, 1):
            print(f"  {idx:2d}. {g}")

        entrada = input("\nIngrese el número o el nombre del género: ").strip()

        # Si el usuario ingresó un número (ej: "2"), devolvemos el texto del género correspondiente
        if entrada.isdigit():
            idx = int(entrada) - 1
            if 0 <= idx < len(generos):
                return generos[idx]

        # Si ingresó el texto directamente (ej: "Arcade") o un número fuera de rango, devolvemos la entrada limpia
        return entrada

    # --- Métodos de Salida / Visualización ---
    @staticmethod
    def mostrar_lista_juegos(titulo_seccion: str, juegos: List[Juego]):
        print(f"\n{titulo_seccion} ({len(juegos)}):")
        if not juegos:
            print("  ❌ No se encontraron videojuegos.")
            return

        for j in juegos:
            print(f" • {j.titulo} ({j.anio_publicacion}) - [{', '.join(j.generos)}] | ⭐ {j.calificacion}")

    @staticmethod
    def mostrar_tarjeta_recomendaciones(juego_base: Juego, recomendaciones: List[Juego]):
        print("\n╔═════════════════════════════════════════════════════╗")
        print("║                   🎮 NEXTGAME                       ║")
        print("╠═════════════════════════════════════════════════════╣")
        print(f" Si te gustó {juego_base.titulo.upper()[:25]:<25}, quizás te interesen:")
        print("                                                      ")
        for idx, r in enumerate(recomendaciones, 1):
            print(f"  {idx}. {r.titulo:<32} ⭐ {r.calificacion:<4}")
        print("╚═════════════════════════════════════════════════════╝")

    @staticmethod
    def mostrar_top_10(juegos: List[Juego]):
        print("\n========================================")
        print("          🏆 TOP 10 VIDEOJUEGOS")
        print("----------------------------------------")
        for idx, j in enumerate(juegos, 1):
            print(f"{idx:2d}. {j.titulo:<28} ⭐ {j.calificacion}")
        print("----------------------------------------")

    @staticmethod
    def mostrar_mensaje(mensaje: str):
        print(f"\n{mensaje}")