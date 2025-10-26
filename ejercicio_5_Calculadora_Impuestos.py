'''Ejercicio 5: Calculadora de Impuestos con Scope Global
Simula el cálculo de impuestos donde la tasa puede cambiar.
1. Define una variable global TASA_IVA = 0.19.
2. Crea una función calcular_iva(precio_base: float) -> float que lea la variable
global y devuelva el valor del IVA para un precio dado.
3. Crea una función actualizar_tasa_iva(nueva_tasa: float) que modifique el
valor de la variable global TASA_IVA usando la palabra clave global.
4. Demuestra cómo el resultado de calcular_iva cambia después de llamar a
actualizar_tasa_iva.
Conceptos aplicados: Scope Global vs. Local, global (y la discusión sobre
cuándo es apropiado su uso). '''

# Variable global
TASA_IVA = 0.19


def calcular_iva(precio_base: float) -> float:
    """
    Calcula el valor del IVA para un precio base usando la tasa global TASA_IVA.

    Args:
        precio_base (float): Precio sin IVA.

    Returns:
        float: Valor del IVA calculado.
    """
    return precio_base * TASA_IVA


def actualizar_tasa_iva(nueva_tasa: float) -> None:
    """
    Actualiza la tasa global TASA_IVA a una nueva tasa.

    Args:
        nueva_tasa (float): Nueva tasa de IVA (por ejemplo, 0.16 para 16%).
    """
    global TASA_IVA
    TASA_IVA = nueva_tasa


def main() -> None:
    """
    Demuestra cómo cambia el cálculo del IVA cuando se modifica la tasa global.
    """
    precio = 100000

    print("Tasa inicial:", TASA_IVA)
    print("IVA con tasa 19%:", calcular_iva(precio))

    actualizar_tasa_iva(0.16)
    print("Tasa actualizada:", TASA_IVA)
    print("IVA con tasa 16%:", calcular_iva(precio))


if __name__ == "__main__":
    main()

