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

        fil_ver = True
        col_ver = True

        while (True):

            if (fil_ver):
                fil = input("Ingresa el N° de fila")
                if (fil < 1 or fil > self.filas):
                    print(f'El numero de fila debe ser entre 1 y {self.filas}')                                                 continue
                else:    
                    fil_ver = False

            if (col_ver):
                col = input("Ingresa el N° de columna")
                if (col < 1 or col > self.colummas):
                    print(f'El numero de fila debe ser entre 1 y {self.columnas}')
                    continue
                else:
                    col_ver = False

           print(f'Fila: {fil}, Columna: {col}')

        
