'''Ejercicio 13: Gestor de Inventario Persistente con JSON
Mejora el proyecto de inventario de módulos anteriores.
1. El inventario (una lista de diccionarios) se debe cargar desde un archivo
inventario.json al iniciar el programa.
2. Cada vez que se agrega un producto, se realiza una venta o se modifica
algo, la lista actualizada se debe guardar de nuevo en el archivo
inventario.json.
3. Usa funciones modulares para cargar, guardar, agregar, vender y mostrar el
inventario.
4. Para mostrar_inventario(). Utilizar la librería rich.
Conceptos integrados: Módulo json (load, dump), Persistencia de datos,
Modularización, Listas y Diccionarios.'''

import json
from rich.console import Console
from rich.table import Table
from typing import List, Dict

ARCHIVO = "inventario.json"
console = Console()

# Cargar y guardar inventario


def cargar_inventario() -> List[Dict]:
    """Carga el inventario desde inventario.json, o retorna lista vacía si no existe."""
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        console.print("[red]❌ Error al leer inventario.json[/red]")
        return []


def guardar_inventario(inventario: List[Dict]) -> None:
    """Guarda el inventario actual en inventario.json."""
    with open(ARCHIVO, "w", encoding="utf-8") as file:
        json.dump(inventario, file, indent=4, ensure_ascii=False)

# Funciones de inventario


def agregar_producto(inventario: List[Dict], nombre: str, cantidad: int, precio: float):
    """Agrega un nuevo producto al inventario."""
    inventario.append({
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    })
    guardar_inventario(inventario)
    console.print("[green]✅ Producto agregado.[/green]")


def vender_producto(inventario: List[Dict], nombre: str, cantidad: int):
    """Resta cantidad al producto, si hay stock."""
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                guardar_inventario(inventario)
                console.print("[green]Venta realizada.[/green]")
                return
            else:
                console.print("[red]No hay suficiente stock.[/red]")
                return

    console.print("[yellow]⚠ Producto no encontrado.[/yellow]")


def mostrar_inventario(inventario: List[Dict]):
    """Muestra el inventario usando rich."""
    if not inventario:
        console.print("[yellow]No hay productos en inventario.[/yellow]")
        return

    tabla = Table(title="Inventario")
    tabla.add_column("Nombre", style="cyan")
    tabla.add_column("Cantidad", style="magenta")
    tabla.add_column("Precio", style="green")

    for producto in inventario:
        tabla.add_row(
            producto["nombre"],
            str(producto["cantidad"]),
            f"${producto['precio']:.2f}"
        )

    console.print(tabla)

# Menú
def main():
    inventario = cargar_inventario()

    while True:
        console.print("\n[bold blue]=== GESTOR DE INVENTARIO ===[/bold blue]")
        console.print("1. Mostrar inventario")
        console.print("2. Agregar producto")
        console.print("3. Vender producto")
        console.print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_inventario(inventario)

        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            agregar_producto(inventario, nombre, cantidad, precio)

        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad a vender: "))
            vender_producto(inventario, nombre, cantidad)

        elif opcion == "4":
            console.print("[green]¡Hasta luego![/green]")
            break

        else:
            console.print("[red]Opción no válida.[/red]")


if __name__ == "__main__":
    main()
