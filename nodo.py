class Nodo_lista:
    def __init__(self, node_name=None, node_position_begin=None, node_position_end=None, node_matriz=None, next=None):
        self.node_name=node_name
        self.node_position_begin=node_position_begin
        self.node_position_end=node_position_end
        self.node_matriz=node_matriz
        self.next=next

class Info_position:
    def __init__(self,node_position_x=None, node_position_y=None):
        self.node_position_x=node_position_x
        self.node_position_y=node_position_y

class Nodo():    
    def __init__(self, name_T=None, coordenate_x=None, coordenate_y=None, size_matriz_x=None, size_matriz_y=None):
        self.name_T = name_T
        self.coordenate_x = coordenate_x
        self.coordenate_y = coordenate_y
        self.size_matriz_x = size_matriz_x
        self.size_matriz_y = size_matriz_y

class NodoEncabezado():
    def __init__(self,informationE=None, nextE=None, beforeE=None, node=None):
        self.informationE = informationE
        self.nextE = nextE
        self.beforeE = beforeE
        self.node = node

class NodoMatriz():
    def __init__(self, number=None, columnM=None, rowM=None, nextM=None, beforeM=None, upM=None, downM=None):
        self.number = number
        self.columnM = columnM
        self.rowM = rowM
        self.nextM = nextM
        self.beforeM = beforeM
        self.upM = upM
        self.downM = downM        