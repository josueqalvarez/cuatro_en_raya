class Tablero:
    def __init__(self, filas = 6, columnas = 7):
        self.columnas = columnas
        self.filad = filas

    def mostrar(self):
        for col in range(self.columnas + 1):
            for fil in range(self.filas):
                print(0)
            print('\n')
