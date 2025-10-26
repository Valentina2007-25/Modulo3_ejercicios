import ejercicio_5_Calculadora_Impuestos # en lugar de importar cada función por separado

def test_calcular_iva_con_tasa_inicial():
    """Verifica que calcular_iva use correctamente la tasa inicial (0.19)."""
    precio = 100000
    esperado = precio * 0.19
    assert ejercicio_5_Calculadora_Impuestos.calcular_iva(precio) == esperado


def test_actualizar_tasa_iva_cambia_valor_global():
    """Prueba que actualizar_tasa_iva modifique correctamente la tasa global."""
    ejercicio_5_Calculadora_Impuestos.actualizar_tasa_iva(0.16)
    assert ejercicio_5_Calculadora_Impuestos.TASA_IVA == 0.16  # Verifica que la variable global cambió


def test_calcular_iva_despues_de_actualizar_tasa():
    """Comprueba que el cálculo del IVA cambie al modificar la tasa."""
    ejercicio_5_Calculadora_Impuestos.actualizar_tasa_iva(0.10)
    precio = 200000
    esperado = precio * 0.10
    assert ejercicio_5_Calculadora_Impuestos.calcular_iva(precio) == esperado


def test_tasa_vuelve_a_valor_original():
    """Restaura la tasa original al finalizar las pruebas."""
    ejercicio_5_Calculadora_Impuestos.actualizar_tasa_iva(0.19)
    assert ejercicio_5_Calculadora_Impuestos.TASA_IVA == 0.19
