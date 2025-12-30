import json

# -------- TXT --------

def guardar_txt(ruta, lista_lineas):
    """Guarda una lista de líneas en un archivo TXT."""
    with open(ruta, "w", encoding="utf-8") as f:
        for linea in lista_lineas:
            f.write(str(linea) + "\n")

def leer_txt(ruta):
    """Lee un archivo TXT y devuelve una lista de líneas."""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return [linea.strip() for linea in f.readlines()]
    except FileNotFoundError:
        return []

# -------- JSON --------

def guardar_json(ruta, datos):
    """Guarda datos en formato JSON."""
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def cargar_json(ruta):
    """Carga datos desde un archivo JSON."""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

# -------- CSV --------

def guardar_csv(ruta, lista_filas):
    """Guarda una lista de listas en un archivo CSV."""
    with open(ruta, "w", encoding="utf-8") as f:
        for fila in lista_filas:
            f.write(",".join(map(str, fila)) + "\n")

def cargar_csv(ruta):
    """Carga un archivo CSV y devuelve una lista de listas."""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return [linea.strip().split(",") for linea in f.readlines()]
    except FileNotFoundError:
        return []
