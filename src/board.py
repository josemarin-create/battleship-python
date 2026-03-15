import numpy as np


def crear_tablero(tamano=10):
    """
    Crea un tablero cuadrado usando numpy.

    Parameters
    ----------
    tamano : int
        Tamaño del tablero (default = 10)

    Returns
    -------
    numpy.ndarray
        Matriz representando el tablero
    """

    tablero = np.full((tamano, tamano), " ")

    return tablero


def mostrar_tablero(tablero):
    letras = "ABCDEFGHIJ"
    print("   " + " ".join(letras))
    print("  " + "-" * 20)
    for i, fila in enumerate(tablero):
        print(f"{i} | " + " ".join(c if c != " " else "~" for c in fila))
