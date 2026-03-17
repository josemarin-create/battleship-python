from src.board import crear_tablero, mostrar_tablero
from src.ships import colocar_flota
from src.game import disparar, quedan_barcos
from src.utils import limpiar_pantalla


while True:

    tablero_p1 = crear_tablero()
    tablero_p2 = crear_tablero()

    colocar_flota(tablero_p1)
    colocar_flota(tablero_p2)

    turno = 1
    restart = False

    while quedan_barcos(tablero_p1) and quedan_barcos(tablero_p2):

        limpiar_pantalla()

        if turno == 1:

            print("PLAYER 1 TURN\n")

            mostrar_tablero(tablero_p2, ocultar_barcos=True)

            resultado = disparar(tablero_p2)

            if resultado == "restart":
                restart = True
                break

            turno = 2

        else:

            print("PLAYER 2 TURN\n")

            mostrar_tablero(tablero_p1, ocultar_barcos=True)

            resultado = disparar(tablero_p1)

            if resultado == "restart":
                restart = True
                break

            turno = 1

    if restart:
        limpiar_pantalla()
        print("🔄 Game restarted!\n")
        continue

    limpiar_pantalla()

    if not quedan_barcos(tablero_p1):
        print("🏆 PLAYER 2 WINS!")
    else:
        print("🏆 PLAYER 1 WINS!")

    jugar_otra = input("\nPlay again? (y/n): ").lower()

    if jugar_otra != "y":
        print("Thanks for playing Battleship!")
        break
