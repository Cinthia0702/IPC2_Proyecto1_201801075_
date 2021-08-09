from nodo import*

class Lista_simple:
    # Constructor
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    # Metódo insertar
    def insert(self, dato):
        newNodo=Nodo(dato)
        if self.head == None:
            self.head=newNodo
        else:
            self.tail.next=newNodo
        # Almacena el ultimo dato ingresado en la lista
        self.tail=newNodo
        self.size+=1
    # Metódo mostrar
    def show(self):
        if self.head == None:
            print('La lista esta vacia')
        else:
            current_node=self.head
            while current_node != None:
                print(current_node.dato,end='->')
                current_node=current_node.next
            print('None')