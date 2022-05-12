"""
Ejercicio 1 (Máximo de 3 números dados) de la Tarea 176 del curso de IA The Egg.
"""

# Creación de la función para encontrar el máximo de 3 números dados. 
def maximo (a, b, c):
    # Introducimos los números en una lista.
    numeros = [a, b, c]
    # Ordenamos los números en una lista nueva, de forma que el mayor quede en la posición 0 de la lista.
    numeros_ordenados = sorted(numeros, reverse=True)
    # Mediante condicionales comprobamos si el número en la posición 0 es mayor que el de la posición 1.
    if numeros_ordenados[0] > numeros_ordenados[1]:
        print("El máximo de los tres números dados es {}".format(numeros_ordenados[0]))
    # Si los números de la posición 0, 1 y 2 son iguales, es que se han introducido 3 números iguales.
    elif numeros_ordenados[0] == numeros_ordenados[1] == numeros_ordenados[2]:
        print("Has introducido 3 números iguales")
    # Si los números de la posición 0 y 1 son iguales, es que se han introducido 2 números iguales que son máximos
    elif numeros_ordenados[0] == numeros_ordenados[1]:
        print("Has introducido 2 números iguales, que son máximos")


maximo(4, 54, 4)
