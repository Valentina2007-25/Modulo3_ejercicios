from ejercicio_8_Transformación_Datos import palabras_mayusculas, longitudes

def test_palabras_mayusculas():
    esperado = ["PYTHON", "PROGRAMACION", "EXTENSO", "APRENDIZAJE."]
    assert palabras_mayusculas == esperado

def test_longitudes():
    esperado = {
        "PYTHON": 6,
        "PROGRAMACION": 12,
        "EXTENSO": 7,
        "APRENDIZAJE.": 12
    }
    assert longitudes == esperado
