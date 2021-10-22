from random import *
from preguntas import algebra, geometria, estadistca
import matplotlib.pyplot as plt
# Importo librerías y el banco de preguntas 

global areas
global puntos
global pregIncorrecta
# Declaro variables que usaré más adelante para guardar los puntos

areas = {'Álgebra':0, 'Geometría':0, 'Estadística':0}
pregIncorrecta = []
# Declaro un diccionario donde guardaré el puntaje más nuevo de cada área 

def menu(): # Función menú, donde el usuario podrá escoger el área de estudio o la consulta de calificaciones

    print("Práctica Examen Pisa\n")
    print("1. Practicar Álgebra")
    print("2. Practicar Geometría")
    print("3. Practicar Estadística")
    print("4. Ver resultados")
    print("5. Salir\n")

    opcion = input('Ingrese una opción: ')

    if opcion == '1':
        examenPrincipal(algebra)
    
    elif opcion == '2':
        examenPrincipal(geometria)

    elif opcion == '3':
        examenPrincipal(estadistca)

    elif opcion == '4':
        graficar()

    elif opcion == '5':
        # A parte de cerrar el programa, lo que se hace es guardar en un archivo de texto, 
        # las calificaciones actuales.

        areasLlaves = areas.keys()
        areasValores = [str(areas[i]) for i in areasLlaves]
        f = open('register.txt', 'w')
        f.write(' '.join(areasValores))
        f.close()

        #Crear el archivo de texto con las preguntas incorrectas

        f = open('Preguntas Incorrectas.txt', mode = 'w', encoding = 'utf-8')
        f.write('\n\n'.join(pregIncorrecta))

    else:
        print('Opción inválida')
        menu()

    

def examenPrincipal(area): 
    # En esta función, lo que se hace es que se le da un parámetro, que es el banco de preguntas correspondiente,
    # y el programa mezcla de manera aleatoria preguntas y respuestas y actualiza la calificación en el diccionario

    # Reseteo la calificación de la cual se está haciendo el examen
    if area == estadistca:
        areas['Estadística'] = 0

    elif area == algebra:
        areas['Álgebra'] = 0

    else:
        areas['Geometría'] = 0

    puntos = []
    selecPregun = sample(area, 4) # Obtengo cuatro preguntas random del banco

    for i in range(4): # Itero para 
        respsRan = sample(selecPregun[i][1:],4) # Hago random el orden de las respuestas 

        print(f'{i+1}) {selecPregun[i][0]}\n') # Muestro la pregunta y la numero
        
        for j in range(4): # En este ciclo, muestro las preguntas con las letras correspondientes
            alph = 'abcd'
            print(f'{alph[j]}) {respsRan[j]}')

        

        while True: # Simulación de un Do-While para pedir una respuesta válida

            resp = input('Su respuesta es: ').lower() # Obtención de la respuesta del usuario
            
            try: # Añadí un try porque si intentaba buscar una respuesta que no estuviera en abcd regresaba error

                if resp == '': # Correción de un error en el que si el usuario pulsaba enter, tomaba la respuesta 1
                    pass
                
                
                elif respsRan[alph.index(resp)] == selecPregun[i][1]: # Hago revisión de la respuesta
                    puntos.append(f'Pregunta {i+1}: Correcta')
                    
                    # Si está correcta, añado un punto dependiendo del área
                    if area == estadistca:
                        areas['Estadística'] = areas['Estadística'] + 1

                    elif area == algebra:
                        areas['Álgebra'] = areas['Álgebra'] + 1

                    else:
                        areas['Geometría'] = areas['Geometría'] + 1

                    # Si no, no añado nada a los puntos y añado una sentencia para informar al usuario que está mal
                else:
                    puntos.append(f'Pregunta {i+1}: Incorrecta')
                    pregIncorrecta.append(selecPregun[i][0])

            except:
                pass

            if resp in 'abcd' and resp != '': # Aquí simulo la condición del Do-While
                print()
                break
            else:
                print('Respuesta no válida')

    print('\n'.join(puntos)) # Le muestro al usuario cuáles respuestas tuvo bien y cuáles mal
    print()

    menu()

def graficar():

    # Esta función se encarga tanto de graficar los datos almacenados en el archivo de texto, como los actuales.
    try:
        f = open('register.txt', 'r')
        valoresAnteriores = f.read().split(' ') # Obtención de los datos apartir del archivo de texto
        valoresAnteriores = [int(i) for i in valoresAnteriores]
        f.close()

    except:
        valoresAnteriores = [0, 0, 0]

    print(areas)
    areasLlaves = areas.keys()
    areasValores = [areas[i] for i in areasLlaves] # Obtención de datos actuales

    fig, (ax1, ax2) = plt.subplots(1, 2) # Formato y representación de la gráficas
    fig.suptitle('Calificación por fecha')
    fig.set_size_inches(13, 5)
    ax1.bar(areasLlaves,valoresAnteriores)
    ax2.bar(areasLlaves,areasValores)
    ax1.set(xlabel = 'Área', ylabel = 'Puntaje (de 4)', ylim = [0, 4], title = 'Intento Anterior')
    ax2.set(xlabel = 'Área', ylabel = 'Puntaje (de 4)', ylim = [0, 4], title = 'Intento Actual')
    fig.show()

    menu()

menu() # Correr el programa