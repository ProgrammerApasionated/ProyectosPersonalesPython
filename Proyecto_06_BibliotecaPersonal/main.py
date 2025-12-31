# Fichero que combina y crea el programa en general.
from libro import Libro
def line():
    print ("-" * 40)

def cargar_libros():
    libros = {}
    try:
        with open("datos/biblioteca.txt", "r", encoding="utf-8") as f:
            for linea in f:
                libro = Libro.from_linea(linea)
                libros[libro.isbn] = libro
    except FileNotFoundError:
        print("No existe biblioteca.txt, se creará al guardar.")
    return libros
def guardar_libros(libros):
    with open("datos/biblioteca.txt", "w", encoding="utf-8") as f:
        for libro in libros.values():
            f.write(libro.to_linea() + "\n")
    print("Libros guardados correctamente.")
def mostrar_menu():
    line()
    print("-" * 4 + " MENú PRINCIPAL " + "-" * 4)
    print("1. Gestionar libros")
    print("2. Gestionar préstamos")
    print("3. Mostrar estadísticas")
    print("4. Guardar y salir")
    opc = input ("Introduce la opción interesada: \n")
    line()
    return opc

def main():
    libros = cargar_libros()
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            gestionar_libros(libros)
        elif opcion == "2":
            gestionar_prestamos(libros)
        elif opcion == "3":
            mostrar_estadisticas(libros)
        elif opcion == "4":
            guardar_libros(libros)
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
def gestionar_libros(libros):
    while True:
        line()
        print ("-" * 4 + " GESTIONAR LIBROS " + "-" * 4)
        print ("1.- Añadir libros")
        print ("2.- Ver libros")
        print ("3.- Eliminar libros")
        print ("4.- Buscar libro por ISBN")
        print ("5.- Salir")
        opci = input ("Introduce la opción deseada: \n")
        line()
        if opci == "1":
            añadir_libro(libros)
        elif opci == "2":
            ver_libros(libros)
        elif opci == "3":
            elim_libro(libros)
        elif opci == "4":
            busc_libro(libros)
        elif opci == "5":
            break
        else :
            print("Opción invalida")
def añadir_libro(libros):
    titulo = input("Introduzca el título del libro: \n")
    while titulo == "":
        titulo = input("El título no puede estar vacío. Introduzca un título válido. \n")
    autor = input("Introduzca el autor del libro: \n")
    while autor == "":
        autor = input("El autor no puede estar vacío. Introduzca un autor válido. \n")
    año = input("Introduce el año del libro: \n")
    while not año.isdigit():
        año = input("El año tiene que ser un número. Introduce el año. \n")
    isbn = input("Introduce el ISBN del libro: \n")
    while not isbn.isdigit():
        isbn = input("El ISBN tiene que ser un número. Introduce el ISBN. \n")
    if isbn in libros:
        print("Ya existe un libro con ese ISBN.")
        return
    libro_nuevo = Libro(titulo, autor, int(año), isbn)
    libros[isbn] = libro_nuevo
    print("Libro añadido correctamente.")
def ver_libros(libros):
    if not libros:
        print("No hay libros registrados.")
        return
    cant_libros = 0
    for libro in libros.values():
        cant_libros += 1
        print(f"[{cant_libros}]   -> [{libro}]")
def elim_libro(libros):
    isbn = input("Introduce el isbn del libro a eliminar: ")
    if isbn not in libros:
        print("No existe un libro con ese código.")
        return
    del libros[isbn]
    print("Libro eliminado correctamente.")
    line()
def busc_libro(libros):
    isbn = input("Introduce el isbn del libro a encontrar: \n")
    if isbn not in libros:
        print("No existe un libro con ese código.")
        return
    print (libros[isbn])
    line()
def gestionar_prestamos(libros):
    while True:
        line()
        print("-" * 4 + " GESTIONAR PRESTAMOS " + "-" * 4)
        print("1.- Prestar libro")
        print("2.- Devolver libro")
        print("3.- Volver")
        op = input("Introduce la opción deseada \n")
        line()
        if op == "1":
            line()
            isbn = input("Introduce el ISBN del libro a prestar: \n")
            if isbn not in libros:
                print("No existe un libro con ese ISBN.")
            else:
                libros[isbn].prestar()
            line()
        elif op == "2":
            line()
            isbn = input("Introduce el ISBN del libro a devolver: \n")
            if isbn not in libros:
                print("No existe un libro con ese ISBN.")
            else:
                libros[isbn].devolver()
            line()
        elif op == "3":
            break
        else:
            print("Opción inválida.")
def mostrar_estadisticas(libros):
    line()
    print("-" * 4 + " ESTADÍSTICAS " + "-" * 4)
    if not libros:
        print("No hay libros registrados.")
        return
    total = len(libros)
    prestados = sum(1 for l in libros.values() if l.prestado)
    disponibles = total - prestados
    # Autor más frecuente
    autores = {}
    for libro in libros.values():
        autores[libro.autor] = autores.get(libro.autor, 0) + 1
    autor_mas_frecuente = max(autores, key=autores.get)
    # Año más común
    años = {}
    for libro in libros.values():
        años[libro.año] = años.get(libro.año, 0) + 1
    año_mas_comun = max(años, key=años.get)
    # Buscamos el año más buscado con la clave años que tiene el máximo valor de apariciones.
    print(f"Total de libros: {total}")
    print(f"Libros prestados: {prestados}")
    print(f"Libros disponibles: {disponibles}")
    print(f"Autor más frecuente: {autor_mas_frecuente}")
    print(f"Año más común: {año_mas_comun}")
    line()
if __name__ == "__main__":
    main()
