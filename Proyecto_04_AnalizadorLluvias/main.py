from lluvia import *
def sep():
    print("-" * 40)
def main():
    ruta = "datos/lluvias.txt"
    lista_lluvias = obtener_clase(ruta)
    max_lluvia, max_loc = lluvia_maxima(lista_lluvias)
    med_lluvia = media_lluvias(lista_lluvias)
    temp_min, min_loc = temp_minima(lista_lluvias)
    temp_medi = temp_media(lista_lluvias)
    lista_ordenada = ranking_lluvias(lista_lluvias)
    while True:
        sep()
        print("-" * 4 + " MENÚ DE OPCIONES " + "-" * 4)
        print("1. Mostrar lluvia máxima")
        print("2. Mostrar media de lluvias")
        print("3. Mostrar temperatura mínima")
        print("4. Mostrar media de temperaturas")
        print("5. Mostrar ranking de lluvias")
        print("6. Mostrar informe completo")
        print("7. Salir")
        sep()
        opcion = input("Elige una opción: ")
        if not opcion.isdigit():
            sep()
            print("Introduce un número válido.")
            sep()
            continue
        if opcion == "1":
            sep()
            print(f"La lluvia máxima es {max_lluvia} mm en {max_loc}")
            sep()
        elif opcion == "2":
            sep()
            print(f"La media de lluvias es {med_lluvia} mm")
            sep()
        elif opcion == "3":
            sep()
            print(f"La temperatura mínima es {temp_min} grados en {min_loc}")
            sep()
        elif opcion == "4":
            sep()
            print(f"La media de temperaturas es {temp_medi} grados")
            sep()
        elif opcion == "5":
            sep()
            mostrar_ranking(lista_ordenada)
            sep()
        elif opcion == "6":
            sep()
            informe(max_lluvia, max_loc, med_lluvia, temp_min, min_loc, temp_medi)
            sep()
        elif opcion == "7":
            sep()
            print("Saliendo del programa...")
            sep()
            break
        else:
            sep()
            print("Opción no válida. Intenta de nuevo.")
            sep()
if __name__ == "__main__":
    main()
