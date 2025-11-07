'''Ejercicio 6: Procesamiento de Datos con map y lambda
Dada una lista de diccionarios productos = [{"nombre": "Camisa", "precio": 50000},
...], utiliza la función map() junto con una función lambda para crear una nueva
lista que contenga solo los precios con un 10% de descuento aplicado.
Conceptos aplicados: Programación funcional, map, lambda, trabajo con
diccionarios. '''

productos = [
    {"nombre": "Camisa", "precio": 50000},
    {"nombre": "Pantalón", "precio": 80000},
    {"nombre": "Zapatos", "precio": 120000},
    {"nombre": "Chaqueta", "precio": 150000},
]
# Usamos map y lambda para aplicar un descuento del 10%
precios_descuento = list(map(lambda p: p["precio"] * 0.9, productos))

# Mostramos el resultado
print(precios_descuento)