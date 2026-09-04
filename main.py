from servicios.catalogo import CatalogoJuegos
from interfaz.menu import InterfazConsola

def main():
    catalogo = CatalogoJuegos()
    catalogo.cargar_desde_json("datos/juegos.json")

    while True:
        opcion = InterfazConsola.mostrar_menu_principal()

        # 1. BUSCAR VIDEOJUEGO
        if opcion == "1":
            query = InterfazConsola.pedir_texto("Ingrese el título a buscar")
            resultados = catalogo.buscar_por_titulo(query)
            InterfazConsola.mostrar_lista_juegos("Resultados de búsqueda", resultados)
            InterfazConsola.pausar()

        # 2. EXPLORAR POR GÉNERO
        elif opcion == "2":
            generos = catalogo.obtener_todos_los_generos()
            # Permite seleccionar por número (ej: 2) o por texto (ej: Arcade)
            genero_sel = InterfazConsola.seleccionar_genero(generos)
            
            resultados = catalogo.obtener_por_genero(genero_sel)
            InterfazConsola.mostrar_lista_juegos(f"Videojuegos en '{genero_sel}'", resultados)
            InterfazConsola.pausar()

        # 3. VER JUEGOS RELACIONADOS
        elif opcion == "3":
            query = InterfazConsola.pedir_texto("Ingrese el título del juego base")
            coincidencias = catalogo.buscar_por_titulo(query)
            if coincidencias:
                juego = coincidencias[0]
                relacionados = catalogo.obtener_relacionados(juego, limite=5)
                InterfazConsola.mostrar_lista_juegos(f"Juegos relacionados con '{juego.titulo}'", relacionados)
            else:
                InterfazConsola.mostrar_mensaje("❌ No se encontró el juego especificado.")
            InterfazConsola.pausar()

        # 4. OBTENER RECOMENDACIONES
        elif opcion == "4":
            query = InterfazConsola.pedir_texto("¿Qué juego te gustó?")
            coincidencias = catalogo.buscar_por_titulo(query)
            if coincidencias:
                juego = coincidencias[0]
                recs = catalogo.obtener_recomendaciones(juego, limite=3)
                InterfazConsola.mostrar_tarjeta_recomendaciones(juego, recs)
            else:
                InterfazConsola.mostrar_mensaje("❌ No se encontró el juego especificado.")
            InterfazConsola.pausar()

        # 5. VER TOP 10
        elif opcion == "5":
            top_10 = catalogo.obtener_top_n(10)
            InterfazConsola.mostrar_top_10(top_10)
            InterfazConsola.pausar()

        # 0. SALIR
        elif opcion == "0":
            InterfazConsola.mostrar_mensaje("¡Gracias por usar NextGame!")
            break

        else:
            InterfazConsola.mostrar_mensaje("Opción inválida. Intente de nuevo.")
            InterfazConsola.pausar()

if __name__ == "__main__":
    main()