def linea():
    print("-" * 40)

def media(lista):
    """Devuelve la media de una lista de números."""
    if not lista:
        return 0
    return sum(lista) / len(lista)

def maximo(lista):
    """Devuelve el valor máximo de una lista."""
    if not lista:
        return None
    return max(lista)

def minimo(lista):
    """Devuelve el valor mínimo de una lista."""
    if not lista:
        return None
    return min(lista)

def racha_aprobados(lista):
    """
    Calcula la racha más larga de números >= 5.
    Perfecto para notas o días con lluvia.
    """
    racha = 0
    max_racha = 0
    for n in lista:
        if n >= 5:
            racha += 1
            max_racha = max(max_racha, racha)
        else:
            racha = 0
    return max_racha

def contar_mayores(lista, valor):
    """Cuenta cuántos elementos son mayores que 'valor'."""
    return sum(1 for x in lista if x > valor)

def contar_menores(lista, valor):
    """Cuenta cuántos elementos son menores que 'valor'."""
    return sum(1 for x in lista if x < valor)

def porcentaje(parte, total):
    """Devuelve el porcentaje de 'parte' respecto a 'total'."""
    if total == 0:
        return 0
    return (parte / total) * 100

def resumen(lista):
    """Imprime un resumen estadístico completo."""
    linea()
    print("RESUMEN ESTADÍSTICO")
    linea()
    print(f"Datos: {lista}")
    print(f"Media: {media(lista):.2f}")
    print(f"Máximo: {maximo(lista)}")
    print(f"Mínimo: {minimo(lista)}")
    print(f"Racha >= 5: {racha_aprobados(lista)}")
    linea()
