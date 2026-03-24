class Producto:
    def __init__(self,nombre,cantidad,precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    # Creamos una clase objeto con los siguientes atributos.
    # nombre -> Identificador del producto, cantidad -> Cantidad del producto, precio -> Coste del producto.
    def __str__(self):
        return f"Identificador del producto {self.nombre} cantidad de {self.cantidad} unidades con un precio de {self.precio} euros."
class Tienda:
    def __init__(self,empleado,localidad):
        self.empleado = empleado
        self.localidad = localidad
        self.productos = []
    # Creamos una clase tienda.
    # empleado -> Nombre de la persona encargada, localidad -> Zona geográfica de la tienda, productos -> Lista de objetos tipo producto.
    def __str__(self):
        # Con la inspiración del Proyecto_08_SistemaVotaciones, concretamente el str de la clase ciudad.
        resultado = f"El empleado {self.empleado} trabaja en la localidad {self.localidad} con : \n"
        cant_productos = 0
        if not self.productos :
            resultado += "No hay productos en la localidad"
        else :
            for p in self.productos:
                cant_productos += 1
                resultado += f"Identificador del producto -> [{p.nombre}]\n"
                resultado += f"Con una cantidad de -> [{p.cantidad}]\n"
                resultado += f"Coste de -> [{p.precio}]\n"
        resultado += f"Cantidad total = {cant_productos}"
        return resultado
        # Creamos un String, con la información de la clase tienda, y con la información de la lista de productos.
    def meter_producto(self,p):
        self.productos.append(p)
    def producto_abundante(self):
        max_cant = None
        max_producto = None
        for p in self.productos:
            if max_cant is None or p.cantidad > max_cant:
                max_cant = p.cantidad
                max_producto = p.nombre
        return max_cant, max_producto
