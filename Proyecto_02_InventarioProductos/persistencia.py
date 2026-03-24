import json

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
