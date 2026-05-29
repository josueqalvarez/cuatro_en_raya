class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.derecha = None
        self.izquierda = None

class DoubleLinkedList:
    def __init__(self):
        self.home = None
        self.tail = None
        self.size = 0

    def prepend(self, nuevo_nodo: Nodo):
        
        if (self.home = None):
            self.home = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            temp = self.home
            self.home = nuevo_nodo
            self.home.derecha = temp
            temp.izquierda = self.home
        
        self.size += 1
    
    
    def append(self, nuevo_nodo: Nodo):



    def shift(self):
        if (self.home = None or self.home.derecha):
            print("No hay nodos suficientes")
        else:
            self.home = self.home.derecha
            self.izquierda = None

        self.size -= 1


    del pop(self):
        if (self.home = None or self.home.derecha):
            print("No hay nodos suficientes")
        else:
            self.tail = self.tail.izquierda
            self.tail.derecha = None

        self.size -= 1

