'''Ejercicio 8: Transformación de Datos con List y Dictionary Comprehensions
Dado un texto largo como un string, realiza lo siguiente:
1. Usa una List Comprehension para crear una lista de todas las palabras del
texto que tengan más de 5 letras y estén en mayúsculas.
2. Usa una Dictionary Comprehension para crear un diccionario que cuente
la longitud de cada palabra de la lista resultante. {"PALABRA": 7, ...}.
Conceptos aplicados: List Comprehensions, Dictionary Comprehensions,
Métodos de string (split, upper). '''

texto = """PYTHON es un lenguaje de PROGRAMACION muy EXTENSO pero practivo y mucho 
APRENDIZAJE."""

palabras_mayusculas = [palabra for palabra in texto.split() if len(palabra) > 5 and palabra.isupper()]

longitudes = {palabra: len(palabra) for palabra in palabras_mayusculas}

print("lista de palabras en mayúsculas con más de 5 letras:", palabras_mayusculas)
print ("diccionario de longitudes de palabras:", longitudes)