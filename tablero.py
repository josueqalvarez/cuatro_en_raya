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

