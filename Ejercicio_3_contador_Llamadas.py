'''Ejercicio 3: Contador de Llamadas con Closure
Diseña una "fábrica de contadores" usando funciones anidadas.
1. Crea una función externa crear_contador() que inicialice una variable
conteo = 0.
2. Dentro de crear_contador(), define una función interna incrementar() que
modifique la variable conteo usando la palabra clave nonlocal y la
devuelva.
3. La función externa debe retornar la función interna incrementar.
4. Escribe el código para probar que cada contador creado es independiente.
Conceptos aplicados: Funciones anidadas, Closures, Scope Enclosing, nonlocal.'''

def crear_contador():
    conteo=0
    """
       crear un contador de llamadas con closure
           definir funcion crear_contador()
           definir funcion incrementar() dentro de crear_contador()
                usar nonlocal para modificar la variable conteo
       Returns:
           retorna la funcion incrementar()

       """
    def incrementar():
        "crear una funcion incrementar() que modifique la variable conteo"
        nonlocal conteo
        conteo +=1
        return conteo
    #  la funcion externa retorna la funcion interna incrementar
    return incrementar

#se crean dos contadores independientes
contador1 = crear_contador()
contador2 = crear_contador()

#se imprimen los contadores para verificar que son independientes
print(contador1())
print(contador1())
print(contador1())

print(contador2())
print(contador2())
