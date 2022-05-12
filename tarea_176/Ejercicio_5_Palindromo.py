"""
Ejercicio 5 (Palíndromos) de la Tarea 176 del curso de IA The Egg. 
"""

# Creación de la función para buscar si una palabra dada es palíndromo.
def palindromo(palabra):
    # Damos la vuelta a la palabra mediante la notación de corte, y almacenamos en la variable palin.
    palin = palabra[::-1]
    # Comprobamos si la palabra dada es igual a la palabra al revés.
    if palabra == palin:
        print('{} es un palíndromo.'.format(palabra))
    else:
        print('{} no es un palíndromo.'.format(palabra))

palindromo('1210111')