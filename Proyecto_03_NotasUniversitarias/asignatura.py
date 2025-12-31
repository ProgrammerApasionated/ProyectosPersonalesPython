

class Asignatura:
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo.upper()
        self.nombre = nombre
        self.creditos = creditos

    def __str__(self):
        return f"{self.codigo} - {self.nombre} ({self.creditos} créditos)"
    def mostrar_info(self):
        print (f"Código:   {self.codigo}")
        print (f"Nombre:   {self.nombre}")
        print (f"Créditos: {self.creditos}")

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "creditos": self.creditos
        }

    def validar_codigo(self, codigo):
        # Válida que el código de la asignatura tenga esta estructura.
        # 3 Carácteres en Mayúsculas + 3 Números.
        if len(codigo) != 6:
            # No tiene 6 carácteres.
            return False
        # Necesitamos que estén em mayúsculas.
        codigo = codigo.upper()
        primera_parte = codigo[:3]
        segunda_parte = codigo[3:]
        if not primera_parte.isalpha():
            # No tiene letras los 3 primeros índices.
            return False
        if not segunda_parte.isdigit():
            # No tiene dígitos los 3 últimos índices.
            return False
        return True
