"""
Ejercicio 3 (Vocales) de la Tarea 176 del curso de IA The Egg. 
"""

# Creación de la función para determinar si un carácter previamente dado es vocal o no. 
def letra(x):
    # Generamos una lista donde almacenar nuestras vocales.
    vocales = ["a", "e", "i", "o", "u"]
    # Comprobamos si la letra introducida está en la lista vocales.
    if x in vocales:
        print("{} es una vocal.".format(x))
    else:
        print("{} no es una vocal.".format(x))

letra("i")