# Inicializamos las características que tienen las lluvias.
class Precipitaciones:
    def __init__(self,cantidad,localidad,temperatura):
        self.cantidad = cantidad
        self.localidad = localidad
        self.temperatura = temperatura
def obtener_clase(ruta):
    lista = []
    with open (ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            cant, local,temp = linea.split("#")
            clase = Precipitaciones (float(cant),local,float(temp))
            lista.append(clase)
    return lista
def lluvia_maxima(lista_lluvias):
    max_lluvia = None
    max_local = None
    for lluvia in lista_lluvias:
        if max_lluvia is None or lluvia.cantidad > max_lluvia:
            max_lluvia = lluvia.cantidad
            max_local = lluvia.localidad
    return max_lluvia, max_local
def media_lluvias(lista_lluvia):
    media = 0
    cant_localidades = 0
    for lluvia in lista_lluvia:
        cant_localidades += 1
        media += lluvia.cantidad
    media = media / cant_localidades
    return round(media,2)
def temp_minima(lista_objetos):
    temp_min = None
    localidad_min = None
    for temperatura in lista_objetos:
        if temp_min is None or temperatura.temperatura < temp_min:
            temp_min = temperatura.temperatura
            localidad_min = temperatura.localidad
    return temp_min, localidad_min
def temp_media(lista_obje):
    media = 0
    cant_localidades = 0
    for temperatura in lista_obje:
        cant_localidades += 1
        media += temperatura.temperatura
    media = media / cant_localidades
    return round(media,2)
def ranking_lluvias(lista_objetos):
    lista_ordenada = sorted(lista_objetos, key=lambda x: x.cantidad, reverse=True)
    return lista_ordenada
def mostrar_ranking(lista_ordenada):
    print("\n--- Ranking de Lluvias ---")
    posicion = 1
    for obj in lista_ordenada:
        print(f"{posicion}. {obj.localidad} – {obj.cantidad} mm")
        posicion += 1

def informe(maxim_lluvia,loc_max_lluvia,media_lluvia,minim_temp,loc_min_temp,media_temp):
    print ("-" * 4 + " Resumen de Lluvias " + "-" * 4)
    print (f"La máxima lluvia ha sido de {maxim_lluvia} mm en la localidad de {loc_max_lluvia}")
    print (f"La temperatura mínima ha sido de {minim_temp} grados en la ciudad de {loc_min_temp}")
    print (f"La media de lluvias en todas las localidad ha sido de {media_lluvia} mm")
    print (f"La media de temperaturas ha sido de {media_temp} grados")