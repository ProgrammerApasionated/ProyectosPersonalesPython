# En este archivo vamos a crear los diferentes métodos que necesita tener un estudiante en este programa.

class Estudiante:
    def __init__(self,dni,nombre,correo):
        self.dni    = dni
        self.nombre = nombre
        self.correo = correo
        self.notas = {}
    def __str__(self):
        return f"El estudiante con nombre {self.nombre} dni {self.dni} y correo {self.correo} tiene estas notas {self.notas}"
    def agregar_notas(self, codigo_asig, nota):
        self.notas[codigo_asig] = nota
    def modificar_nota(self,codigo_asig, n_nota):
        if codigo_asig in self.notas:
            self.notas[codigo_asig] = n_nota
            print (f"Se ha modificado el valor de {codigo_asig} a {n_nota}")
        else :
            print (f"La asignatura {codigo_asig} no existe para el estudiante {self.nombre}")
    def eliminar_asignatura(self,codigo_asig):
        if codigo_asig in self.notas:
            nota_el = self.notas[codigo_asig]
            del self.notas[codigo_asig]
            print(f"Se ha eliminado la asignatura {codigo_asig} con nota {nota_el}")
        else :
            print (f"Esta asignatura {codigo_asig} no está en el estudiante {self.nombre}")
    def calcular_medias(self):
        if not self.notas:
            return None
        else:
            media = sum(self.notas.values()) / len(self.notas)
            return media
