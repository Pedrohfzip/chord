

# Mudar nodo para cada um ter uma lista e se é ativo ou não

# Procura no primeiro nodo ativo que encontrar  
# O proximo é ativo ? Se não, procura o valor nele, 
# Se o proximo nodo for ativo para a loop e vai pro proximo nodo ativo procurar os valores 

class Nodo():
    def __init__(self,data):
        self.data = data
        self.next = None



class CircleList():
        def __init__(self):
             self.first = None
             self.last = None

        
        def empty(self):
             return self.first == None
        
        def addInit(self, data):
            if self.empty():
                self.first = self.last = Nodo(data)
                self.last.next = self.first
            else:
                aux = Nodo(data)
                aux.next = self.first
                self.first = aux
                self.last.next = self.first
                
        def addEnd(self, data):
            if self.empty():
                 self.first = self.last = Nodo(data)
                 self.last.next = self.first
            else:
                 aux = self.last
                 self.last = aux.next = Nodo(data)
                 self.last.next = self.first

        def removeInit(self):
            if self.empty():
                print("List empty")
            elif self.first == self.last:
                self.first = self.last = None
            else:
                self.first = self.first.next
                self.last.next = self.first 

        def removeEnd(self):
            if self.empty():
                print("List empty")
            elif self.first == self.last:
                self.first = self.last = None
            else:
                aux = self.first
                while aux.next != self.last:
                    aux = aux.next
                aux.next = self.first
                self.last = aux
        def runList(self):
            if(self.first == None):
                 print("List empty")
            else:
                aux = self.first
                while aux.next != self.first:
                    print(aux.data)
                    aux = aux.next
                print(aux.data)      
                       


lista = CircleList()
lista.addEnd(10)
lista.addEnd(20)
lista.addEnd(30)
lista.addEnd(40)
lista.addEnd(50)
lista.addEnd(60)
lista.addInit(70)
lista.removeEnd()
lista.runList()
