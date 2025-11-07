'''Ejercicio 7: Filtrado de Estudiantes con filter
Dada una lista de tuplas estudiantes = [("Ana", 4.5), ("Juan", 2.8), ("Maria", 3.9)], usa
filter() y una lambda para obtener una nueva lista que contenga únicamente a los
estudiantes que aprobaron (nota >= 3.0).
Conceptos aplicados: filter, lambda, trabajo con tuplas. '''

estudiantes = [("Ana", 4.5), ("Juan", 2.8), ("Maria", 3.9), ("Luis", 2.5), ("Sofia", 3.2)]

estudiantes_aprobados = list(filter(lambda estudiante: estudiante[1] >= 3.0, estudiantes))
print(estudiantes_aprobados)  # Salida: [('Ana', 4.5), ('Maria', 3.9), ('Sofia', 3.2)]
# se muestra el resultado de los estudiantes aprobados
print("Estudiantes aprobados:")
for estudiante in estudiantes_aprobados:
    print(f"{estudiante[0]} con nota {estudiante[1]}")
