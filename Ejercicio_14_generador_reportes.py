'''Ejercicio 14: Generador de Reportes a partir de Múltiples Archivos
Crea un script que:
1. Lea datos de un archivo estudiantes.csv.
2. Lea datos de un archivo cursos.json.
3. Combine la información para generar un reporte en un archivo reporte.txt
que indique qué cursos ha tomado cada estudiante.
4. Todo el proceso debe estar encapsulado en funciones bien definidas
(leer_csv, leer_json, generar_reporte).
5. Para mostrar el reporte.txt final en la consola antes de guardarlo. Utilizar la
librería rich.
Conceptos integrados: Combinación de csv y json, Manejo de múltiples archivos,
Lógica de negocio en funciones, Escritura de archivos de texto. '''

import csv
import json
from rich.console import Console
from rich.table import Table

console = Console()

# FUNCIONES+
def leer_csv(ruta_csv):
    estudiantes = []
    try:
        with open(ruta_csv, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                estudiantes.append({"id": fila["id"], "nombre": fila["nombre"]})
    except FileNotFoundError:
        console.print("[red]El archivo estudiantes.csv no existe[/red]")
    return estudiantes


def leer_json(ruta_json):
    try:
        with open(ruta_json, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        console.print("[red]El archivo cursos.json no existe[/red]")
        return {}
    except json.JSONDecodeError:
        console.print("[red]ERROR: cursos.json está mal formado[/red]")
        return {}


def generar_reporte(estudiantes, cursos_dict, ruta_salida):
    reporte = []

    for estudiante in estudiantes:
        cursos = cursos_dict.get(estudiante["id"], [])
        reporte.append({
            "nombre": estudiante["nombre"],
            "cursos": cursos
        })

    guardar_reporte(reporte, ruta_salida)
    mostrar_reporte(reporte)


def guardar_reporte(reporte, ruta_salida):
    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        for entrada in reporte:
            archivo.write(f"{entrada['nombre']} -> {', '.join(entrada['cursos'])}\n")


def mostrar_reporte(reporte):
    table = Table(title="📄 Reporte de Estudiantes y Cursos")

    table.add_column("Estudiante", style="cyan")
    table.add_column("Cursos", style="magenta")

    for entrada in reporte:
        nombre = entrada["nombre"]
        cursos = ", ".join(entrada["cursos"]) if entrada["cursos"] else "Ninguno"
        table.add_row(nombre, cursos)

    console.print(table)


# PROGRAMA PRINCIPAL

def main():
    ruta_csv = "estudiantes.csv"
    ruta_json = "cursos.json"
    ruta_salida = "reporte.txt"

    estudiantes = leer_csv(ruta_csv)
    cursos_dict = leer_json(ruta_json)
    generar_reporte(estudiantes, cursos_dict, ruta_salida)

    console.print("\n[green]Reporte generado en archivo reporte.txt[/green]")


if __name__ == "__main__":
    main()
