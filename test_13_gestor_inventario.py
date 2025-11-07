import json
import pytest
from Ejercicio_13_gestor_inventario import (
    cargar_inventario,
    guardar_inventario,
    agregar_producto,
    vender_producto,
    ARCHIVO
)

@pytest.fixture
def inventario_temp(tmp_path, monkeypatch):
    """Crea inventario temporal redirigiendo archivo JSON al tmp."""
    archivo = tmp_path / "inventario.json"

    # Reemplazar ruta del módulo por archivo temporal
    monkeypatch.setattr("ejercicio_13_gestor_inventario.ARCHIVO", str(archivo))
    return archivo


def test_cargar_inventario_vacio(inventario_temp):
    inventario = cargar_inventario()
    assert inventario == []


def test_guardar_y_cargar_inventario(inventario_temp):
    data = [
        {"nombre": "Manzanas", "cantidad": 10, "precio": 2.5}
    ]

    guardar_inventario(data)
    inventario = cargar_inventario()

    assert inventario == data


def test_agregar_producto(inventario_temp):
    inventario = []
    agregar_producto(inventario, "Leche", 5, 3.2)

    assert len(inventario) == 1
    assert inventario[0]["nombre"] == "Leche"
    assert inventario[0]["cantidad"] == 5
    assert inventario[0]["precio"] == 3.2


def test_vender_producto_exitoso(inventario_temp, capsys):
    inventario = [{"nombre": "Pan", "cantidad": 10, "precio": 1.0}]
    vender_producto(inventario, "Pan", 3)

    assert inventario[0]["cantidad"] == 7

    out = capsys.readouterr().out
    assert "Venta realizada" in out


def test_vender_producto_stock_insuficiente(inventario_temp, capsys):
    inventario = [{"nombre": "Pan", "cantidad": 2, "precio": 1.0}]
    vender_producto(inventario, "Pan", 5)

    out = capsys.readouterr().out
    assert "No hay suficiente stock" in out
    assert inventario[0]["cantidad"] == 2  # No se descuenta


def test_vender_producto_no_existe(inventario_temp, capsys):
    inventario = [{"nombre": "Pan", "cantidad": 2, "precio": 1.0}]
    vender_producto(inventario, "Carne", 1)

    out = capsys.readouterr().out
    assert "Producto no encontrado" in out
