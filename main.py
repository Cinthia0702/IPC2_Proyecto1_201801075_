from xml.dom import minidom

def cargar_archivo():
    global terreno, name, posicion, position_begin_x, position_begin_y, position_end_x, position_end_y, position_matriz_x, position_matriz_y, number_matriz
    ruta=str(input('Ingrese ruta sel archivo: '))
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
            # Posicion inicial
            posicioninicio=hijo.getElementsByTagName('posicioninicio')
            # Posicion final
            posicionfin=hijo.getElementsByTagName('posicionfin')
            # Posicion
            posicion=hijo.getElementsByTagName('posicion')
            for subHijo in posicioninicio:
                x=subHijo.getElementsByTagName('x')
                y=subHijo.getElementsByTagName('y')
                print('Posicion inicial: ')
                for subSubHijo in x:
                    position_begin_x=subSubHijo.firstChild.data
                    print('x: ',subSubHijo.firstChild.data, end=', ')
                for subSubHijo in y:
                    position_begin_y=subSubHijo.firstChild.data
                    print('y: ',subSubHijo.firstChild.data)
            for subHijo in posicionfin:
                x=subHijo.getElementsByTagName('x')
                y=subHijo.getElementsByTagName('y')
                print('Posicion final: ')
                for subSubHijo in x:
                    position_end_x=subSubHijo.firstChild.data
                    print('x: ',subSubHijo.firstChild.data, end=', ')
                for subSubHijo in y:
                    position_end_y=subSubHijo.firstChild.data
                    print('y: ',subSubHijo.firstChild.data)
                print()
            # Se encuentra el valor maximo del eje x y del eje y
            for subHijo in posicion:
                position_x=int(subHijo.getAttribute('x'))
                position_y=int(subHijo.getAttribute('y'))
            x=position_x
            print('Cantidad de columnas: ',x,end=' ')
            y=position_y
            print('Cantidad de filas: ',y)
            #list_simple=Lista_simple(name_matriz=name,size_x=x,size_y=y)
            #matriz_ortogonal=Lista_ortogonal(name,x,y)
            # Se encuentran las posiciones de x, y y el valor que almacena
            for subHijo in posicion:
                position_matriz_x=int(subHijo.getAttribute('x'))
                position_matriz_y=int(subHijo.getAttribute('y'))
                number_matriz=int(subHijo.firstChild.data)
                print('x: ',subHijo.getAttribute('x'),', y: ',subHijo.getAttribute('y'),end=' = ')
                print(subHijo.firstChild.data)
                #list_simple.insert(name,position_begin_x,position_begin_y,position_end_x,position_end_y,position_matriz_x,position_matriz_y,number_matriz)
                #matriz_ortogonal.insert_ortogonal(number_matriz,position_matriz_x,position_matriz_y)
            #print()
            #list_simple.show(position_matriz_x,position_matriz_y)
            #matriz_ortogonal.show_ortogonal(position_matriz_x,position_matriz_y)
            #number_position=len(posicion)
            #print(number_position)
    except:
        print('No se puede abrir el archivo')

def procesar_archivo():
    pass

def escribir_archivo_salida():
    pass

def generar_grafica():
    pass

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