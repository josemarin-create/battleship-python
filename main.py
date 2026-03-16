from src.board import crear_tablero, mostrar_tablero
from src.ships import colocar_flota
from src.game import disparar

tablero = crear_tablero()

colocar_flota(tablero)

while True:

    mostrar_tablero(tablero)

    disparar(tablero)
