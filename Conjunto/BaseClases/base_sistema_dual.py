def linea():
    print("-" * 40)

class Entidad:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

    def __str__(self):
        return f"{self.nombre} -> {self.valor}"

class GrupoEntidades:
    def __init__(self):
        self.lista = []

    def añadir(self, entidad):
        self.lista.append(entidad)
        print(f"'{entidad.nombre}' añadido.")

    def mostrar(self):
        if not self.lista:
            print("No hay elementos.")
        else:
            for i, ent in enumerate(self.lista, start=1):
                print(f"{i}. {ent}")

    def buscar(self):
        nombre = input("Introduce el nombre a buscar: ").title()
        for ent in self.lista:
            if ent.nombre == nombre:
                print(ent)
                return ent
        print("No encontrado.")
        return None

class Sistema:
    def __init__(self):
        self.grupo = GrupoEntidades()

    def menu(self):
        while True:
            linea()
            print("-------- MENÚ SISTEMA --------")
            print("1.- Añadir entidad")
            print("2.- Mostrar entidades")
            print("3.- Buscar entidad")
            print("4.- Salir")
            linea()

            opcion = input("Introduce la opción deseada: ")

            if opcion == "1":
                linea()
                self.añadir_entidad()
                linea()
            elif opcion == "2":
                linea()
                self.grupo.mostrar()
                linea()
            elif opcion == "3":
                linea()
                self.grupo.buscar()
                linea()
            elif opcion == "4":
                print("Bye Bye...")
                break
            else:
                print("Opción inválida.")

    def añadir_entidad(self):
        nombre = input("Introduce el nombre: ")
        valor = input("Introduce el valor: ")
        nueva = Entidad(nombre, valor)
        self.grupo.añadir(nueva)

def main():
    sistema = Sistema()
    sistema.menu()

main()
