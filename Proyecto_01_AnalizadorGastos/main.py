from gastos import *
from categorias import clasificar_gastos
def main():
    ruta = "datos/gastos.txt"
    lista_gastos = leer_gastos(ruta)
    clasificar_gastos(lista_gastos)
    totales = calcular_totales(lista_gastos)
    print ("-" * 40)
    maximo = gasto_maximo(lista_gastos)
    minimo = gasto_minimo(lista_gastos)
    media = gasto_medio(lista_gastos)
    mostrar_resumen(totales, maximo, minimo, media)
    print ("-" * 40)
if __name__ == "__main__":
    main()
