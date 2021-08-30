class Nodo_lista:
    def __init__(self, information=None, next=None):
        self.information=information
        self.next=next

class NodoEncabezado:
    def __init__(self, ejeE=None, nextE=None, beforeE=None, next_node_matriz=None):
        self.ejeE = ejeE
        self.nextE = nextE
        self.beforeE = beforeE
        # Es el que apunta del nodo encabezado al nodo de la matriz
        self.next_node_matriz = next_node_matriz

class NodoMatriz:
    def __init__(self, number=None, rowM=None, columnM=None, nextM=None, beforeM=None, upM=None, downM=None):
        self.number = number
        self.rowM = rowM
        self.columnM = columnM
        self.nextM = nextM
        self.beforeM = beforeM
        self.upM = upM
        self.downM = downM        