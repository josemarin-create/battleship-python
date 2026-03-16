from src.utils import convertir_coordenada


def disparar(tablero):
    """
    Ask the player for a coordinate and perform a shot on the board.

    Parameters
    ----------
    tablero : numpy.ndarray
        Game board.

    Returns
    -------
    None
    """

    coordenada = input("Enter coordinate (e.g., B7): ")

    fila, columna = convertir_coordenada(coordenada)

    if tablero[fila][columna] == "O":

        print("💥 Hit!")

        tablero[fila][columna] = "X"

    elif tablero[fila][columna] == " ":

        print("❌ Miss!")

        tablero[fila][columna] = "-"

    else:

        print("You already shot here.")
