from InquirerPy import inquire

class Jugador:
    def __init__(self):
        self.nombre = None
        self.color_fichas = None

    def definir_datos(self):
        
        self.nombre = input("ingresa el nombre del jugador 1: ")
    
        self.color_fichas = inquirer.select(
        message="Ingresa el color de sus fichas:",
        choices=["🔴 Rojas","🟡 Amarillas"]).execute()


