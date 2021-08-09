from xml.dom import minidom
from lista_simple import*

list_simple=Lista_simple()

def cargar_archivo():
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
            # Inserta y muestra los nombres de los terrenos 
            # en una lista simple
            print('\nLista simple: ')
            list_simple.insert(name)
            list_simple.show()
            print()
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
                    print('x: ',subSubHijo.firstChild.data, end=', ')
                for subSubHijo in y:
                    print('y: ',subSubHijo.firstChild.data)
            for subHijo in posicionfin:
                x=subHijo.getElementsByTagName('x')
                y=subHijo.getElementsByTagName('y')
                print('Posicion final: ')
                for subSubHijo in x:
                    print('x: ',subSubHijo.firstChild.data, end=', ')
                for subSubHijo in y:
                    print('y: ',subSubHijo.firstChild.data)
                print()
            for subHijo in posicion:
                print('x: ',subHijo.getAttribute('x'),', y: ',subHijo.getAttribute('y'),end=' = ')
                print(subHijo.firstChild.data)
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