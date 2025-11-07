import os
import csv
import pytest
from Ejercicio_12_analizador_datos import analizar_csv


@pytest.fixture
def crear_csv_tmp(tmp_path):
    """Genera un archivo CSV temporal para pruebas."""
    def _crear(nombre, encabezados, filas):
        ruta = tmp_path / nombre
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=encabezados)
            writer.writeheader()
            writer.writerows(filas)
        return ruta
    return _crear


def test_analizar_csv_correcto(crear_csv_tmp):
    archivo = crear_csv_tmp(
        "datos.csv",
        ["nombre", "valor"],
        [{"nombre": "A", "valor": "10"}, {"nombre": "B", "valor": "20"}, {"nombre": "C", "valor": "30"}]
    )

    resultado = analizar_csv(str(archivo), "valor")

    assert resultado["promedio"] == 20
    assert resultado["maximo"] == 30
    assert resultado["minimo"] == 10


def test_analizar_csv_columna_inexistente(crear_csv_tmp):
    archivo = crear_csv_tmp(
        "datos.csv",
        ["x", "y"],
        [{"x": "A", "y": "10"}]
    )

    with pytest.raises(ValueError):
        analizar_csv(str(archivo), "invalido")


def test_analizar_csv_sin_archivo(capsys):
    resultado = analizar_csv("archivo_inexistente.csv", "valor")

    captured = capsys.readouterr()

    assert resultado == {}
    assert "Archivo" in captured.out


def test_analizar_csv_sin_datos_numericos(crear_csv_tmp, capsys):
    archivo = crear_csv_tmp(
        "datos.csv",
        ["dato"],
        [{"dato": "x"}, {"dato": "y"}]
    )

    resultado = analizar_csv(str(archivo), "dato")

    captured = capsys.readouterr()

    assert resultado == {}
    assert "No hay datos numéricos" in captured.out
