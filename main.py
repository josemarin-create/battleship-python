from src.board import crear_tablero, mostrar_tablero
from src.ships import colocar_flota
from src.game import disparar, quedan_barcos

tablero = crear_tablero()

colocar_flota(tablero)

while quedan_barcos(tablero):

    mostrar_tablero(tablero)

    disparar(tablero)

print("🎉 ALL SHIPS DESTROYED")
print("🏆 YOU WIN!")
