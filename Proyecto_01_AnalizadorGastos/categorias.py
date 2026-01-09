# Clasificación de las categorias por clave.
def palabras_clave_por_categoria():
    return {
        "Comida": ["super", "mercadona", "pizza", "restaurante", "bar"],
        "Transporte": ["bus", "metro", "gasolina", "uber"],
        "Ocio": ["cine", "netflix", "spotify", "juego"],
        "Hogar": ["luz", "agua", "internet", "muebles"],
    }
def clasificar_gasto(gasto):
    categorias = palabras_clave_por_categoria()
    concepto = gasto.concepto.lower()
    for categoria, claves in categorias.items():
        for palabra in claves:
            if palabra in concepto:
                gasto.categoria = categoria
                return
    gasto.categoria = "Desconocido"

def clasificar_gastos(lista_gastos):
    for gasto in lista_gastos:
        clasificar_gasto(gasto)
