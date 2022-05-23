"""
Tarea 94 - Crear módulos propios en Python 
"""

def tierra(tiempo):
    tiempo = float(tiempo)
    gravedad = 9.8
    altura = 1/2 * gravedad * tiempo**2
    return altura

def marte(tiempo):
    tiempo = float(tiempo)
    gravedad = 3.7
    altura = 1/2 * gravedad * tiempo**2
    return altura

def jupiter(tiempo):
    tiempo = float(tiempo)
    gravedad = 24.8
    altura = 1/2 * gravedad * tiempo**2
    return altura