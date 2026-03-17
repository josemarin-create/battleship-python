import os


def convertir_coordenada(coordenada):
    """
    Convert player input (e.g., B7) into board indexes.
    Returns a tuple (row, column).
    """

    letras = "ABCDEFGHIJ"

    columna_letra = coordenada[0].upper()
    fila_numero = int(coordenada[1:])

    columna = letras.index(columna_letra)
    fila = fila_numero - 1

    return fila, columna


def limpiar_pantalla():
    """
    Clear the console screen.
    Works on Windows, Linux and Mac.
    """

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
