from estudiante import Estudiante
from asignatura import Asignatura
import csv
# Parte que une todos los ficheros y incluye el menú interactivo.
def line():
    print ("-" * 40)
def cargar_datos():
    estudiantes = {}  # Diccionario donde guardaremos los estudiantes
    try:
        with open("datos/notas.csv", "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Saltamos la cabecera del CSV
            for fila in lector:
                dni, nombre, correo, codigo_asig, nota = fila
                # Si el estudiante no existe, lo creamos
                if dni not in estudiantes:
                    estudiantes[dni] = Estudiante(dni, nombre, correo)
                # Añadimos la nota a su diccionario
                estudiantes[dni].agregar_notas(codigo_asig, float(nota))
    except FileNotFoundError:
        print("El archivo notas.csv no existe. Se creará al guardar datos.")
    return estudiantes

def guardar_datos(estudiantes):
    with open("datos/notas.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        # Cabecera del CSV
        escritor.writerow(["dni", "nombre", "correo", "codigo_asig", "nota"])
        # Recorremos todos los estudiantes
        for dni, estudiante in estudiantes.items():
            # Recorremos todas las notas del estudiante
            for codigo_asig, nota in estudiante.notas.items():
                escritor.writerow([
                    estudiante.dni,
                    estudiante.nombre,
                    estudiante.correo,
                    codigo_asig,
                    nota
                ])
    print("Datos guardados correctamente en notas.csv")

def mostrar_menu():
    line()
    print( 4 * "-" + " MENÚ PRINCIPAL" + "-" * 4)
    print("1. Gestionar estudiantes")
    print("2. Gestionar asignaturas")
    print("3. Gestionar notas")
    print("4. Mostrar estadísticas")
    print("5. Guardar y salir")
    line()
    opcion = input("Elige una opción: ")
    opciones = ["1" , "2", "3", "4", "5"]
    while opcion not in opciones:
        print("Opción no válida. Inténtalo de nuevo.")
        opcion = input("Elige una opción: ")
    return opcion

def gestionar_estudiantes(estudiantes):
    while True:
        line()
        print(4 * "-" + " GESTOR ESTUDIANTES " + "-" * 4)
        print("1. Añadir estudiante")
        print("2. Ver estudiantes")
        print("3. Eliminar estudiante")
        print("4. Volver")
        line()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            añadir_estudiante(estudiantes)
        elif opcion == "2":
            ver_estudiantes(estudiantes)
        elif opcion == "3":
            eliminar_estudiante(estudiantes)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")
def añadir_estudiante(estudiantes):
    dni = input("DNI del estudiante: ")
    nombre = input("Nombre del estudiante: ")
    correo = input("Correo del estudiante: ")
    if dni in estudiantes:
        print("Ya existe un estudiante con ese DNI.")
        return
    estudiantes[dni] = Estudiante(dni, nombre, correo)
    print("Estudiante añadido correctamente.")

def ver_estudiantes(estudiantes):
    line()
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print("-" * 4 + " LISTA DE ESTUDIANTES " + "-" * 4)
    for estudiante in estudiantes.values():
        print(estudiante)
    line()
def eliminar_estudiante(estudiantes):
    dni = input("Introduce el DNI del estudiante a eliminar: ")
    if dni not in estudiantes:
        print("No existe un estudiante con ese DNI.")
        return
    del estudiantes[dni]
    print("Estudiante eliminado correctamente.")
    line()

def gestionar_asignaturas(asignaturas):
    while True:
        line()
        print(4 * "-" + " GESTOR ASIGNATURAS " + "-" * 4)
        print("1. Añadir asignatura")
        print("2. Ver asignaturas")
        print("3. Eliminar asignatura")
        print("4. Volver")
        line()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            añadir_asignatura(asignaturas)
        elif opcion == "2":
            ver_asignaturas(asignaturas)
        elif opcion == "3":
            eliminar_asignatura(asignaturas)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")
def añadir_asignatura(asignaturas):
    codigo = input("Código de la asignatura (ABC123): ")
    # Creamos un objeto temporal para usar su validador
    inicializar = Asignatura(codigo, "", 0)
    while not inicializar.validar_codigo(codigo):
        print("Código inválido. Debe ser 3 letras + 3 números.")
        codigo = input("Introduce un código válido: ")
        inicializar = Asignatura(codigo, "", 0)
    nombre = input("Nombre de la asignatura: ")
    creditos = int(input("Créditos: "))
    asignaturas[codigo] = Asignatura(codigo, nombre, creditos)
    print("Asignatura añadida correctamente.")
def ver_asignaturas(asignaturas):
    if not asignaturas:
        print("No hay asignaturas registradas.")
        return
    line()
    print(4 * "-" + " LISTA ASIGNATURAS " + "-" * 4)
    for asignatura in asignaturas.values():
        print(asignatura)
    line()
def eliminar_asignatura(asignaturas):
    codigo = input("Introduce el código de la asignatura a eliminar: ")
    if codigo not in asignaturas:
        print("No existe una asignatura con ese código.")
        return
    del asignaturas[codigo]
    print("Asignatura eliminada correctamente.")
    line()
def gestionar_notas(estudiantes, asignaturas):
    while True:
        line()
        print("-" * 4 + " GESTOR NOTAS " + "-" * 4)
        print("1. Añadir nota")
        print("2. Modificar nota")
        print("3. Eliminar nota")
        print("4. Ver notas de un estudiante")
        print("5. Volver")
        line()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            añadir_nota(estudiantes, asignaturas)
        elif opcion == "2":
            modificar_nota(estudiantes)
        elif opcion == "3":
            eliminar_nota(estudiantes)
        elif opcion == "4":
            ver_notas_estudiante(estudiantes)
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")
        line()
def añadir_nota(estudiantes, asignaturas):
    dni = input("DNI del estudiante: ")
    if dni not in estudiantes:
        print("No existe un estudiante con ese DNI.")
        return
    codigo = input("Código de la asignatura: ")
    if codigo not in asignaturas:
        print("No existe una asignatura con ese código.")
        return
    try:
        nota = float(input("Introduce la nota: "))
    except ValueError:
        print("La nota debe ser un número.")
        return
    estudiantes[dni].agregar_notas(codigo, nota)
    print("Nota añadida correctamente.")

def modificar_nota(estudiantes):
    dni = input("DNI del estudiante: ")

    if dni not in estudiantes:
        print("No existe un estudiante con ese DNI.")
        return
    codigo = input("Código de la asignatura: ")
    if codigo not in estudiantes[dni].notas:
        print("Ese estudiante no tiene nota en esa asignatura.")
        return
    try:
        nueva_nota = float(input("Nueva nota: "))
    except ValueError:
        print("La nota debe ser un número.")
        return
    estudiantes[dni].modificar_nota(codigo, nueva_nota)
    print("Nota modificada correctamente.")

def eliminar_nota(estudiantes):
    dni = input("DNI del estudiante: ")
    if dni not in estudiantes:
        print("No existe un estudiante con ese DNI.")
        return
    codigo = input("Código de la asignatura: ")
    if codigo not in estudiantes[dni].notas:
        print("Ese estudiante no tiene esa asignatura.")
        return
    estudiantes[dni].eliminar_asignatura(codigo)
    print("Nota eliminada correctamente.")

def ver_notas_estudiante(estudiantes):
    dni = input("DNI del estudiante: ")
    if dni not in estudiantes:
        print("No existe un estudiante con ese DNI.")
        return
    print(f"\nNotas de {estudiantes[dni].nombre}:")
    estudiantes[dni].mostrar_notas()


def mostrar_estadisticas(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print("-" * 4 + " ESTADISTICAS " + "-" * 4)
    total_notas = 0
    cantidad_notas = 0
    mejor_media = -1
    peor_media = 11
    mejor_estudiante = None
    peor_estudiante = None
    aprobados = 0
    suspensos = 0
    for est in estudiantes.values():
        if not est.notas:
            continue
        suma = sum(est.notas.values())
        num = len(est.notas)
        media = suma / num
        for nota in est.notas.values():
            if nota >= 5:
                aprobados += 1
            else:
                suspensos += 1
        total_notas += suma
        cantidad_notas += num
        if media > mejor_media:
            mejor_media = media
            mejor_estudiante = est
        if media < peor_media:
            peor_media = media
            peor_estudiante = est
    if cantidad_notas == 0:
        print("No hay notas registradas.")
        return
    media_global = total_notas / cantidad_notas
    print(f"Media global de todas las notas: {media_global:.2f}")
    if mejor_estudiante:
        print(f"Mejor estudiante: {mejor_estudiante.nombre} (media {mejor_media:.2f})")
    if peor_estudiante:
        print(f"Peor estudiante: {peor_estudiante.nombre} (media {peor_media:.2f})")
    print(f"Total de notas: {cantidad_notas}")
    print(f"Aprobados: {aprobados}")
    print(f"Suspensos: {suspensos}")

def main():
    estudiantes = cargar_datos()
    asignaturas = {}
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            gestionar_estudiantes(estudiantes)
        elif opcion == "2":
            gestionar_asignaturas(asignaturas)
        elif opcion == "3":
            gestionar_notas(estudiantes, asignaturas)
        elif opcion == "4":
            mostrar_estadisticas(estudiantes)
        elif opcion == "5":
            guardar_datos(estudiantes)
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()
