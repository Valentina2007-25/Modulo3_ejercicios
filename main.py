from biblioteca import (
    prestar_libro,
    devolver_libro,
    buscar_libro,
    ver_libros_prestados,
)

def main():
    while True:
        print("\nSISTEMA BIBLIOTECA")
        print("1. Prestar libro")
        print("2. Devolver libro")
        print("3. Buscar libro por título")
        print("4. Ver libros prestados")
        print("5. Salir")

        opcion = input(">> ")

        if opcion == "1":
            libro_id = input("ID del libro: ")
            nombre = input("Nombre del aprendiz: ")
            prestar_libro(libro_id, nombre)

        elif opcion == "2":
            libro_id = input("ID del libro: ")
            devolver_libro(libro_id)

        elif opcion == "3":
            query = input("Buscar: ")
            buscar_libro(query)

        elif opcion == "4":
            ver_libros_prestados()

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
