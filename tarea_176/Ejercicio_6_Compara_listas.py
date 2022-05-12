"""
Ejercicio 6 (Comparar listas) de la Tarea 176 del curso de IA The Egg. 
"""

# Creación de la función para que compare dos listas y encuentre si hay algún valor coincidente.
def comparar(lista1, lista2):
    # Recogemos en la variable a una lista donde comprobamos si el contenido de la primera lista está en la segunda lista,
    # obteniendo una lista de la misma longitud que la lista 1 y con valores booleanos de True o False en caso de que esté o no.
    a = list(map(lambda x: x in lista2, lista1))
    # Realizamos un condicional para comprobar si efectivamente hya valores coincidentes o no.
    if True in a:
        # Para conocer que valores son coincidentes, realizamos un loop, donde obtenemos el índice del valor que coincide, y agregamos dicho valor a la lista [valor].
        valor = []
        for indx, bool in enumerate(a):
            if bool == True:
                valor.append(lista1[indx])
        print("Hay valores iguales, y son: {}".format(valor))
    else:
        print("No hay valores iguales")

lista1 = [1, 2, 3]
lista2 = [2, 4, 5, 1]

comparar(lista1, lista2)
