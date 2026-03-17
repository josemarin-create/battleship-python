from src.utils import convertir_coordenada


def barco_hundido(tablero, fila, columna):
    """
    Check if the ship that was hit has been completely destroyed.
    """

    for i in range(max(0, fila - 1), min(10, fila + 2)):
        for j in range(max(0, columna - 1), min(10, columna + 2)):
            if tablero[i][j] == "O":
                return False

    return True


def disparar(tablero):
    """
    Ask the player for a coordinate and perform a shot on the board.
    The player can type 'r' or 'restart' to restart the game.
    """

    while True:

        coordenada = input(
            "Enter coordinate (e.g., B7) or 'r' to restart: "
        ).lower().strip()

        # restart command
        if coordenada in ["r", "restart"]:
            return "restart"

        try:
            fila, columna = convertir_coordenada(coordenada)

            if fila < 0 or fila > 9 or columna < 0 or columna > 9:
                print("Invalid coordinate. Try again.")
                continue

            break

        except Exception:
            print("Invalid coordinate. Try again.")

    # Evaluate the shot
    if tablero[fila][columna] == "O":

        print("💥 Hit!")
        tablero[fila][columna] = "X"

        if barco_hundido(tablero, fila, columna):
            print("🚢 Ship destroyed!")

    elif tablero[fila][columna] == " ":

        print("❌ Miss!")
        tablero[fila][columna] = "-"

    else:

        print("You already shot here.")


def quedan_barcos(tablero):
    """
    Check if there are remaining ships on the board.

    Returns
    -------
    bool
        True if ships remain, False if all ships are destroyed.
    """

    for fila in tablero:
        for celda in fila:
            if celda == "O":
                return True

    return False
