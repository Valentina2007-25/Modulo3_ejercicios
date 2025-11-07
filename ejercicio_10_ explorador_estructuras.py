'''Ejercicio 10: Explorador de Estructuras de Datos Recursivo
Crea una función recursiva explorar_estructura(elemento) que pueda "explorar"
cualquier estructura de datos anidada (listas dentro de listas, diccionarios dentro
de diccionarios, etc.) e imprima cada valor no-iterable (como strings, números)
junto a su "profundidad".
Ejemplo de salida para [1, [2, 3], {"a": 4}]: Valor: 1, Profundidad: 1 Valor: 2,
Profundidad: 2 ...
• Conceptos aplicados: Recursividad, Caso base, isinstance(), Type Hinting
(Any). '''

from typing import Any

def explorar_estructura(elemento: Any, profundidad: int = 1) -> None:
    """
    Explora recursivamente estructuras anidadas (listas, tuplas, sets, diccionarios)
    e imprime los valores no iterables con su nivel de profundidad.
    """

    if isinstance(elemento, (int, float, str, bool, type(None))):
        print(f"Valor: {elemento}, Profundidad: {profundidad}")
        return

    # Si es diccionario, recorrer sus valores
    if isinstance(elemento, dict):
        for valor in elemento.values():
            explorar_estructura(valor, profundidad + 1)

    # Si es iterable → recorrer cada item (lista, tupla, set)
    elif isinstance(elemento, (list, tuple, set)):
        for item in elemento:
            explorar_estructura(item, profundidad + 1)

    # Si no es reconocible (otro tipo), mostrarlo igualmente
    else:
        print(f"Valor: {elemento}, Profundidad: {profundidad}")


# Ejemplo de prueba
if __name__ == "__main__":
    data = [1, [2, 3], {"a": 4}]
    explorar_estructura(data)
