import numpy as np


def crear_tablero(tamano=10):
    """
    Create a square game board using NumPy.

    Parameters
    ----------
    tamano : int
        Size of the board (default = 10).

    Returns
    -------
    numpy.ndarray
        A 2D array representing the game board filled with empty spaces.
    """

    # Create a matrix filled with empty spaces representing water
    tablero = np.full((tamano, tamano), " ")

    return tablero


def mostrar_tablero(tablero, ocultar_barcos=False):
    """
    Display the game board in the console using emojis.

    This function converts the internal board representation into a
    visual format that is easy for the player to understand.

    Parameters
    ----------
    tablero : numpy.ndarray
        The game board.
    ocultar_barcos : bool, optional
        If True, ships will be hidden (used for opponent view).

    Internal representation
    -----------------------
    " " -> empty water
    "O" -> ship
    "X" -> hit
    "-" -> miss

    Visual representation
    ---------------------
    🌊 -> water
    🚢 -> ship
    💥 -> hit
    ❌ -> miss
    """

    # Column labels (A–J)
    letras = "ABCDEFGHIJ"

    # Print column headers
    print("   " + " ".join(letras))

    # Print separator
    print("  " + "-" * 20)

    # Iterate through each row
    for i, fila in enumerate(tablero):

        fila_visual = []

        for celda in fila:

            if celda == " ":
                fila_visual.append("🌊")

            elif celda == "O":
                if ocultar_barcos:
                    fila_visual.append("🌊")
                else:
                    fila_visual.append("🚢")

            elif celda == "X":
                fila_visual.append("💥")

            elif celda == "-":
                fila_visual.append("❌")

            else:
                fila_visual.append(celda)

        # Print row
        print(f"{i} | " + " ".join(fila_visual))
