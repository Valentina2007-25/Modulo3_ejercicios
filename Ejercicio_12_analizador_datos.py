'''Ejercicio 12: Analizador de Datos CSV
Escribe una función analizar_csv(nombre_archivo: str, columna: str) -> dict.
1. La función debe leer un archivo .csv que contiene datos de estudiantes
(nombre, edad, calificación).
2. Debe calcular el promedio, el máximo y el mínimo de la columna numérica
especificada.
3. Debe devolver un diccionario con estos tres valores. Utiliza el módulo csv
de Python.
4. Para presentar el diccionario de resultados del análisis (promedio, max,
min) en una tabla. Utilizar la librería rich.
Conceptos integrados: Módulo csv (DictReader), Conversión de tipos, Manejo
de archivos, Funciones. '''

import csv
from rich.console import Console
from rich.table import Table
from typing import Dict

console = Console()


def analizar_csv(nombre_archivo: str, columna: str) -> Dict[str, float]:
    """
    Lee un archivo CSV y calcula el promedio, el valor máximo y mínimo
    de la columna numérica indicada.
    """

    valores = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            if columna not in lector.fieldnames:
                raise ValueError(f"La columna '{columna}' no existe en el archivo CSV.")

            for fila in lector:
                try:
                    valores.append(float(fila[columna]))
                except ValueError:
                    pass  # Ignora valores no numéricos

    except FileNotFoundError:
        console.print(f"[red]❌ Archivo '{nombre_archivo}' no encontrado.[/red]")
        return {}

    if not valores:
        console.print("[yellow]⚠ No hay datos numéricos para analizar.[/yellow]")
        return {}

    return {
        "promedio": sum(valores) / len(valores),
        "maximo": max(valores),
        "minimo": min(valores)
    }


def mostrar_resultados(resultados: Dict[str, float]):
    """Muestra los resultados (promedio, max, min) en una tabla usando rich."""
    if not resultados:
        console.print("[yellow]No hay resultados para mostrar.[/yellow]")
        return

    tabla = Table(title="Análisis de Datos CSV")
    tabla.add_column("Métrica", style="cyan")
    tabla.add_column("Valor", style="magenta")

    for clave, valor in resultados.items():
        tabla.add_row(clave.capitalize(), f"{valor:.2f}")

    console.print(tabla)


def main():
    nombre = input("Ingrese el nombre del archivo CSV: ")
    columna = input("Ingrese el nombre de la columna numérica a analizar: ")

    resultados = analizar_csv(nombre, columna)
    mostrar_resultados(resultados)


if __name__ == "__main__":
    main()
