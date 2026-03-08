# Fichero donde se presentan los distintos partidos políticos.

class Partido:
    def __init__(self,nombre,corriente,popularidad):
        self.nombre = nombre
        self.corriente = corriente
        self.popularidad = popularidad

    def __str__(self):
        return f"El partido con nombre {self.nombre} tiene corriente {self.corriente} con una popularidad de {self.popularidad} votantes."

    def aumentar_popularidad(self,n):
        if not isinstance(n,int):
            print (f"Dato incorrecto, vuelve a intentarlo.")
            return
        print (f"Se ha aumentado la popularidad del partido {self.nombre} de {self.popularidad} a {self.popularidad + n}")
        self.popularidad = self.popularidad + n

    def cambiar_dato(self,dato):
        opcion = input("N -> Nombre, C -> Corriente, P -> Popularidad : \n")
        while opcion.upper not in "NCP":
            print("Introduce una opción correcta.")
            opcion = input("N -> Nombre, C -> Corriente, P -> Popularidad : \n")
        if opcion.upper == "N":
            while dato == "":
                dato = input("Introduce un nombre válido : \n")
            self.nombre = dato
        elif opcion.upper == "C":
            while dato == "":
                print ("Introduce una corriente válida.")
                dato = input(f"Introduce la corriente nueva del partido {self.nombre} : \n")
            self.corriente = dato
        else :
            while dato <= 0 or dato.isdigit():
                print ("Introduce una popularidad válida (Mayor que 0) ")
                dato = int(input(f"Introduce el número de votantes que tiene el partido {self.nombre} : \n"))
            self.popularidad = dato

# Creamos la clase base, que tiene las funciones necesarias para funcionar.

class Ciudad:
    def __init__(self,localidad):
        self.localidad = localidad
        self.partidos = []

    def __str__(self):
        resultado = f"Ciudad: {self.localidad}\nPartidos:\n"
        cant_partidos = 0
        if not self.partidos:
            resultado += "  No hay partidos registrados.\n"
        else:
            for partido in self.partidos:
                cant_partidos += 1
                resultado += f"[{cant_partidos}] -> {partido.nombre} ({partido.corriente}) con {partido.popularidad} votantes.\n"
        return resultado
# Creamos un str algo más largo, pero con un string que tiene el resultado del str.

    def meter_partido(self,partido):
        return self.partidos.append(partido)

    def mostrar_ciudades(self):
        print (f"En la localidad {self.localidad}, están los partidos :")
        cant_partidos = 0
        for i in range(len(self.partidos)):
            cant_partidos += 1
            print (f"[{cant_partidos}] -> {self.partidos[i]}")

    def partido_popular(self):
        max_popularidad = None
        partido_max = None
        for i in range(len(self.partidos)):
            if max_popularidad is None or max_popularidad < self.partidos[i].popularidad:
                max_popularidad = self.partidos[i].popularidad
                partido_max = self.partidos[i]
        return self.localidad,partido_max
# Mediante unas funciones algo más útiles, creamos una ciudad consistente de una localidad y unos partidos.

class Pais:
    def __init__(self,nombre):
        self.nombre = nombre
        self.ciudades = []

    def __str__(self):
        resultado = f"País: {self.nombre}\nCiudades:\n"
        cant_ciudades = 0
        if not self.ciudades:
            resultado += "  No hay ciudades registradas.\n"
        else:
            for ciudad in self.ciudades:
                cant_ciudades += 1
                resultado += f"[{cant_ciudades}] -> Ciudad: {ciudad.localidad}\nPartidos:\n"
                cant_partidos = 0
                if not ciudad.partidos:
                    resultado += "   No hay partidos registrados.\n"
                else:
                    for partido in ciudad.partidos:
                        cant_partidos += 1
                        resultado += f"   [{cant_partidos}] -> {partido.nombre} ({partido.corriente}) con {partido.popularidad} votantes.\n"
        return resultado
# Un str algo más complejo, pero con la misma idea, con el detalle de unos espacios para que se vea más estético.

    def mostrar_ciudad(self):
        cont_ciudades = 0
        for i in range(len(self.ciudades)):
            cont_ciudades += 1
            print (f"[{cont_ciudades}] -> {self.ciudades[i]}")

    def ciudad_popular(self):
        max_popularidad = 0
        max_ciudad = None
        max_partido = None
        for ciudad in self.ciudades:
            nombre_ciudad, partido = ciudad.partido_popular()
            if partido.popularidad > max_popularidad:
                max_popularidad = partido.popularidad
                max_ciudad = nombre_ciudad
                max_partido = partido
        return max_ciudad, max_partido

    def informe(self):
        resultado = f"Informe del país -> {self.nombre}\n"
        resultado += f"Número de ciudades -> {len(self.ciudades)}\n\n"
        if not self.ciudades:
            resultado += "No hay ciudades registradas.\n"
            return resultado
        for ciudad in self.ciudades:
            resultado += f"Ciudad: {ciudad.localidad}\n"
            if not ciudad.partidos:
                resultado += "  No hay partidos registrados.\n"
            else:
                for partido in ciudad.partidos:
                    resultado += f"  - {partido.nombre} ({partido.corriente}): {partido.popularidad} votantes.\n"
            _, partido_max = ciudad.partido_popular()
            if partido_max:
                resultado += f"  Partido más popular de la ciudad: {partido_max.nombre} con {partido_max.popularidad} votantes.\n"
            resultado += "\n"
        ciudad_top, partido_top = self.ciudad_popular()
        if ciudad_top and partido_top:
            resultado += f"Ciudad con el partido más popular del país -> {ciudad_top}\n"
            resultado += f"Partido más popular del país: {partido_top.nombre} ({partido_top.popularidad} votantes.)\n"
        return resultado
# La clase pais junta las clases con unas funciones muy interesantes.
