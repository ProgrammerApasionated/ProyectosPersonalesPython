def linea():
    print("-" * 40)

def pedir_opcion(min_op, max_op):
    opcion = input("Introduce la opción deseada: ")
    while not opcion.isdigit() or not (min_op <= int(opcion) <= max_op):
        print("Opción inválida.")
        opcion = input("Introduce una opción válida: ")
    return int(opcion)

def menu_principal():
    while True:
        linea()
        print("-------- MENÚ PRINCIPAL --------")
        print("1.- Opción A")
        print("2.- Opción B")
        print("3.- Opción C")
        print("4.- Salir")
        linea()

        opcion = pedir_opcion(1, 4)

        if opcion == 1:
            linea()
            print("Has elegido la opción A.")
            linea()
        elif opcion == 2:
            linea()
            print("Has elegido la opción B.")
            linea()
        elif opcion == 3:
            linea()
            print("Has elegido la opción C.")
            linea()
        elif opcion == 4:
            print("Bye Bye...")
            break

def main():
    menu_principal()

main()
