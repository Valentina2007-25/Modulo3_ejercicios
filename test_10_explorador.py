import pytest
from ejercicio_ import explorar_estructura


def test_valor_simple(capsys):
    explorar_estructura(10)
    captured = capsys.readouterr()
    assert "Valor: 10, Profundidad: 1" in captured.out


def test_lista_simple(capsys):
    explorar_estructura([1, 2])
    captured = capsys.readouterr()
    assert "Valor: 1, Profundidad: 2" in captured.out
    assert "Valor: 2, Profundidad: 2" in captured.out


def test_estructura_anidada(capsys):
    explorar_estructura([1, [2, 3]])
    captured = capsys.readouterr()
    assert "Valor: 1, Profundidad: 2" in captured.out
    assert "Valor: 2, Profundidad: 3" in captured.out
    assert "Valor: 3, Profundidad: 3" in captured.out


def test_diccionario(capsys):
    explorar_estructura({"a": 1, "b": 2})
    captured = capsys.readouterr()
    assert "Valor: 1, Profundidad: 2" in captured.out
    assert "Valor: 2, Profundidad: 2" in captured.out


def test_combination(capsys):
    explorar_estructura([1, {"a": 2, "b": [3]}])
    captured = capsys.readouterr()

    assert "Valor: 1, Profundidad: 2" in captured.out
    assert "Valor: 2, Profundidad: 3" in captured.out
    assert "Valor: 3, Profundidad: 4" in captured.out
