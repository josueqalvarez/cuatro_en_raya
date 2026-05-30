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
        
        if self.home == None:
            self.home = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            temp = self.home
            self.home = nuevo_nodo
            self.home.derecha = temp
            temp.izquierda = self.home
            
            if temp.derecha == None:
                self.tail = temp

        self.size += 1
    
    
    def append(self, nuevo_nodo: Nodo):
        
        if self.home == None:
            self.home = nuevo_nodo
            self.tail = nuevo_nodo
        elif self.home.derecha == None:
            self.tail = nuevo_nodo
            self.tail.izquierda = self.home
            self.home.derecha = self.tail
        else:
            temp = self.tail
            temp.derecha = nuevo_nodo
            nuevo_nodo.izquierda = temp
            self.tail = temp
        
        self.size += 1


    def shift(self):
        if self.home == None or self.home.derecha:
            print("No hay nodos suficientes")
        else:
            self.home = self.home.derecha
            self.izquierda = None

        self.size -= 1


    def pop(self):
        if self.home == None or self.home.derecha:
            print("No hay nodos suficientes")
        else:
            self.tail = self.tail.izquierda
            self.tail.derecha = None

        self.size -= 1


    def get(self, indice):
        
        temp = self.home

        if indice <= self.size and indice > 0:
            for i in range(indice):
                if (i+1) == indice:
                    print(i+1 , " ", temp.valor)
                else:
                    temp = temp.derecha



dll = DoubleLinkedList()

dll.prepend(Nodo("primero"))
dll.append(Nodo("segundo"))
dll.append(Nodo("tercero"))
dll.get(3)
