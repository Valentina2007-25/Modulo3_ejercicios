"""Ejercicio 1: Refactorización de Calculadora de IMC
Toma el código del "Ejercicio 1: Calculadora de IMC" del Módulo 1 y refactorízalo
completamente para que siga el principio de responsabilidad única.
1. Crea una función calcular_imc(peso: float, altura: float) -> float que reciba
el peso y la altura y devuelva el IMC.
2. Crea una función interpretar_imc(imc: float) -> str que reciba un IMC y
devuelva una cadena de texto interpretando el resultado (ej: "Bajo peso",
"Normal", "Sobrepeso").
3. Crea una función main() que orqueste el programa: pidiendo los datos al
usuario, llamando a las otras dos funciones e imprimiendo el resultado
f
 inal.
Conceptos aplicados: def, return, Type Hinting, Docstrings, Refactorización,
Principio de Responsabilidad Única, if/elif/else. """

def calcular_imc(peso: float, altura: float) -> float:
    """Calcula el Índice de Masa Corporal IMC.

    Args:
        peso (float): Peso de la persona en kilogramos.
        altura (float): Altura de la persona en metros.

    Returns:
        float: IMC redondeado a dos decimales.
    """
    imc = peso / (altura ** 2)
    return round(imc, 2)


def interpretar_imc(imc: float) -> str:
    """Devuelve una interpretación del IMC según la OMS.

    Args:
        imc (float): Valor numérico del IMC.

    Returns:
        str: Categoría correspondiente al valor del IMC.
    """
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


def main() -> None:
    """Función principal que ejecuta la calculadora de IMC."""
    peso = float(input("Digite su peso en kg: "))
    altura = float(input("Digite su altura en metros: "))

    imc = calcular_imc(peso, altura)
    categoria = interpretar_imc(imc)

    print(f"\nSu IMC es: {imc}")
    print(f"Clasificación: {categoria}")

if __name__ == "__main__":
    main()

