# Archivo donde se definen las funciones que se utilizan en el main.

def limpiar_texto(texto): # Limpia el formato del texto, haciéndolo legible, solo caracteres + primera letra mayúscula.
    texto_limpio = ""
    for caracter in texto:
        if caracter.isalpha() or caracter.isspace():
            texto_limpio += caracter
    return texto_limpio.upper()
    # Recorremos cada carácter y lo metemos a una variable auxiliar.

def contar_palabras(texto):  # Cuenta las palabras del texto.
    texto_correcto = limpiar_texto(texto).split()
    # Si la lista está vacía, no hay palabras
    return len(texto_correcto)

def palabras_mas_frecuentes(texto,n): # Devuelve un diccionario con las palabras que se repiten más de n veces.
    texto_limpio = limpiar_texto(texto).lower()
    lista_texto = texto_limpio.split()
    frecuencias = {}
    # Limpiamos el texto y lo partimos en una lista con strip.
    for palabra in lista_texto:
        if palabra not in frecuencias:
            frecuencias[palabra] = 1
        else :
            frecuencias[palabra] += 1
    # Recorremos las palabras de la lista y si ya están añadimos 1 a la clave de su diccionario.
    lista_ordenada = sorted(frecuencias.items(),key=lambda x:x[1],reverse=True)
    return lista_ordenada[:n]
    # Y al final devuelve una lista con las n palabras que más se repiten en el texto.

def contar_caracteres(texto): # Cuenta la cantidad de carácteres sin espacios que hay en ese texto.
    texto_bien = limpiar_texto(texto)
    total_carac = 0
    for caracter in texto_bien:
        if caracter.isalpha():
            total_carac += 1
    return total_carac
    # O la simple, solo return len(texto_bien), que devuelve tanto carácteres como espacios.

def buscar_palabras(texto,palabra): # Cuenta la cantidad de repetición que hay de una palabra en un texto.
    texto_cor = limpiar_texto(texto)
    lista_texto = texto_cor.split()
    repeticiones = 0
    palabra = palabra.upper()
    for palabra2 in lista_texto:
        if palabra == palabra2:
            repeticiones += 1
    return repeticiones

def contar_frase(texto): # Cuenta las frases que hay en un texto, suponiendo que una frase acaba con "." o "!" o "?" o "¿".
    cant_puntuacion = 0
    for caracter in texto:
        if caracter in ".!?¿":
            cant_puntuacion += 1
    return cant_puntuacion

def analisis_completo(texto): # Función que junta todas las anteriores en una como un "informe" y hace un resumen de todas.
    analisis = {"Palabras": contar_palabras(texto), "Carácteres": contar_caracteres(texto),
                "Cantidad Frases": contar_frase(texto), "Top 5": palabras_mas_frecuentes(texto, 5)}
    return analisis