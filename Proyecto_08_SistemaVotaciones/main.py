from candidato import Partido, Ciudad, Pais

def linea():
    print("-" * 40)

def pedir_opcion(min_op, max_op):
    opcion = input("Introduce la opción deseada: ")
    while not opcion.isdigit() or not (min_op <= int(opcion) <= max_op):
        print("Opción inválida.")
        opcion = input("Introduce una opción válida: ")
    return int(opcion)

def obtener_partidos_manual():
    pais_nombre = input("Introduce el nombre del país: ")
    pais = Pais(pais_nombre)
    n_ciudades = int(input("¿Cuántas ciudades quieres introducir? "))
    for _ in range(n_ciudades):
        linea()
        ciudad_nombre = input("Nombre de la ciudad: ")
        ciudad = Ciudad(ciudad_nombre)
        pais.ciudades.append(ciudad)
        n_partidos = int(input(f"¿Cuántos partidos hay en {ciudad_nombre}? "))
        for _ in range(n_partidos):
            print("\n--- Datos del partido ---")
            nombre = input("Nombre del partido: ")
            corriente = input("Corriente del partido: ")
            popularidad = int(input("Número de votantes: "))
            ciudad.meter_partido(Partido(nombre, corriente, popularidad))

    return pais

def cargar_partidos_desde_fichero(nombre_fichero="partidos.txt"):
    pais = Pais("País desde fichero")
    ciudades_dict = {}
    try:
        with open(nombre_fichero, "r", encoding="utf-8") as f:
            next(f)  # Saltamos encabezado si existe
            for linea in f:
                datos = linea.strip().split()
                if len(datos) != 4:
                    continue
                ciudad_nombre, partido_nombre, corriente, popularidad = datos
                partido = Partido(partido_nombre, corriente, int(popularidad))
                if ciudad_nombre not in ciudades_dict:
                    ciudad = Ciudad(ciudad_nombre)
                    ciudades_dict[ciudad_nombre] = ciudad
                    pais.ciudades.append(ciudad)
                else:
                    ciudad = ciudades_dict[ciudad_nombre]
                ciudad.meter_partido(partido)

    except FileNotFoundError:
        print(f"No se encontró el fichero '{nombre_fichero}'")

    return pais

def guardar_partidos_en_fichero(pais, nombre_fichero="partidos.txt"):
    with open(nombre_fichero, "w", encoding="utf-8") as f:
        for ciudad in pais.ciudades:
            for partido in ciudad.partidos:
                f.write(
                    f"{ciudad.localidad} {partido.nombre} "
                    f"{partido.corriente} {partido.popularidad}\n"
                )
    print(f"Datos guardados en '{nombre_fichero}'")

def menu_pais(pais):
    while True:
        linea()
        print("-------- GESTOR DEL PAÍS --------")
        print("1.- Mostrar país completo")
        print("2.- Mostrar ciudades por separado")
        print("3.- Ciudad con partido más popular")
        print("4.- Generar informe del país")
        print("5.- Guardar datos en fichero")
        print("6.- Volver al menú principal")
        linea()
        opcion = pedir_opcion(1, 6)
        if opcion == 1:
            print("\n" + str(pais))
        elif opcion == 2:
            pais.mostrar_ciudad()
        elif opcion == 3:
            ciudad_top, partido_top = pais.ciudad_popular()
            if partido_top:
                print(
                    f"\nCiudad: {ciudad_top}\n"
                    f"Partido: {partido_top.nombre}\n"
                    f"Votantes: {partido_top.popularidad}"
                )
            else:
                print("No hay partidos registrados.")
        elif opcion == 4:
            print("\n" + pais.informe())
        elif opcion == 5:
            nombre_fichero = input("Nombre del fichero para guardar: ")
            guardar_partidos_en_fichero(pais, nombre_fichero)
        elif opcion == 6:
            break
def menu_principal():
    pais = None
    while True:
        linea()
        print("-------- MENÚ PRINCIPAL --------")
        print("1.- Cargar datos manualmente")
        print("2.- Cargar datos desde fichero")
        print("3.- Gestionar país")
        print("4.- Salir")
        linea()
        opcion = pedir_opcion(1, 4)
        if opcion == 1:
            pais = obtener_partidos_manual()
        elif opcion == 2:
            nombre_fichero = input("Nombre del fichero: ")
            pais = cargar_partidos_desde_fichero(nombre_fichero)
        elif opcion == 3:
            if pais is None:
                print("Primero debes cargar o crear un país.")
            else:
                menu_pais(pais)
        elif opcion == 4:
            print("Bye Bye...")
            break
def main():
    menu_principal()

if __name__ == "__main__":
    main()
