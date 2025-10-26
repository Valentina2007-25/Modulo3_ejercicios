from ejercicio_4_Validador_Datos import aplicar_validador, es_email_valido, es_mayor_a_10

def test_es_email_valido():
    """Prueba la función que valida correos electrónicos."""
    assert es_email_valido("valentina@gmail.com") is True
    assert es_email_valido("usuario_sin_arroba") is False
    assert es_email_valido("correo@dominio.com") is True
    assert es_email_valido("correo.sin@punto") is False


def test_es_mayor_a_10():
    """Prueba la función que valida si un número es mayor a 10."""
    assert es_mayor_a_10(5) is False
    assert es_mayor_a_10(10) is False
    assert es_mayor_a_10(11) is True
    assert es_mayor_a_10(20) is True


def test_aplicar_validador_con_emails():
    """Verifica que aplicar_validador funcione correctamente con correos."""
    correos = ["a@gmail.com", "sin_arroba", "b@dominio.com"]
    resultado = aplicar_validador(correos, es_email_valido)
    assert resultado == ["a@gmail.com", "b@dominio.com"]


def test_aplicar_validador_con_numeros():
    """Verifica que aplicar_validador funcione correctamente con números."""
    numeros = [5, 12, 8, 20, 3, 15]
    resultado = aplicar_validador(numeros, es_mayor_a_10)
    assert resultado == [12, 20, 15]
