import numpy as np


def crear_tablero(tamano=10):
    """
    Create a square game board using NumPy.

    tamano :
        Size of the board (default = 10).

    """

    # Create a matrix filled with empty spaces representing water
    tablero = np.full((tamano, tamano), " ")

    return tablero


def mostrar_tablero(tablero):
    """
    Display the game board in the console in a visual format.

    The function converts internal board symbols into emojis
    so the player can easily understand the board state.

    Internal representation:
        " " -> empty water
        "O" -> ship position

    Visual representation:
        🌊 -> water
        🚢 -> ship
        💥 -> hit
        ❌ -> miss
    """

    # Column labels (A–J) shown at the top of the board (JUST VISUAL)
    letras = "ABCDEFGHIJ"

    # Print column headers (JUST VISUAL)
    print("   " + " ".join(letras))

    # Print horizontal separator (JUST VISUAL)
    print("  " + "-" * 20)

    # Iterate through each row of the board
    for i, fila in enumerate(tablero):

        # This list will store the visual representation of the row
        fila_visual = []

        # Iterate through each cell in the row
        for celda in fila:

            # Convert internal board values to visual symbols
            if celda == " ":
                fila_visual.append("🌊")

            elif celda == "O":
                fila_visual.append("🚢")

            elif celda == "X":
                fila_visual.append("💥")

            elif celda == "-":
                fila_visual.append("❌")

            else:
                fila_visual.append(celda)

    # Print row number and visual row content
        print(f"{i} | " + " ".join(fila_visual))
