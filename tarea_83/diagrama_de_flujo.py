"""
Tarea 83 - Diagramas de flujo: esquematizar antes de programar II
-----------------------------------------------------------------

Se realiza el programa, codificado en Python, del diagrama que está en la misma carpeta.
"""

# Primero preguntamos el valor que tenga el lado del cuadrado en centímetros.
lado = int(input("Vamos a calcular el área de un cuadrado.\n ¿Cuánto mide el lado en centímetros?"))

# Calculamos el área del cuadrado multiplicando el lado por lado.
area = lado * lado

# Imprimimos el resultado del área del cuadrado.
print("El área del cuadrado es {} cm\u00b2".format(area))