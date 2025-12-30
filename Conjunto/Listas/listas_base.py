def linea():
    print(" - " * 40)

def añadir(lista):
    elem = input("Introduce el elemento a añadir: ")
    lista.append(elem)
    print(f"Elemento '{elem}' añadido.")

def mostrar(lista):
    if not lista:
        print("No hay elementos.")
    else:
        for i, elem in enumerate(lista, start=1):
            print(f"{i}. {elem}")

def buscar(lista):
    valor = input("Introduce el elemento a buscar: ")
    for elem in lista:
        if elem.lower() == valor.lower():
            print(f"Elemento encontrado: {elem}")
            return elem
    print("Elemento no encontrado.")
    return None

def eliminar(lista):
    valor = input("Introduce el elemento a eliminar: ")
    if valor in lista:
        lista.remove(valor)
        print(f"Elemento '{valor}' eliminado.")
    else:
        print("No existe ese elemento.")

def editar(lista):
    viejo = input("Introduce el elemento a editar: ")
    if viejo in lista:
        nuevo = input("Introduce el nuevo valor: ")
        idx = lista.index(viejo)
        lista[idx] = nuevo
        print("Elemento actualizado.")
    else:
        print("No existe ese elemento.")