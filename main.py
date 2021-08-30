from os import startfile, system, write
from xml.dom import minidom
from lista_simple import*
from matriz_ortogonal import*

list_simple=Lista_simple()

def cargar_archivo():
    ruta=str(input('Ingrese ruta del archivo: '))
    try:
        archivo=open(ruta,mode='r')
        archivo_cargado=minidom.parse(archivo)
        terreno=archivo_cargado.getElementsByTagName('terreno')
        # Cuantas matrices tiene
        print('\nCantidad de terrenos: ',terreno.length)
        for hijo in terreno:
            # Nombre de los terrenos
            name=hijo.getAttribute('nombre')
            print('\nNombre del terreno: ', name) 
            # Dimension de la matriz
            for subHijo in hijo.getElementsByTagName('dimension'):
                print('Dimesion: ')
                # x
                for subSubHijo in subHijo.getElementsByTagName('m'):
                    dimension_x=int(subSubHijo.firstChild.data)
                    print('x: ',dimension_x, end=', ')
                # y
                for subSubHijo in subHijo.getElementsByTagName('n'):
                    dimension_y=int(subSubHijo.firstChild.data)
                    print('y: ',dimension_y)
            # Posicion inicial
            for subHijo in hijo.getElementsByTagName('posicioninicio'):
                print('Posicion inicial: ')
                for subSubHijo in subHijo.getElementsByTagName('x'):
                    position_begin_x=subSubHijo.firstChild.data
                    print('x: ',subSubHijo.firstChild.data, end=', ')
                for subSubHijo in subHijo.getElementsByTagName('y'):
                    position_begin_y=subSubHijo.firstChild.data
                    print('y: ',subSubHijo.firstChild.data)
            # Posicion final
            for subHijo in hijo.getElementsByTagName('posicionfin'):
                print('Posicion final: ')
                for subSubHijo in subHijo.getElementsByTagName('x'):
                    position_end_x=subSubHijo.firstChild.data
                    print('x: ',subSubHijo.firstChild.data, end=', ')
                for subSubHijo in subHijo.getElementsByTagName('y'):
                    position_end_y=subSubHijo.firstChild.data
                    print('y: ',subSubHijo.firstChild.data)
                print()
            matriz_ortogonal=Lista_ortogonal(name_T=name,size_x=dimension_x,size_y=dimension_y,position_begin_x=position_begin_x,
            position_begin_y=position_begin_y,position_end_x=position_end_x,position_end_y=position_end_y)
            list_simple.insert(matriz_ortogonal)
            # Posicion
            # Se encuentran las posiciones de x, y y el valor que almacena
            for subHijo in hijo.getElementsByTagName('posicion'):
                position_matriz_x=int(subHijo.getAttribute('x'))
                position_matriz_y=int(subHijo.getAttribute('y'))
                number_matriz=int(subHijo.firstChild.data)
                print('x: ',position_matriz_x,', y: ',position_matriz_y,'=',number_matriz)
                matriz_ortogonal.insert_ortogonal(number_matriz,position_matriz_x,position_matriz_y,dimension_x,dimension_y)
                matriz_ortogonal.show_ortogonal(position_matriz_x,position_matriz_y)
            print()
            list_simple.show()
    except:
        print('No se puede abrir el archivo')

def procesar_archivo():
    nombre_terreno=input('Ingrese nombre de terreno que desee: ')
    list_simple.search(nombre_terreno)

def escribir_archivo_salida():
    pass

def generar_grafica():
    nombre_terreno=input('Ingrese nombre de terreno que desee: ')
    search_name=list_simple.search(nombre_terreno)
    if search_name:
        grafica='''
        digraph L{
        node[shape=box fillcolor="#FFEDBB" style=filled]
        subgraph cluster_p{'''
        grafica+='label= %s '% search_name.name_T 
        grafica+='bgcolor = "#900C3F"'
        grafica+='raiz[label = "0,0"]'
        grafica+='edge[dir = "both"]\n'
        
        aux_node_x=search_name.list_encabezado_x.headE
        current_node_row=aux_node_x.nextE
        #amarillo
        grafica+='Fila%s '% aux_node_x.ejeE+'[label = %s ,group=1,fillcolor="#FFC30F"];\n'% aux_node_x.ejeE
        while current_node_row:
            grafica+='Fila%s '% current_node_row.ejeE+'[label = %s ,group=1,fillcolor="#FFC30F"];\n'% current_node_row.ejeE
            #grafica+='Fila%s'% current_node_row.ejeE+'->'
            current_node_row=current_node_row.nextE
        
        node_x=search_name.list_encabezado_x.headE
        node_row=node_x.nextE
        grafica+='Fila1->'
        while node_row != None:
            grafica+='Fila%s'% node_row.ejeE+'->'
            node_row=node_row.nextE
        grafica+='None_x[label=""];\n'

        aux_node_y=search_name.list_encabezado_y.headE
        current_node_column=aux_node_y.nextE
        grafica+='Columna%s '% aux_node_y.ejeE+'[label = %s ,group=2,fillcolor="#FF5733"];\n'% aux_node_y.ejeE
        while current_node_column:
            grafica+='Columna%s '% current_node_column.ejeE+'[label = %s ,group=2,fillcolor="#FF5733"];\n'% current_node_column.ejeE
            current_node_column=current_node_column.nextE

        node_y=search_name.list_encabezado_y.headE
        node_column=node_y.nextE
        grafica+='Columna1->'
        while node_column != None:
            grafica+='Columna%s'% node_column.ejeE+'->'
            node_column=node_column.nextE
        grafica+='None_y[label=""];\n'

        grafica+='raiz->Fila1;'
        grafica+='raiz->Columna1;\n'

        aux_node_y=search_name.list_encabezado_y.headE
        current_node_column=aux_node_y.nextE
        grafica+='{rank=same; raiz;'
        grafica+='Columna1 '
        while current_node_column:
            grafica+='Columna%s '% current_node_column.ejeE
            current_node_column=current_node_column.nextE
        grafica+='None_y;'
        grafica+='}\n'

        aux_node_x=search_name.list_encabezado_x.headE 
        current_node_row=aux_node_x.next_node_matriz
        while current_node_row != None:
            aux_node_y=search_name.list_encabezado_y.headE 
            current_node_column=aux_node_y.next_node_matriz
            current_node_column=current_node_row
            while current_node_column != None:
                grafica+='nodoFila%s'% current_node_column.rowM+'nodoColumna%s '% current_node_column.columnM+'[label ='+str(current_node_column.number)+', group='+str(current_node_column.columnM,)+', fillcolor="#C70039"];\n'
                current_node_column=current_node_column.downM
            current_node_row=current_node_row.nextM

        #auxnode_x=search_name.list_encabezado_x.headE
        #currentnode_row=auxnode_x.nextE
        #grafica+='Fila1->'
        #while currentnode_row:
        #    grafica+='Fila%s'% currentnode_row.ejeE+'->'
        #    currentnode_row=currentnode_row.nextE            

        aux_x_node_x=search_name.list_encabezado_x.headE 
        current_x_node_row=aux_x_node_x.next_node_matriz
        while current_x_node_row != None:
            aux_y_node_y=search_name.list_encabezado_y.headE 
            current_y_node_column=aux_y_node_y.next_node_matriz
            current_y_node_column=current_x_node_row
            while current_y_node_column != None:
                grafica+='nodoFila%s'% current_y_node_column.rowM+'nodoColumna%s '% current_y_node_column.columnM+'->'
                current_y_node_column=current_y_node_column.downM
            current_x_node_row=current_x_node_row.nextM
        grafica+='None_x_m[label=""];\n'

        grafica+='}'
        grafica+='}'
        archivo=open('grafica.dot','w')
        archivo.write(grafica)
        archivo.close()

        system('dot -Tpng grafica.dot -o grafica.png')
        system('cd ./grafica.png')
        startfile('grafica.png')
        
    else:
        print('No se encontro')
    
while True:
    print('\n<-------------------------------------------------->')
    print('<                       Menú                       >')
    print('<          1. Cargar archivo                       >')
    print('<          2. Procesar archivo                     >')
    print('<          3. Escribir archivo salida              >')
    print('<          4. Mostrar datos del estudiante         >')
    print('<          5. Generar gráfica                      >')
    print('<          6. Salida                               >')
    print('<-------------------------------------------------->')
    opcion=int(input('Ingrese una opción: '))
    if opcion==1:
        cargar_archivo()
    elif opcion==2:
        procesar_archivo()
    elif opcion==3:
        escribir_archivo_salida()
    elif opcion==4:
        print('\nCinthia Avex Nim Quiñonez Alvarez\n201801075\nIntroducción a la programación y computación 2 "E"\nIngenieria en Ciencias y Sistemas\n4to Semestre\n')
    elif opcion==5:
        generar_grafica()
    elif opcion==6:
        print('Fin del programa :)')
        exit()
    else:
        print('Opción incorrecta, vuelva a ingresar otra opción')