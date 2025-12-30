def pedir_entero(min_val=None, max_val=None):
    """Pide un entero válido dentro de un rango opcional."""
    entrada = input()
    while True:
        if entrada.isdigit():
            valor = int(entrada)
            if (min_val is None or valor >= min_val) and (max_val is None or valor <= max_val):
                return valor
        print("Entrada inválida. Intenta de nuevo:")
        entrada = input()

def pedir_float(min_val=None, max_val=None):
    """Pide un número decimal válido dentro de un rango opcional."""
    entrada = input()
    while True:
        try:
            valor = float(entrada)
            if (min_val is None or valor >= min_val) and (max_val is None or valor <= max_val):
                return valor
        except ValueError:
            pass
        print("Entrada inválida. Intenta de nuevo:")
        entrada = input()

def pedir_texto(obligatorio=True):
    """Pide texto, pudiendo exigir que no esté vacío."""
    texto = input().strip()
    while obligatorio and texto == "":
        print("Texto vacío. Introduce algo:")
        texto = input().strip()
    return texto

def pedir_opcion(lista_opciones):
    """Pide una opción dentro de una lista de opciones válidas."""
    opcion = input().strip().lower()
    opciones_validas = [op.lower() for op in lista_opciones]
    while opcion not in opciones_validas:
        print(f"Opción inválida. Opciones válidas: {lista_opciones}")
        opcion = input().strip().lower()
    return opcion

def pedir_confirmacion():
    """Devuelve True si el usuario confirma con 's'."""
    respuesta = input().strip().lower()
    while respuesta not in ["s", "n"]:
        print("Respuesta inválida. Escribe 's' o 'n':")
        respuesta = input().strip().lower()
    return respuesta == "s"
