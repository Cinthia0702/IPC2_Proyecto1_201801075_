from nodo import Nodo
from lista_doble import Lista_Doble_Encabezado
from nodo import NodoMatriz
from nodo import NodoEncabezado

class Lista_ortogonal():
    def __init__(self,name_matriz,size_x,size_y):
        list_encabezado_x = Lista_Doble_Encabezado()
        list_encabezado_y = Lista_Doble_Encabezado()
        self.first_node = Nodo(name_T=name_matriz, coordenate_x=list_encabezado_x, coordenate_y=list_encabezado_y, size_matriz_x=size_x,size_matriz_y=size_y)
    # Metodo insertar nodo en la matriz
    def insert_ortogonal(self, number, column, row):
        new_node_matriz = NodoMatriz(number=number,columnM=column,rowM=row) 
        # Valida si no existe la columna y fila para insertarla
        if self.first_node.coordenate_x.existLD(column) == False and self.first_node.coordenate_y.existLD(row) == False:
            #print('Se agrega nueva fila y columna')
            node_head_column = NodoEncabezado(column)
            node_head_row = NodoEncabezado(row)
            node_head_column.node = new_node_matriz
            node_head_row.node = new_node_matriz
            self.first_node.coordenate_y.insert_header(node_head_row)
            self.first_node.coordenate_x.insert_header(node_head_column)
        # Valida si no existe la columna la inserta en la matriz
        elif self.first_node.coordenate_x.existLD(column) == False and self.first_node.coordenate_y.existLD(row):
            #print('Se agrego nueva columna')
            aux_node = self.first_node.coordenate_y.searchLD(row)
            current_node = aux_node.node
            node_head_column = NodoEncabezado(column)
            node_head_column.node = new_node_matriz
            self.first_node.coordenate_x.insert_header(node_head_column)
            while current_node.nextM != None:
                current_node = current_node.nextM
            current_node.nextM = new_node_matriz
            new_node_matriz.beforeM = current_node
        # Valida si no existe la fila la inserta en la matriz
        elif self.first_node.coordenate_x.existLD(column) and self.first_node.coordenate_y.existLD(row) == False:
            #print('Se agrego nueva fila')
            aux_node = self.first_node.coordenate_x.searchLD(column)
            current_node = aux_node.node
            node_head_row = NodoEncabezado(row)
            node_head_row.node = new_node_matriz
            self.first_node.coordenate_y.insert_header(node_head_row)
            while current_node.downM != None:
                current_node = current_node.downM
            current_node.downM = new_node_matriz
            new_node_matriz.upM = current_node
        # Valida si existe fila y columna para no insertar nada
        else:
            #print('No se inserta ni columna ni fila porque ya existe')
            aux_node_column = self.first_node.coordenate_x.searchLD(column)
            current_node_column = aux_node_column.node
            while current_node_column.downM != None:
                current_node_column = current_node_column.downM
            current_node_column.downM = new_node_matriz
            new_node_matriz.upM = current_node_column
            
            aux_node_row = self.first_node.coordenate_y.searchLD(row)
            current_node_row = aux_node_row.node
            while current_node_row.nextM != None:
                current_node_row = current_node_row.nextM
            current_node_row.nextM = new_node_matriz
            new_node_matriz.beforeM = current_node_row
    # Metodo mostrar
    def show_ortogonal(self, coordenada_x, coordenada_y):
        aux_node_column = self.first_node.coordenate_x.searchLD(coordenada_x)
        current_node_column = aux_node_column.node
        print('x '+str(coordenada_x)+': ')
        #print('x: ')
        while current_node_column != None:
            #self.first_node.coordenate_x.show_header()
            print(current_node_column.number,' ', end = '') 
            current_node_column = current_node_column.downM
        print('')

        aux_node_row = self.first_node.coordenate_y.searchLD(coordenada_y)
        current_node_row = aux_node_row.node
        print('y '+str(coordenada_y)+': ')
        #print('y: ')
        while current_node_row != None:
            #self.first_node.coordenate_y.show_header()
            print(current_node_row.number,' ', end = '') 
            current_node_row = current_node_row.nextM 
        print('')