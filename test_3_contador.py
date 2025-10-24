from Ejercicio_3_contador_Llamadas import crear_contador


def test_contadores_independientes():
    contador1 = crear_contador()
    contador2 = crear_contador()

    # Verificar que ambos comienzan desde 1
    assert contador1() == 1
    assert contador2() == 1

    # contador1 avanza sin afectar al contador2
    assert contador1() == 2
    assert contador1() == 3
    assert contador2() == 2


def test_incremento_continuo():
    contador = crear_contador()

    # Comprobar que el conteo es consecutivo
    assert contador() == 1
    assert contador() == 2
    assert contador() == 3
    assert contador() == 4


def test_reinicio_independiente():
    contador_a = crear_contador()
    contador_b = crear_contador()

    # contador_a avanza
    assert contador_a() == 1
    assert contador_a() == 2

    # contador_b no se afecta
    assert contador_b() == 1
    assert contador_b() == 2  # esta mal
