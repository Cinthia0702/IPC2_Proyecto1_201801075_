from nodo import NodoEncabezado

class Lista_Doble_Encabezado:
    # Constructor
    def __init__(self):
        self.headE = None
        self.tailE = None
    # Metodo insertar en lista doblemente enlazada
    def insert_header(self,information):
        if self.headE==None:
            self.headE = self.tailE = information
        else: 
            new_node = self.tailE
            self.tailE = information
            information.beforeE = new_node
            new_node.nextE = information
    # Metodo mostrar en lista doblemente enlazada
    def show_header(self):
        if self.headE==None:
            print('Esta vacia')
        else:
            new_node = self.headE
            while(new_node != None):
                print(new_node.ejeE,end='->')
                new_node = new_node.nextE
            print('None')
    # Metodo validar si existe nodo en la lista 
    # doblemente enlazada
    def existLD(self, coordenate):
        new_node = self.headE
        if new_node == None :
            return False
        else:  
            while new_node != None:
                if coordenate == new_node.ejeE:
                    return True
                new_node = new_node.nextE
            return False
    # Metodo buscar si existe el nodo en la lista 
    # doblemente enlazada
    def searchLD(self,coordenate):
        new_node = self.headE
        if new_node==None:
            print('Esta vacia')
        else:
            while new_node != None:
                if (coordenate) == (new_node.ejeE):
                    return new_node
                new_node = new_node.nextE