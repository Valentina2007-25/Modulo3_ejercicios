from ejercicio_7_FiltradoEstudiantes import estudiantes_aprobados

def test_estudiantes_aprobados():
    esperado = [("Ana", 4.5), ("Maria", 3.9), ("Sofia", 3.2)]
    assert estudiantes_aprobados == esperado
