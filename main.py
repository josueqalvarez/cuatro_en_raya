from crear_jugador import Jugador
from tablero import Tablaero

jugador_1 = Jugador()
jugador_1.definir_datos()

jugador_2 = Jugador()
jugador_2.definir_datos()

tablero = Tablero()

print(f"Rojos empiezan. \nTurno de {jugador_1.nombre}")


tablero.mostrar()
