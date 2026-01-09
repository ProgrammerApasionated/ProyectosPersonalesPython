def obtener_lista_temperaturas():
    lista_temperaturas = []
    cadena = input("Introduce la temperatura (cadena vacía para terminar): ")
    temperatura = None
    while cadena != "":
        while True:
            try:
                temperatura = float(cadena)
                break
            except ValueError:
                cadena = input("Valor no válido, introduce una temperatura correcta: \n")
                if cadena == "":
                    break
        if cadena == "":
            break
        lista_temperaturas.append(temperatura)
        cadena = input("Introduce la temperatura (cadena vacía para terminar): ")
    return lista_temperaturas

def eliminar_una_temperatura(lista_temperaturas):
    valor = int (input ("Introduce el valor a borrar  "))
    i = 0
    while i < len(lista_temperaturas):
        if lista_temperaturas[i] == valor :
            opcion = input (f"Quieres que elimine el valor {valor} (S/N) ")
            if opcion == "S":
                lista_temperaturas.remove(valor)
                print (f"La lista modificada ha quedado así {lista_temperaturas}")
            else :
                print (f"El elemento {valor} no se ha eliminado de la lista de temperaturas ")
            break
        i += 1
    return lista_temperaturas

def media_temperaturas(listas_temperaturas):
    suma_total_temperaturas = 0
    for temperaturas in listas_temperaturas:
        suma_total_temperaturas += temperaturas
    media_total = suma_total_temperaturas / len(listas_temperaturas)
    return round(media_total,2)
def maxima_temperatura(lista_temperaturas):
    temperatura_maxima = lista_temperaturas[0]
    for maxima in lista_temperaturas:
        if maxima > temperatura_maxima:
            temperatura_maxima = maxima
    return temperatura_maxima

def minima_temperatura(lista_temperaturas):
    temperatura_minima = lista_temperaturas[0]
    for minima in lista_temperaturas:
        if minima < temperatura_minima:
            temperatura_minima = minima
    return temperatura_minima

def temperaturas_negativas(lista_temperaturas):
    lista_temperaturas_negativas = []
    for negativa in lista_temperaturas:
        if negativa < 0:
            lista_temperaturas_negativas.append(negativa)
    return lista_temperaturas_negativas

def racha_de_ola_de_frio(lista_temperaturas):
    inicio = -1
    longitud = 0
    mayor_inicio = -1
    mayor_longitud = 0
    mayor_final = -1
    i = 0
    while i < len(lista_temperaturas):
        if lista_temperaturas[i] < 0:
            if longitud == 0:
                inicio = i
            longitud += 1
        else:
            if longitud > mayor_longitud:
                mayor_longitud = longitud
                mayor_inicio = inicio
                mayor_final = i - 1
            longitud = 0
        i += 1
    if longitud > mayor_longitud:
        mayor_longitud = longitud
        mayor_inicio = inicio
        mayor_final = i - 1
    if mayor_longitud == 0:
        return 0, None, None
    return mayor_longitud, mayor_inicio, mayor_final

def informe(lista_temp):
    media = media_temperaturas(lista_temp)
    media = round(media,2)
    temp_max = maxima_temperatura(lista_temp)
    temp_min = minima_temperatura(lista_temp)
    long_max, may_inc, may_fin = racha_de_ola_de_frio(lista_temp)
    print (f"La media de temperaturas ha sido de {media}.")
    print (f"La temperatura máxima ha sido de {temp_max} grados y la mínima de {temp_min} grados.")
    if long_max == 0:
        print("No ha habido ninguna ola de frío.")
    else:
        print(f"La racha de frío ha empezado el {may_inc} y ha acabado el {may_fin} con una longitud de {long_max}.")

def cargar_temperaturas_desde_fichero(nombre_fichero="temperaturas.txt"):
    lista = []
    ruta = f"../data/{nombre_fichero}"
    try:
        with open(ruta, "r") as f:
            for linea in f:
                linea = linea.strip()
                if linea != "":
                    lista.append(int(linea))
    except FileNotFoundError:
        print(f"No existe el fichero '{ruta}'.")
    return lista

def guardar_temperaturas_en_fichero(lista, nombre_fichero="temperaturas.txt"):
    ruta = f"../data/{nombre_fichero}"
    with open(ruta, "w") as f:
        for temp in lista:
            f.write(f"{temp}\n")
    print(f"Temperaturas guardadas en '{ruta}'.")

def line():
    print ("-" * 40)

def menu(lista_temp):
    while True:
        line()
        print ("1.- Eliminar una temperatura.")
        print ("2.- Media temperatura")
        print ("3.- Max/Min temperatura.")
        print ("4.- Temperaturas negativas.")
        print ("5.- Racha temperaturas negativas.")
        print ("6.- Informe.")
        print ("7.- Cargar lista desde fichero (sobrescribe la actual)")
        print ("8.- Guardar lista y salir. ")
        print ("9.- Mostrar lista actual.")
        line()
        op = input ("Introduce la opción deseada \n")
        if op == "1":
            line()
            eliminar_una_temperatura(lista_temp)
            line()
        elif op == "2":
            line()
            media = media_temperaturas(lista_temp)
            print (f"La media es de {media} grados.")
            line()
        elif op == "3":
            elegir = input ("Introduce la opción deseada Max/Min \n")
            while elegir not in ["Max","Min"]:
                elegir = input ("Introduce una opción válida, (Max o Min) \n")
            if elegir == "Max":
                line()
                max_ = maxima_temperatura(lista_temp)
                print (f"La temperatura máxima ha sido de {max_} grados.")
                line()
            else:
                line()
                min_ = minima_temperatura(lista_temp)
                print (f"La temperatura mínima ha sido de {min_} grados.")
                line()
        elif op == "4":
            line()
            neg = temperaturas_negativas(lista_temp)
            print(f"Temperaturas negativas: {neg}")
            line()
        elif op == "5":
            line()
            long_, ini, fin = racha_de_ola_de_frio(lista_temp)
            if long_ == 0:
                print("No ha habido ola de frío.")
            else:
                print(f"Ola de frío de {long_} días, desde {ini} hasta {fin}.")
            line()
        elif op == "6":
            line()
            informe(lista_temp)
            line()
        elif op == "7":
            line()
            print("Cargando temperaturas desde fichero (esto reemplaza la lista actual)...")
            lista_temp = cargar_temperaturas_desde_fichero()
            print("Temperaturas cargadas:", lista_temp)
            line()
        elif op == "8":
            line()
            guardar_temperaturas_en_fichero(lista_temp)
            print("Lista guardada. Saliendo...")
            line()
            break
        elif op == "9":
            print (lista_temp)
        else :
            print ("Opción incorrecta, vuelve a intentarlo.")

def main():
    print("¿Cómo quieres cargar las temperaturas?")
    print("1. Introducir manualmente")
    print("2. Cargar desde fichero")
    opc = input("Elige una opción: ")
    if opc == "2":
        lista_temp = cargar_temperaturas_desde_fichero()
        print("Temperaturas cargadas:", lista_temp)
    else:
        lista_temp = obtener_lista_temperaturas()
    menu(lista_temp)

if __name__ == "__main__":
    main()
