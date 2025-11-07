import json
import csv
import os
import pytest
from io import StringIO
from unittest.mock import mock_open, patch

from Ejercicio_14_generador_reportes import (
    leer_csv,
    leer_json,
    generar_reporte,
    guardar_reporte,
)


def test_leer_csv(tmp_path):
    # Crear archivo CSV temporal
    data = "id,nombre\n1,Ana\n2,Carlos\n"
    archivo_csv = tmp_path / "estudiantes.csv"
    archivo_csv.write_text(data, encoding="utf-8")

    estudiantes = leer_csv(str(archivo_csv))

    assert len(estudiantes) == 2
    assert estudiantes[0]["nombre"] == "Ana"
    assert estudiantes[1]["id"] == "2"


def test_leer_csv_archivo_no_existe(capfd):
    estudiantes = leer_csv("no_existe.csv")
    captured = capfd.readouterr()

    assert estudiantes == []
    assert "no existe" in captured.out


def test_leer_json(tmp_path):
    data = {"1": ["Python", "Excel"]}
    archivo_json = tmp_path / "cursos.json"
    archivo_json.write_text(json.dumps(data), encoding="utf-8")

    resultado = leer_json(str(archivo_json))

    assert resultado["1"] == ["Python", "Excel"]


def test_leer_json_malformado(tmp_path, capfd):
    archivo_json = tmp_path / "cursos.json"
    archivo_json.write_text("{mal json", encoding="utf-8")

    resultado = leer_json(str(archivo_json))
    captured = capfd.readouterr()

    assert resultado == {}
    assert "mal formado" in captured.out


def test_guardar_reporte(tmp_path):
    reporte = [
        {"nombre": "Ana", "cursos": ["Python"]},
        {"nombre": "Luis", "cursos": []},
    ]

    ruta = tmp_path / "reporte.txt"
    guardar_reporte(reporte, str(ruta))

    contenido = ruta.read_text(encoding="utf-8")
    assert "Ana -> Python" in contenido
    assert "Luis -> " in contenido


def test_generar_reporte(tmp_path):
    estudiantes = [
        {"id": "1", "nombre": "Ana"},
        {"id": "2", "nombre": "Luis"}
    ]

    cursos = {
        "1": ["Python", "Java"],
        "2": []
    }

    ruta = tmp_path / "reporte.txt"

    # Solo comprobamos que el archivo se genera
    generar_reporte(estudiantes, cursos, str(ruta))

    assert ruta.exists()
    contenido = ruta.read_text(encoding="utf-8")
    assert "Ana -> Python, Java" in contenido
    assert "Luis -> " in contenido

