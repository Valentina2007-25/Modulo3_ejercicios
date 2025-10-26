'''Ejercicio 4: Validador de Datos Genérico
Escribe una función de orden superior aplicar_validador(datos: list, validador: 
callable) -> list. 
1. Esta función recibirá una lista de datos y otra función (el validador). 
2. Debe aplicar la función validador a cada elemento de la lista y devolver una 
nueva lista solo con los elementos que pasaron la validación. 
3. Crea al menos dos funciones de validación para probarla: 
es_email_valido(email: str) -> bool y es_mayor_a_10(numero: int) -> bool. 
• Conceptos aplicados: Funciones como argumentos (Higher-Order 
Functions), Type Hinting (Callable), Reutilización de código. '''

from typing import Callable  # 👈 Import usar Callable

def aplicar_validador(datos: list, validador: Callable) -> list:
    """
        Aplica una función validadora a cada elemento de una lista y devuelve
        una nueva lista con los elementos que pasan la validación.

        Args:
            datos (list): Lista de elementos a validar.
            validador (Callable): Función que recibe un elemento y devuelve True o False.

        Returns:
            list: Nueva lista con los elementos que pasaron la validación.
        """
    return [d for d in datos if validador(d)]


# --- Funciones de validación ---
def es_email_valido(email: str) -> bool:
    """
    Valida si un correo electrónico tiene formato correcto.
    Debe contener un '@' y un '.' después del '@'.
    """
    if "@" not in email:
        return False

    nombre, dominio = email.split("@", 1)
    if "." not in dominio:
        return False

    # Evita casos vacíos como "@gmail.com" o "nombre@"
    return bool(nombre) and bool(dominio.split(".")[-1])

def es_mayor_a_10(numero: int) -> bool:
    """
    Determina si un número entero es mayor que 10.

    Args:
        numero (int): Número que se desea evaluar.

    Returns:
        bool: True si el número es mayor a 10, False en caso contrario.
    """
    return numero > 10


#Ejemplo de uso
if __name__ == "__main__":
    # Lista de correos
    correos = ["chaparrovalentina989@gmail.com", "correo@dominio.com"]
    correos_validos = aplicar_validador(correos, es_email_valido)
    print("Correos válidos:", correos_validos)

    # Lista de números
    numeros = [5, 12, 8, 20, 3, 15]
    numeros_validos = aplicar_validador(numeros, es_mayor_a_10)
    print("Números mayores a 10:", numeros_validos)
