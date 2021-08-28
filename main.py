from os import startfile, system, write
from xml.dom import minidom
from lista_simple import*
from matriz_ortogonal import*

list_simple=Lista_simple()

def cargar_archivo():
    global terreno, name, posicion, position_begin_x, position_begin_y, position_end_x, position_end_y, position_matriz_x, position_matriz_y, number_matriz
    global dimension_x, dimension_y
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
    if list_simple.search(nombre_terreno):
        grafica='''
        digraph L{
        node[shape=box fillcolor="#FFEDBB" style=filled]
        subgraph cluster_p{'''
        grafica+='label= %s '% nombre_terreno
        grafica+='bgcolor = "#900C3F"'
        grafica+='raiz[label = "0,0"]'
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
    print('<-------------------------------------------------->')
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