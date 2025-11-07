'''Ejercicio 9: Sumatoria con reduce
Utiliza functools.reduce para dos propósitos:
1. Calcular la suma total de una lista de números [1, 2, 3, 4, 5].
2. Concatenar una lista de strings ["Hola", " ", "SENA", "!"] en una sola frase.
• Conceptos aplicados: functools.reduce, lambda. '''

from functools import reduce

numeros = [1, 2, 3, 4, 5]
suma_total = reduce(lambda x, y: x + y, numeros)
print("Suma total:", suma_total)

palabras = ["Hola", " ", "SENA", "!"]
frase = reduce(lambda x, y: x + y, palabras)
print("Frase concatenada:", frase)