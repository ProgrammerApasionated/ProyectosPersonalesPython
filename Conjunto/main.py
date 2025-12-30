from Menus.menu_base import menu_principal
from Estadisticas.estadisticas_base import resumen
from Listas.listas_base import mostrar
from BaseClases.base_sistema_dual import SistemaCompleto

def main():
    print("Bienvenido al sistema de Álvaro.")
    print("Inicializando módulos...")
    sistema = SistemaCompleto()
    sistema.menu()

if __name__ == "__main__":
    main()
main()