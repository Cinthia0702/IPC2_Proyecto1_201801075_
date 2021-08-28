class Nodo_lista:
    def __init__(self, information=None, next=None):
        self.information=information
        self.next=next

class Info_position:
    def __init__(self,node_position_x=None, node_position_y=None):
        self.node_position_x=node_position_x
        self.node_position_y=node_position_y

class Nodo:    
    def __init__(self, name_T=None, coordenate_x=None, coordenate_y=None, node_position_begin_x=None, node_position_begin_y=None, node_position_end_x=None, node_position_end_y=None, size_x=None, size_y=None):
        self.name_T=name_T
        self.coordenate_x = coordenate_x
        self.coordenate_y = coordenate_y
        self.node_position_begin_x=node_position_begin_x
        self.node_position_begin_y=node_position_begin_y
        self.node_position_end_x=node_position_end_x
        self.node_position_end_y=node_position_end_y
        self.size_x=size_x
        self.size_y=size_y

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