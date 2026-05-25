class Tablero:
    def __init__(self, filas = 6, columnas = 7):
        self.columnas = columnas
        self.filas = filas

    def mostrar(self):
        for fil in range(self.filas):
            fila_tablero = ""
            for col in range(self.columnas):
                fila_tablero = fila_tablero + "⚪️ "
            print(f'{fila_tablero}\n')

    def mover_ficha(self, jugador: Jugador, fila, columna):
        while (True):
            fil = input("Ingresa el N° de fila")
            col = input("Ingresa el N° de columna")

            if not (fil > 0 and fil <= self.filas):
                err = "filas"
            else if (col > 0 and col <= self.columnas):
                col = "columnas"

        
