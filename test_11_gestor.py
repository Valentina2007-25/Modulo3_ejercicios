import os
import pytest
from Ejercicio_11_gestor_tareas import agregar_tarea, ver_tareas, ARCHIVO


@pytest.fixture
def limpiar_archivo():
    """Elimina el archivo antes y después de cada prueba."""
    if os.path.exists(ARCHIVO):
        os.remove(ARCHIVO)
    yield
    if os.path.exists(ARCHIVO):
        os.remove(ARCHIVO)


def test_agregar_tarea(limpiar_archivo):
    agregar_tarea("Hacer mercado")

    assert os.path.exists(ARCHIVO)

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    assert "Hacer mercado" in contenido


def test_ver_tareas_sin_archivo(limpiar_archivo, capsys):
    tareas = ver_tareas()
    captured = capsys.readouterr()

    assert tareas == []
    assert "No existe el archivo de tareas" in captured.out


def test_ver_tareas_con_contenido(limpiar_archivo):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        archivo.write("Estudiar Python\n")
        archivo.write("Hacer ejercicio\n")

    tareas = ver_tareas()

    assert tareas == ["Estudiar Python", "Hacer ejercicio"]
