from src.board import crear_tablero, mostrar_tablero
from src.ships import colocar_flota

tablero = crear_tablero()

colocar_flota(tablero)

mostrar_tablero(tablero)
