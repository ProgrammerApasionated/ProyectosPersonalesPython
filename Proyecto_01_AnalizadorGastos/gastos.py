# Archivo que tiene las características de los gastos.
class Gasto:
    def __init__(self, fecha, concepto, cantidad):
        self.fecha = fecha
        self.concepto = concepto
        self.cantidad = cantidad
        self.categoria = None

def leer_gastos(ruta):
    lista = []
    with open (ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            fecha, concepto, cantidad = linea.split(",")
            gasto = Gasto(fecha,concepto,float(cantidad))
            lista.append(gasto)
        return lista

def calcular_totales(lista_gastos):
    totales = {}
    for gasto in lista_gastos:
        categoria = gasto.categoria
        totales[categoria]=totales.get(categoria,0) + gasto.cantidad
    return totales
def gasto_maximo(lista_gastos):
    maximo = lista_gastos[0]
    for gasto in lista_gastos:
        if gasto.cantidad > maximo.cantidad:
            maximo = gasto
    return maximo

def gasto_minimo(lista_gastos):
    minimo = lista_gastos[0]
    for gasto in lista_gastos:
        if gasto.cantidad < minimo.cantidad:
            minimo = gasto
    return minimo

def gasto_medio(lista_gastos):
    suma = 0
    for gasto in lista_gastos:
        suma += gasto.cantidad
    return suma / len(lista_gastos)

def mostrar_resumen(totales, maximo, minimo, media):
    print ("-" * 10 + " Resumen de Gastos " + "-" * 10)
    for categoria, total in totales.items():
        print(f"{categoria}: {total:.2f} €")
    print ("-" * 40)
    print ("-" * 10 + " Estadísticas " + "-" * 10)
    print(f"Gasto máximo: {maximo.concepto} - {maximo.cantidad:.2f} €")
    print(f"Gasto mínimo: {minimo.concepto} - {minimo.cantidad:.2f} €")
    print(f"Gasto medio: {media:.2f} €")
