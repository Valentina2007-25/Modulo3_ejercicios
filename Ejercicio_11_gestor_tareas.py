'''Ejercicio 11: Gestor de Tareas en Archivo de Texto (.txt)
Crea una aplicación de consola que permita al usuario gestionar una lista de
tareas.
1. Las tareas se deben guardar en un archivo tareas.txt, una por línea.
2. Para mostrar la lista de tareas. Utilizar la librería rich.
3. Implementa funciones para:
o agregar_tarea(tarea: str): Añade una tarea al final del archivo.
o ver_tareas() -> list[str]: Lee todas las tareas del archivo y las
devuelve como una lista.
o Una función main que muestre un menú y gestione las llamadas.
Conceptos integrados: Funciones, Manejo de archivos (with open, modos 'r', 'a'),
writelines, readlines. '''

from rich.console import Console
from rich.table import Table

# Nombre del archivo donde se guardan las tareas
ARCHIVO = "tareas.txt"

console = Console()


def agregar_tarea(tarea: str) -> None:
    """Añade una tarea al archivo tareas.txt"""
    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(tarea + "\n")
    console.print("[green]✅ Tarea agregada correctamente.[/green]")


def ver_tareas() -> list[str]:
    """Lee todas las tareas del archivo y las retorna como lista"""
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            tareas = archivo.readlines()
        return [tarea.strip() for tarea in tareas]
    except FileNotFoundError:
        console.print("[red]⚠ No existe el archivo de tareas aún.[/red]")
        return []


def mostrar_tareas():
    """Muestra las tareas usando rich"""
    tareas = ver_tareas()

    if not tareas:
        console.print("[yellow]No hay tareas disponibles.[/yellow]")
        return

    tabla = Table(title="Lista de Tareas")
    tabla.add_column("N°", style="cyan", justify="center")
    tabla.add_column("Tarea", style="magenta")

    for i, tarea in enumerate(tareas, start=1):
        tabla.add_row(str(i), tarea)

    console.print(tabla)


def main():
    while True:
        console.print("\n[bold blue]=== GESTOR DE TAREAS ===[/bold blue]")
        console.print("1. Agregar tarea")
        console.print("2. Ver tareas")
        console.print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea = input("Ingrese la tarea: ")
            agregar_tarea(tarea)

        elif opcion == "2":
            mostrar_tareas()

        elif opcion == "3":
            console.print("[bold green]cerrando programa ---[/bold green]")
            break

        else:
            console.print("[red] Opción no válida.[/red]")


if __name__ == "__main__":
    main()
