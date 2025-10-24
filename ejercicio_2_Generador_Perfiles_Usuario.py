'''Ejercicio 2: Generador de Perfiles de Usuario con Argumentos Flexibles
Crea una función crear_perfil(nombre: str, edad: int, *hobbies: str,
**redes_sociales: str) -> str que genere un perfil de usuario.
1. La función debe aceptar un nombre y una edad como argumentos
posicionales obligatorios.
2. Debe aceptar cualquier cantidad de hobbies como argumentos de longitud
variable (*args).
3. Debe aceptar cualquier cantidad de redes_sociales como argumentos de
palabra clave (**kwargs), donde la clave es el nombre de la red (ej.
twitter="@usuario") y el valor es el usuario.
4. La función debe devolver un string formateado con toda la información.
Conceptos aplicados: *args, **kwargs, Parámetros posicionales, Type Hinting
(Tuple, Dict), Docstrings, f-strings.'''

def crear_perfil(nombre: str, edad: int, *hobbies: str, **redes_sociales: str) -> str:
    """
    Genera un perfil de usuario a partir del nombre, la edad, hobbies y redes sociales.

    Args:
        nombre (str): Nombre del usuario.
        edad (int): Edad del usuario (debe ser positiva).
        *hobbies (str): Lista variable de hobbies del usuario.
        **redes_sociales (str): Diccionario de redes sociales donde la clave es la red.

    Returns:
        str: Texto formateado con toda la información del perfil.

    Raises:
        ValueError: Si alguno de los valores ingresados no cumple con las validaciones.
    """

    # Validaciones de entrada
    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("El nombre no debe estar vacío.")

    if nombre.isdigit():
        raise ValueError("El nombre no puede contener solo números.")

    if any(char.isdigit() for char in nombre):
        raise ValueError("El nombre no puede contener números.")

    if not isinstance(edad, int) or edad <= 0:
        raise ValueError("La edad debe ser un número entero positivo.")

    if any(not isinstance(h, str) or not h.strip() for h in hobbies):
        raise ValueError("Todos los hobbies deben ser cadenas no vacías.")

    if any(not isinstance(k, str) or not isinstance(v, str) for k, v in redes_sociales.items()):
        raise ValueError("Las redes sociales deben ser cadenas (clave y valor).")

    # Construcción del perfil
    perfil = "\n____ PERFIL DE USUARIO ____\n"
    perfil += f"Nombre: {nombre}\n"
    perfil += f"Edad: {edad}\n"

    if hobbies:
        perfil += f"Hobbies: {', '.join(hobbies)}\n"
    else:
        perfil += "Hobbies: No especifica\n"

    if redes_sociales:
        perfil += "Redes Sociales:\n"
        for red, usuario in redes_sociales.items():
            perfil += f"  - {red}: {usuario}\n"
    else:
        perfil += "Redes Sociales: No registro\n"

    return perfil

# Función principal para interacción por consola
def main():
    """Función principal para interactuar con el usuario por consola."""
    while True:
        try:
            # Ingreso de nombre y edad
            nombre = input("Ingrese el nombre del usuario: ").strip()
            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            if nombre.isdigit():
                raise ValueError("El nombre no puede contener solo números.")
            if any(char.isdigit() for char in nombre):
                raise ValueError("El nombre no puede contener números.")

            edad_input = input("Ingrese la edad del usuario: ").strip()
            if not edad_input.isdigit():
                raise ValueError("Debe ingresar un número válido para la edad.")
            edad = int(edad_input)
            if edad <= 0:
                raise ValueError("La edad debe ser mayor que cero.")

            # Ingreso de hobbies
            hobbies_input = input("Ingrese los hobbies separados por coma: ")
            hobbies = [h.strip() for h in hobbies_input.split(",") if h.strip()]

            # Ingreso de redes sociales
            redes_sociales = {}
            while True:
                agregar = input("¿Desea agregar una red social? (s/n): ").lower().strip()
                if agregar == "n":
                    break
                elif agregar == "s":
                    red = input("Nombre de la red social: ").strip()
                    usuario = input(f"Usuario en {red}: ").strip()
                    if red and usuario:
                        redes_sociales[red] = usuario
                    else:
                        print("Datos no válidos. Intente nuevamente.")
                else:
                    print("Respuesta no válida. Escriba 's' o 'n'.")

            # Generar y mostrar el perfil
            perfil = crear_perfil(nombre, edad, *hobbies, **redes_sociales)
            print("\n~ ~ ~ PERFIL GENERADO ~ ~ ~ ")
            print(perfil)
            break  # Sale del bucle si todo fue bien

        except ValueError as e:
            print(f"\nError: {e}")
            print("Por favor, vuelve a intentarlo.\n")


if __name__ == "__main__":
    main()




