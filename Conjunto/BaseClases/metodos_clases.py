def linea():
    return "-" * 40
class Azul:
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return f"Color -> {self.color}"
class Colores:
    def __init__(self, gama):
        self.gama = gama
        self.colores = []
    def __str__(self):
        resultado = linea() + "\n"
        resultado += f"Gama: {self.gama}\n"
        resultado += "Colores registrados:\n"
        if not self.colores:
            resultado += "  (ninguno)\n"
        else:
            for i, color in enumerate(self.colores, start=1):
                resultado += f"  [{i}] {color}\n"
        resultado += linea()
        return resultado
# Inspirado del str usado en P8 -> candidato.py

