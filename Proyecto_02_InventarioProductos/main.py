from producto import *
from persistencia import guardar_json, cargar_json
RUTA_JSON = "datos/inventario.json"
def producto_a_dict(p):
    return {
        "nombre": p.nombre,
        "cantidad": p.cantidad,
        "precio": p.precio
    }
def dict_a_producto(d):
    return Producto(d["nombre"], d["cantidad"], d["precio"])
def cargar_productos_en_tienda(tienda):
    datos = cargar_json(RUTA_JSON)
    if datos:
        for d in datos:
            tienda.meter_producto(dict_a_producto(d))
def guardar_productos_de_tienda(tienda):
    datos = [producto_a_dict(p) for p in tienda.productos]
    guardar_json(RUTA_JSON, datos)
def linea():
    print("-" * 40)
def pedir_opcion(min_op, max_op):
    opcion = input("Introduce la opción deseada: ")
    while not opcion.isdigit() or not (min_op <= int(opcion) <= max_op):
        print("Opción inválida.")
        opcion = input("Introduce una opción válida: ")
    return int(opcion)
def menu_principal(tienda):
    while True:
        linea()
        print("-------- MENÚ PRINCIPAL --------")
        print("1.- Añadir producto")
        print("2.- Mostrar productos")
        print("3.- Producto más abundante")
        print("4.- Salir")
        linea()
        opcion = pedir_opcion(1, 4)
        if opcion == 1:
            linea()
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            tienda.meter_producto(Producto(nombre, cantidad, precio))
            guardar_productos_de_tienda(tienda)
            print("Producto añadido y guardado.")
            linea()
        elif opcion == 2:
            linea()
            print(tienda)
            linea()
        elif opcion == 3:
            linea()
            if tienda.productos:
                cantidad, nombre = tienda.producto_abundante()
                print(f"Producto más abundante: {nombre} ({cantidad} unidades)")
            else:
                print("No hay productos.")
            linea()
        elif opcion == 4:
            print("Bye Bye...")
            break
def main():
    tienda = Tienda("Azul", "Gandia")
    # Cargar productos desde JSON al iniciar
    cargar_productos_en_tienda(tienda)
    menu_principal(tienda)

main()
