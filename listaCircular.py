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
             pass
        def removeEnd(self):
             pass

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
lista.runList()
