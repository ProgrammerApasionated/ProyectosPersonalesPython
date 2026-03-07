from Proyecto_07_AnalizadorTexto.analizador import contar_palabras, buscar_palabras, palabras_mas_frecuentes, \
    analisis_completo, contar_frase, contar_caracteres
# Menú implementación a partir de Conjunto/Menus/menu_base.py

def linea():
    print("-" * 40)

def pedir_opcion(min_op, max_op):
    opcion = input("Introduce la opción deseada: ")
    while not opcion.isdigit() or not (min_op <= int(opcion) <= max_op):
        print("Opción inválida.")
        opcion = input("Introduce una opción válida: ")
    return int(opcion)

def pedir_texto():
    texto = input ("Introduce el texto a analizar : \n")
    while texto == "":
        texto = input ("Introduce un texto válido distinto a la cadena vacía : \n")
    return texto

def pedir_palabra(texto):
    palabra = input ("Introduce una palabra a buscar en el texto : \n")
    while palabra == "" or len(palabra) > len(texto):
        palabra = input ("Introduce una palabra válida o una palabra más corta que el texto : \n")
    return palabra
def pedir_frecuencia():
    frec = int(input("Introduce la cantidad de palabras más encontradas en el texto : \n"))
    while frec <= 0:
        frec = int(input("Introduce una frecuencia mayor que 0 : \n"))
    return frec

def cargar_texto_desde_archivo():
    nombre = input("Introduce el nombre del archivo .txt (con extensión): ")
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            contenido = f.read()
        if contenido.strip() == "":
            print("El archivo está vacío. Introduce otro archivo.")
            return cargar_texto_desde_archivo()
        # Lee el contenido y se asegura de que no esté vacío.
        print("Archivo cargado correctamente.")
        return contenido
    except FileNotFoundError:
        print("No se ha encontrado el archivo. Inténtalo de nuevo.")
        return cargar_texto_desde_archivo()
    except UnicodeDecodeError:
        print("Error al leer el archivo. Asegúrate de que es un archivo .txt válido.")
        return cargar_texto_desde_archivo()
    # Excepto si no existe el fichero o no tiene los carácteres Unicode, salta a cargar el texto.

def guardar_texto_en_archivo(texto):
    nombre = input("Introduce el nombre del archivo donde guardar el texto (con .txt): ")
    if not nombre.endswith(".txt"):
        print("El archivo debe terminar en .txt")
        return guardar_texto_en_archivo(texto)
    # Si no acaba con .txt salta error
    try:
        with open(nombre, "w", encoding="utf-8") as f:
            f.write(texto)
        print(f"Texto guardado correctamente en '{nombre}'.")
    except Exception as e:
        print("Error al guardar el archivo:", e)
    # Intenta escribir el texto en el archivo, excepto si salta una excepción y muestra el mensaje de error.

def menu_entrada_texto():
    linea()
    print("-" * 4 + "TIPO DE TEXTO" + "-" * 4)
    print("1. Introducir texto manualmente")
    print("2. Cargar texto desde archivo")
    linea()
    opcion = pedir_opcion(1, 2)
    if opcion == 1:
        return pedir_texto()
    else:
        return cargar_texto_desde_archivo()

def menu_principal():
    texto = menu_entrada_texto()
    while True:
        linea()
        print("-" * 4 + "MENÚ" + "-" * 4)
        print("1. Contar Palabras. ")
        print("2. Contar Carácteres. ")
        print("3. Contar Frases. ")
        print("4. Buscar una Palabra. ")
        print("5. Palabras más frecuentes. ")
        print("6. Análisis completo. ")
        print("7. Cambiar el texto. ")
        print("8. Guardar texto en archivo")
        print("9. Salir")
        linea()

        opcion = pedir_opcion(1, 9)
        if opcion == 1:
            linea()
            print("Has elegido Contar Palabras ")
            palabras = contar_palabras(texto)
            print (f"El texto tiene : {palabras} palabras.")
            linea()
        elif opcion == 2:
            linea()
            print("Has elegido la opción Contar Carácteres ")
            print(f"Se han encontrado {contar_caracteres(texto)} caracteres en el texto.")
            linea()
        elif opcion == 3:
            linea()
            print("Has elegido la opción Contar Frases ")
            print (f"Se han encontrado un total de : {contar_frase(texto)} frases en el texto.")
            linea()
        elif opcion == 4:
            linea()
            print ("Has elegido la opción Buscar Palabra ")
            palabra = pedir_palabra(texto)
            print (f"La palabra : {palabra} se ha encontrado un total de : {buscar_palabras(texto,palabra.upper())} veces")
            linea()
        elif opcion == 5:
            linea()
            print ("Has elegido la opción Palabras Frecuentes ")
            palabras = palabras_mas_frecuentes(texto,pedir_frecuencia())
            print (palabras)
            linea()
        elif opcion == 6:
            linea()
            print ("Has elegido la opción Análisis Completo ")
            print (analisis_completo(texto))
            linea()
        elif opcion == 7:
            texto = menu_entrada_texto()
        elif opcion == 8:
            linea()
            print("Has elegido guardar el texto en un archivo.")
            guardar_texto_en_archivo(texto)
            linea()
        elif opcion == 9:
            print("Bye Bye...")
            break

def main():
    menu_principal()
main()
