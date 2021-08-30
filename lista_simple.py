from nodo import*

class Lista_simple:
    # Constructor
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    # Metódo insertar
    def insert(self, info):
        newNodo=Nodo_lista(information=info)
        if self.head == None:
            self.head=self.tail=newNodo
            print('Se inserto al principio de la lista')
        else:
            self.tail.next=newNodo
            self.tail=newNodo
            print('Se inserto')
        self.size+=1
        print(self.size)
    # Metódo mostrar
    def show(self):
        if self.head == None:
            print('La lista esta vacia')
        else:
            current_node=self.head
            while current_node != None:
                current_node.information.show_datos()
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
                if new_node.information.get_name() == name:
                    print('Ya existe no se agrego :(')
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
                if new_node.information.get_name() == name:
                    return new_node.information
                new_node=new_node.next