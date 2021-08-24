from nodo import*
from lista_simple import*
from matriz_ortogonal import*

class Lista_simple:
    # Constructor
    def __init__(self,name_matriz,size_x,size_y):
        self.head=None
        self.tail=None
        list_info_matriz=Lista_ortogonal(name_matriz=name_matriz,size_x=size_x,size_y=size_y)
        self.node_info_matriz=Nodo_lista(None,None,None,list_info_matriz)
        self.size=0
    
    # Metódo insertar
    def insert(self, name, position_begin_x, position_begin_y, position_end_x, position_end_y, position_matriz_x, position_matriz_y, number_matriz):
        newNodo=Nodo_lista(node_name=name, node_position_begin= Info_position(node_position_x=position_begin_x, node_position_y=position_begin_y), 
        node_position_end= Info_position(node_position_x=position_end_x, node_position_y=position_end_y), 
        node_matriz=self.node_info_matriz.node_matriz.insert_ortogonal(number=number_matriz, column=position_matriz_x, row=position_matriz_y)) 
        if self.head == None:
            self.head=self.tail=newNodo
        else:
            if self.exist(name)==True:
                pass
            else:
                self.tail.next=newNodo
                # Almacena el ultimo dato ingresado en la lista
                self.tail=newNodo
        self.size+=1
    # Metódo mostrar
    def show(self,colum,row):
        if self.head == None:
            print('La lista esta vacia')
        else:
            current_node=self.head
            while current_node != None:
                print('Nombre: ',current_node.node_name,
                ', Posicion inicial x: ', current_node.node_position_begin.node_position_x,
                ', Posicion inicial y: ', current_node.node_position_begin.node_position_y,
                ', Posicion final x: ', current_node.node_position_end.node_position_x,
                ', Posicion final y: ', current_node.node_position_end.node_position_y,
                ', Matriz: ',end='') 
                self.node_info_matriz.node_matriz.show_ortogonal(coordenada_x= colum, coordenada_y=row)
                print(end='->')
                current_node=current_node.next
            print('None')
    # Metodo existe el nombre del terreno 
    def exist(self, name):
        new_node=self.head
        if new_node == None:
            print('La lista esta vacia')
            return False
        else: 
            node_exist=False
            new_node=self.head
            while new_node != None:
                if new_node.node_name == name:
                    #print('Ya existe no se agrego :(')
                    node_exist=True
                new_node=new_node.next
        return node_exist
    # Metódo buscar el nombre del terreno
    def search(self,name):
        new_node=self.head
        if self.head == None:
            print('La lista esta vacia')
        else:
            while new_node != None:
                if name in new_node.node_name:
                    print('Se encontro: ',new_node.node_name)
                    return new_node
                new_node=new_node.next