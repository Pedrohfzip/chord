



import hashlib

class Nodo():
    def __init__(self, data, is_active=False):
        self.data = data
        self.next = None
        self.values = []  # Lista para armazenar valores
        self.is_active = is_active  # Indicador de ativo ou não
        # self.finger_table = {}  # Tabela de finger

    def deactivate(self):
        self.is_active = False

class CircleList():
    def __init__(self):
        self.first = None
        self.last = None
        self.active_nodes = []  # Lista para armazenar os nós ativos

    def empty(self):
        return self.first == None

    def activateNode(self, data):
        node = self.first
        while node:
            if node.data == data:
                if not node.is_active:
                    node.is_active = True
                    self.active_nodes.append(node)
                    self.active_nodes.sort(key=lambda x: x.data)
                    # Transferir dados de volta para o nó ativado
                    self.transfer_data_back(node)
                return
            node = node.next
        print("Node not found")

    def deactivateNode(self, data):
        for i, node in enumerate(self.active_nodes):
            if node.data == data:
                node.deactivate()
                self.transfer_data(node, self.active_nodes[(i + 1) % len(self.active_nodes)])
                self.active_nodes.remove(node)
                return
        print("Node not found or already inactive.")

    def transfer_data(self, origin_node, target_node):
        target_node.values.extend(origin_node.values)
        origin_node.values = []

    def transfer_data_back(self, node):
        for active_node in self.active_nodes:
            if active_node != node:
                node_values = [value for value in active_node.values if self.hash_function(value) == self.active_nodes.index(node)]
                node.values.extend(node_values)
                active_node.values = [value for value in active_node.values if self.hash_function(value) != self.active_nodes.index(node)]


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
        if self.empty():
            print("List empty")
        else:
            aux = self.first
            while aux.next != self.first:
                print("Data:", aux.data, "Active:", aux.is_active)
                print("Values:", aux.values)
                # print("Finger Table:", aux.finger_table)
                aux = aux.next
            print("Data:", aux.data, "Active:", aux.is_active)
            print("Values:", aux.values)
            print("Data:", aux.next.data, "Active:", aux.next.is_active)
            print("Values:", aux.next.values)
            # print("Finger Table:", aux.finger_table)

    def hash_function(self, key):
        return int(hashlib.sha1(str(key).encode()).hexdigest(), 16) % len(self.active_nodes)

    def insert_data(self, value):
        if not self.active_nodes:
            print("No active nodes.")
            return

        index = self.hash_function(value)
        active_node = self.active_nodes[index]
        active_node.values.append(value)

    def search_value(self, value):
        for node in self.active_nodes:
            node = node
            while True:
                if value in node.values:
                    print(f"Value '{value}' found in Node ID: {node.data}")
                    return
                node = node.next
                if node == node:
                    break
        print(f"Value '{value}' not found in any active node.")


# Criando a lista circular e ativando os nós desejados
lista = CircleList()
for i in range(20):
    lista.addEnd(i)

lista.activateNode(1)
lista.activateNode(5)
lista.activateNode(7)
lista.activateNode(9)



# Construindo a finger table para os nós ativos
# lista.build_finger_table()

# Exibindo a lista circular com informações sobre nós ativos e suas finger tables



# Inserindo valores nos nós ativos
lista.insert_data(10)
lista.insert_data(20)
lista.insert_data(30)
lista.insert_data(40)
lista.insert_data(50)
lista.insert_data(60)
lista.insert_data(12370)
lista.insert_data(2230)
lista.insert_data(32320)
lista.insert_data(42320)
lista.insert_data(52320)
lista.insert_data(6330)
lista.insert_data(704)

lista.runList()
print("\n\n\n")
# Desativando um nó e transferindo os valores
lista.deactivateNode(5)
print("\n\n\n")
lista.runList()

# Ativando novamente um nó
lista.activateNode(5)
print("\n\n\n")
lista.runList()

# Procurando valores na lista
lista.search_value(42320)
lista.search_value(3)


