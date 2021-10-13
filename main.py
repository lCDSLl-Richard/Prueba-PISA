from random import *
from preguntas import algebra, geometria, estadistca
import matplotlib.pyplot as plt

global areas
global puntos


areas = {'Álgebra':0, 'Geometría':0, 'Estadística':0}

def menu():

    print("Práctica Examen Pisa")
    print("1. Practicar Álgebra")
    print("2. Practicar Geometría")
    print("3. Practicar Estadística")
    print("4. Ver resultados")
    print("5. Salir")

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

        areasLlaves = areas.keys()
        areasValores = [str(areas[i]) for i in areasLlaves]
        f = open('register.txt', 'w')
        f.write(' '.join(areasValores))
        f.close()

    else:
        print('Opción inválida')
        menu()

    

def examenPrincipal(area):

    if area == estadistca:
        areas['Estadística'] = 0

    elif area == algebra:
        areas['Álgebra'] = 0

    else:
        areas['Geometría'] = 0

    puntos = []
    selecPregun = sample(area, 4)

    for i in range(4):
        respsRan = sample(selecPregun[i][1:],4)

        print(f'{i+1}) {selecPregun[i][0]}')
        
        for j in range(4):
            alph = 'abcd'
            print(f'{alph[j]}) {respsRan[j]}')

        

        while True:

            resp = input('Su respuesta es: ').lower()
            
            try:

                if resp == '':
                    pass
                
                
                elif respsRan[alph.index(resp)] == selecPregun[i][1]:
                    puntos.append(f'Pregunta {i+1}: Correcta')
                    
                    if area == estadistca:
                        areas['Estadística'] = areas['Estadística'] + 1

                    elif area == algebra:
                        areas['Álgebra'] = areas['Álgebra'] + 1

                    else:
                        areas['Geometría'] = areas['Geometría'] + 1


                else:
                    puntos.append(f'Pregunta {i+1}: Incorrecta')

            except:
                pass

            if resp in 'abcd' and resp != '':
                print()
                break
            else:
                print('Respuesta no válida')

    print('\n'.join(puntos))

    menu()

def graficar():
    
    f = open('register.txt', 'r')

    print(areas)

    valoresAnteriores = f.read().split(' ')
    valoresAnteriores = [int(i) for i in valoresAnteriores]

    f.close()

    areasLlaves = areas.keys()
    areasValores = [areas[i] for i in areasLlaves]

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Calificación por fecha')
    fig.set_size_inches(13, 5)
    ax1.bar(areasLlaves,valoresAnteriores)
    ax2.bar(areasLlaves,areasValores)
    ax1.set(xlabel = 'Área', ylabel = 'Puntaje (de 4)')
    ax2.set(xlabel = 'Área', ylabel = 'Puntaje (de 4)')
    ax1.set_title('Intento Anterior')
    ax2.set_title('Intento Actual')
    fig.show()

    menu()

menu()