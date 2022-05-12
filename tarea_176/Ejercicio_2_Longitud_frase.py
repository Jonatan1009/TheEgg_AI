"""
Ejercicio 2 (Longitud de una frase) de la Tarea 176 del curso de IA The Egg. 
"""

# Creación de la función para contabilizar la longitud de una frase. 
def long_frase(frase):
    # Utilizamos la función map, para contabilizar los caracteres que tiene nuestra frase y los introducimos en una lista.
    caracteres = list(map(len,frase))
    # Sumamos todos los valores de la lista, obteniendo la longitud de nuestra frase.
    longitud = sum(caracteres)
    # Devolvemos el valor de la variable longitud
    return longitud


frase = "Hola, esta es la frase de prueba."
resultado = long_frase(frase)
print("La frase que has introducido tiene una longitud de {} caracteres".format(resultado))