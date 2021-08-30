from lista_doble import Lista_Doble_Encabezado
from nodo import NodoMatriz
from nodo import NodoEncabezado

class Lista_ortogonal:
    def __init__(self, name_T=None, size_x=None, size_y=None, position_begin_x=None, position_begin_y=None, position_end_x=None, position_end_y=None):
        self.name_T=name_T
        self.size_x=size_x
        self.size_y=size_y
        self.position_begin_x=position_begin_x
        self.position_begin_y=position_begin_y
        self.position_end_x=position_end_x
        self.position_end_y=position_end_y
        self.list_encabezado_x = Lista_Doble_Encabezado()
        self.list_encabezado_y = Lista_Doble_Encabezado()
        
    def show_datos(self):
        print('Nombre: ',self.name_T,', Dimensión en x: ',self.size_x,', Dimensión en y: ',self.size_y,
        ', Posición inicial x: ',self.position_begin_x,', Posición inicial y: ',self.position_begin_y,
        ', Posición final x: ',self.position_end_x,', Posición final y: ',self.position_end_y,end='->')

    def get_name(self):
        return self.name_T

    # Metodo insertar nodo en la matriz
    def insert_ortogonal(self, number, row, column, size_x:int, size_y:int):
        new_node_matriz = NodoMatriz(number=number, rowM=row, columnM=column) 
        if row<=size_x or column<=size_y:
            # Valida si no existe el nodo encabezado en el eje x=fila y en el eje y=columna y la inserta
            if self.list_encabezado_x.existLD(row) == False and self.list_encabezado_y.existLD(column) == False:    
                print('Se agrega un nuevo nodo cabecera a la fila y columna')
                node_head_row = NodoEncabezado(row)
                node_head_column = NodoEncabezado(column)
                # Nodo encabezado apunta al nodo matriz de columna o fila = nuevo nodo en la matriz
                node_head_row.next_node_matriz = new_node_matriz
                node_head_column.next_node_matriz = new_node_matriz
                # Inserta los valores a la lista encabezado x
                self.list_encabezado_x.insert_header(node_head_row)
                # Inserta los valores a la lista encabezado y
                self.list_encabezado_y.insert_header(node_head_column)
            # Valida si no existe el nodo encabazado en el eje x=fila y la inserta
            elif self.list_encabezado_x.existLD(row) == False and self.list_encabezado_y.existLD(column):
                print('Se agrego un nuevo nodo cabecera a la fila')
                node_head_row = NodoEncabezado(row)
                # Nodo encabezado apunta al primer nodo matriz de la fila = nuevo nodo en la matriz
                node_head_row.next_node_matriz = new_node_matriz
                self.list_encabezado_x.insert_header(node_head_row)
                # Buscamos una columna que ya existe
                aux_node = self.list_encabezado_y.searchLD(column)
                # como ya existe el nodo encabezado de la matriz de la columna se apunta a otro nodo 
                current_node = aux_node.next_node_matriz
                # Agregamos otro nodo a la columna
                while current_node.downM != None:
                    current_node = current_node.downM
                current_node.downM = new_node_matriz
                new_node_matriz.upM = current_node
            # Valida si no existe el nodo encabezado en el eje y=columna y la inserta
            elif self.list_encabezado_x.existLD(row) and self.list_encabezado_y.existLD(column) == False:
                print('Se agrego un nuevo nodo cabecera a la columna')
                node_head_column = NodoEncabezado(column)
                # Nodo encabezado apunta al primer nodo matriz de la columna = nuevo nodo en la matriz
                node_head_column.next_node_matriz = new_node_matriz
                self.list_encabezado_y.insert_header(node_head_column)
                # Buscamos una fila que ya existe
                aux_node = self.list_encabezado_x.searchLD(row)
                # como ya existe el nodo encabezado de la matriz de la fila se apunta a otro nodo
                current_node = aux_node.next_node_matriz
                # Agregamos otro nodo a la fila 
                while current_node.nextM != None:
                    current_node = current_node.nextM
                current_node.nextM = new_node_matriz
                new_node_matriz.beforeM = current_node
            # Valida si existe fila y columna para no insertar nada
            else:
                print('No se agrega un nuevo nodo cabecera a la columna ni a la fila porque ya existe')
                # Buscamos una columna que ya existe
                aux_node_column = self.list_encabezado_y.searchLD(column)
                # como ya existe el primer nodo matriz de la columna se apunta a otro nodo a la misma columna
                current_node_column = aux_node_column.next_node_matriz
                # Agregamos otro nodo a la columna con nodos matriz existentes
                while current_node_column.downM != None:
                    current_node_column = current_node_column.downM
                current_node_column.downM = new_node_matriz
                new_node_matriz.upM = current_node_column
                # Buscamos una fila que ya existe
                aux_node_row = self.list_encabezado_x.searchLD(row)
                # como ya existe el primer nodo matriz de la fila se apunta a otro nodo a la misma fila
                current_node_row = aux_node_row.next_node_matriz
                # Agregamos otro nodo a la fila con nodos matriz existentes
                while current_node_row.nextM != None:
                    current_node_row = current_node_row.nextM
                current_node_row.nextM = new_node_matriz
                new_node_matriz.beforeM = current_node_row
        else:
            print('Sale de los parametros')
    # Metodo mostrar
    def show_ortogonal(self,coordenada_x, coordenada_y):
        # Recorre en filas
        aux_node_row = self.list_encabezado_x.searchLD(coordenada_x)
        current_node_row = aux_node_row.next_node_matriz
        while current_node_row != None:
            # Recorre en columnas
            aux_node_column = self.list_encabezado_y.searchLD(coordenada_y)
            current_node_column = aux_node_column.next_node_matriz
            current_node_column = current_node_row
            while current_node_column != None:
                print('[',current_node_column.number,']')
                current_node_column = current_node_column.downM  
            current_node_row = current_node_row.nextM