import json
from typing import Any, List, Dict
from rich.table import Table
from rich.console import Console

console = Console()

RUTA = "biblioteca.json"

def cargar_datos() -> List[Dict[str, Any]]:
    """Carga el inventario desde archivo JSON."""
    try:
        with open(RUTA, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        console.print("[red]No existe biblioteca.json, creando uno nuevo...[/red]")
        guardar_datos([])
        return []
    except json.JSONDecodeError:
        console.print("[red]Error: JSON malformado[/red]")
        return []


def guardar_datos(data: List[Dict[str, Any]]) -> None:
    """Guarda inventario en JSON."""
    with open(RUTA, "w", encoding="utf-8") as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)


def prestar_libro(libro_id: str, nombre_aprendiz: str) -> None:
    """Marca un libro como prestado."""
    data = cargar_datos()

    for libro in data:
        if libro["libro_id"] == libro_id:
            if libro["prestado_a"] is not None:
                console.print("[yellow]El libro ya está prestado[/yellow]")
                return
            libro["prestado_a"] = nombre_aprendiz
            guardar_datos(data)
            console.print("[green]Libro prestado exitosamente[/green]")
            return

    console.print("[red]Libro no encontrado[/red]")


def devolver_libro(libro_id: str) -> None:
    """Marca un libro como disponible."""
    data = cargar_datos()

    for libro in data:
        if libro["libro_id"] == libro_id:
            if libro["prestado_a"] is None:
                console.print("[yellow]⚠ El libro ya estaba disponible[/yellow]")
                return
            libro["prestado_a"] = None
            guardar_datos(data)
            console.print("[green]Libro devuelto[/green]")
            return

    console.print("[red]Libro no encontrado[/red]")


def buscar_libro(query: str) -> List[Dict[str, Any]]:
    """Devuelve libros cuyo título contenga query."""
    data = cargar_datos()
    resultado = [
        libro for libro in data
        if query.lower() in libro["titulo"].lower()
    ]

    mostrar_tabla(resultado, title="Resultados de búsqueda")
    return resultado


def ver_libros_prestados() -> List[Dict[str, Any]]:
    """Devuelve libros prestados."""
    data = cargar_datos()
    prestados = [libro for libro in data if libro["prestado_a"]]

    mostrar_tabla(prestados, title="Libros Prestados")
    return prestados


def mostrar_tabla(lista: List[Dict[str, Any]], title: str) -> None:
    """Muestra libros en tabla (rich)."""
    table = Table(title=title)
    table.add_column("ID")
    table.add_column("Título")
    table.add_column("Prestado a")

    for libro in lista:
        table.add_row(libro["libro_id"], libro["titulo"], str(libro["prestado_a"]))

    console.print(table)
