# Fichero que crea la clase libro y los métodos que tiene.
class Libro:
    def __init__(self, titulo, autor, año, isbn, prestado=False):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.isbn = isbn
        self.prestado = prestado
    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"{self.titulo} — {self.autor} ({self.año}) | ISBN: {self.isbn} | {estado}"
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"Se ha prestado el libro con título {self.titulo}.")
        else:
            print(f"No se puede prestar un libro que ya está prestado.")
    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"El libro con título {self.titulo} se ha devuelto.")
        else:
            print(f"No se puede devolver un libro que no está prestado.")
    def mostrar_info(self):
        print (f" Título -> [{self.titulo}]")
        print (f" Autor ->  [{self.autor}]")
        print (f" Año   -> [{self.año}]")
        print (f" ISBN  -> [{self.isbn}]")
        if self.prestado:
            print (f" Estado -> [Prestado]")
        else:
            print (f" Estado -> [No Prestado]")
    @staticmethod
    def from_linea(linea):
        titulo, autor, año, isbn, prestado = linea.strip().split(",")
        return Libro(titulo, autor, int(año), isbn, prestado == "True")
    def to_linea(self):
        return f"{self.titulo},{self.autor},{self.año},{self.isbn},{self.prestado}"
