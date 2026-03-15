import random

# Ship sizes for the classic Battleship fleet
BARCOS = [5, 4, 3, 3, 2]


def generar_barco(tamano):
    """
    Generate random ship coordinates.

    The ship can be placed either horizontally or vertically
    starting from a random position on the board.

    Parameters
    ----------
    tamano : int
        Length of the ship

    Returns
    -------
    list of tuple
        List of coordinates representing the ship positions
    """

    orientacion = random.choice(["horizontal", "vertical"])

    fila = random.randint(0, 9)
    columna = random.randint(0, 9)

    coordenadas = []

    if orientacion == "horizontal":

        for i in range(tamano):
            coordenadas.append((fila, columna + i))

    else:

        for i in range(tamano):
            coordenadas.append((fila + i, columna))

    return coordenadas


def validar_barco(tablero, barco):
    """
    Validate if a generated ship can be placed on the board.

    Conditions checked:
    - The ship must stay inside the board limits
    - The ship cannot overlap with other ships
    - The ship cannot touch other ships (even diagonally)

    Parameters
    ----------
    tablero : numpy.ndarray
        Game board
    barco : list of tuple
        Coordinates of the ship

    Returns
    -------
    bool
        True if the ship placement is valid
    """

    for fila, columna in barco:

        # Check board boundaries
        if fila < 0 or fila >= 10 or columna < 0 or columna >= 10:
            return False

        # Check collision with other ships
        if tablero[fila][columna] == "O":
            return False

        # Check neighbouring cells
        for i in range(fila - 1, fila + 2):
            for j in range(columna - 1, columna + 2):

                if 0 <= i < 10 and 0 <= j < 10:

                    if tablero[i][j] == "O":
                        return False

    return True


def colocar_barco(tablero, barco):
    """
    Place a ship on the board by marking its coordinates.

    Parameters
    ----------
    tablero : numpy.ndarray
        Game board
    barco : list of tuple
        Ship coordinates
    """

    for fila, columna in barco:
        tablero[fila][columna] = "O"


def colocar_flota(tablero):
    """
    Place the entire fleet randomly on the board.

    Ships will be generated and validated until
    a valid placement is found.

    Parameters
    ----------
    tablero : numpy.ndarray
        Game board
    """

    for tamano in BARCOS:

        colocado = False

        while not colocado:

            barco = generar_barco(tamano)

            if validar_barco(tablero, barco):

                colocar_barco(tablero, barco)

                colocado = True
