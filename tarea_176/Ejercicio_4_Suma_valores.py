"""
Ejercicio 4 (Suma de los valores de una lista) de la Tarea 176 del curso de IA The Egg. 
"""

# Creación de la función para realizar la suma de los valores de una lista.
def suma(lista):
    # Usamos la función sum para sumar los valores de la lista.
    suma = sum(lista)
    print("La suma de lis valores de la lista es {}".format(suma))

lis = [1, 2, 2]
suma(lis)