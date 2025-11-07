from ejercicio_6_Procesamiento_Datos import productos, precios_descuento

def test_cantidad_descuentos():
    """Verifica que la cantidad de precios con descuento sea igual a la cantidad de productos."""
    assert len(precios_descuento) == len(productos)

def test_calculo_descuento():
    """Verifica que cada precio tenga un 10% de descuento aplicado correctamente."""
    for i in range(len(productos)):
        precio_original = productos[i]["precio"]
        precio_esperado = precio_original * 0.9
        assert precios_descuento[i] == precio_esperado
