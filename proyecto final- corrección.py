# !/usr/bin/env python3
"""En el siguiente modulo se realizara un juego similar a batalla naval"""
#importamos libreria random
import random

""" la siguiente función nos ayudara a mostrar los tabletos del
jugador o usuario y el computador"""
def showBoard(player, user, PC):
    #si el usuario no ingresa su nombre
    if user == "":
        #Le da el nombre de PJ
        user = "PJ"
    #imprime PC
    print("=====PC======")
    #Ciclo para ubicar los barcos en el tablero del PC ya que el jugador no puede ver la ubicacion de estos
    for i in range(0, 9):
        for j in range(0, 9):
            # Si i y j son iguales aun barco imprime el simbolo que representa el agua
            if PC[i][j] == 'B':
                print('O', end="")
            # Si no solo imprime un salto de linea
            else:
                print(PC[i][j], end="")
        #Al final del ciclo imprime un salto de linea
        print("\n", end="")
    # imprime una linea divisoria
    print("\n=============\n")
    # Imprime el nombre de usuario si se ingreso sino imprime PJ
    print("=====", user, "======")
    # Ciclo para imprimir el tablero del jugador
    for i in range(0, 9):
        for j in range(0, 9):
            #imprime las posiciones de los barcos
            print(player[i][j], end="")
        #Imprime un salto de linea
        print("\n", end="")
    return 0

"""con esta función nos aseguramos que no se permita ubicar barcos en
columnas y filas donde ya los hay"""
def inGame(player, PC, user, barcosPC, barcosPlayer):
    #imprime el turno del jugador
    print("   ¡ES TU TURNO!")
    # Pide al usuario que ingrese la fila
    filaJ = int(input("Introduzca la fila: "))
    #la columna en donde desea atacar al enemigo
    columJ = int(input("Introduzca la columna: "))
    # Mientras las filas y las columnas se encuentren entre 0 y 9 o mientras los elementos del PC sea dif a agua y los elementos del PC sean diferentes a Barcos
    while ((filaJ < 0 or columJ > 9 or filaJ > 9 or columJ < 0) or (
            PC[filaJ][columJ] != 'O' and PC[filaJ][columJ] != 'B')):
        #Imprimir disparo invalido
        print("Disparo invalidado.")
        #Vuelve a preguntar las filas para atacar
        filaJ = int(input("Introduzca la fila: "))
        # Vuelve a preguntar columnas para atacar
        columJ = int(input("Introduzca la columna: "))

    # Si La ubicacion seleccionada por el usuario se encuantra un barco
    if PC[filaJ][columJ] == 'B':
        #imprime impacto
        print("  Impacto!")
        #se cambia el valor en la ubicacion de agua a barco undido
        PC[filaJ][columJ] = 'D'
        # se resta un barco al PC
        barcosPC = barcosPC - 1
    # sino
    else:
        #imprime disparo fallido
        print("  Disparo fallado")
        # Cambia el valor de agua a disparo fallido en las coordenadas ingresados por el usuario
        PC[filaJ][columJ] = 'X'

    # Si los barcos del PC son mayores a cero
    if barcosPC > 0:
        #Entonces el PC elige aleatoriamente en donde atarcar al PJ
        filaPC = random.randint(0, 9)
        columPC = random.randint(0, 9)
        #MIentras la ubicaion que ingresa el PC es diferente a agua y la ubicacion ingresada es dif a un barco
        while (player[filaPC][columPC] != 'O' and player[filaPC][columPC] != 'B'):
            filaPC = random.randint(0, 9)
            columPC = random.randint(0, 9)
        #Si la ubicacion es igual a barco
        if player[filaPC][columPC] == 'B':
            #Imprime impacto enemigo
            print("  Impacto Enemigo!")
            # Cambia el valor en la ubicacion por barco undido
            player[filaPC][columPC] = 'D'
            # Se le resta un barco al jugador
            barcosPlayer = barcosPlayer - 1

        #sino
        else:
            #imprime disparo fallado
            print("  Disparo enemigo fallado")
            #cambia el valor en la ubicacion por disparo fallado
            player[filaPC][columPC] = 'X'

        #Si los barcos de del jugador son iguales a cero
        if barcosPlayer == 0:
            #imprime juego terminado
            print("  JUEGO TERMINADO")
            #imprime que el ganador es el PC
            print("  EL GANADOR ES EL PC")
            #Pide presionar enter para continuar con el juego
            input("  presione ENTER para continuar: ")
            return 0

    # sino
    else:
        #si el usuario no ingresa su nombre
        if user == "":
            #Le da el valor de PJ
            user = "PJ"
        #Imprime juego terminado
        print("  JUEGO TERMINADO")
        #imprime el ganador el elo usuario
        print("EL GANADOR ES:", user)
        #pide al usuario que de enter para continuar
        input("presione ENTER para continuar: ")
        return 0
    # Llama la funcion
    showBoard(player, user, PC)
    inGame(player, PC, user, barcosPC, barcosPlayer)

"""La siguiente función nos indica si el tiro del enemigo fue acertado o
incorrecto y también imprime los tableros del PC y del jugador """
def mainMenu():
    # Menú principal
    #la variable user vale
    user = ""
    #Imprimir
    print("-----Los Caracteres Especiales-----")
    print("-----Batalla naval-----")
    print("-----Menú principal-----")
    print("1. Introducir nombre del jugador")
    print("2. Iniciar juego")
    print("3. Cerrar programa")
    # Interacciones del usuario
    print("---------------------------------------------------")
    select = int(input("Introduzca un numero de los mostrados anteriromente: "))
    #si selecciona uno
    if select == 1:
        #pide introducir el nombre al jugador
        user = input("Introduzca el nombre del jugador: ")
        print("------------------------------------------------------")
        #imprime hola y nombre del jugador
        print("", "Hola", user, "")
        #se vuelve a llamar a la funcion para que vuelva a imprimir el menu principal
        mainMenu()

    # si selecciona 2 inicia el juego
    elif select == 2:
        # Se crea una variable que contenga la matriz de 10x10 que indican el los tableros de juego del PC y el PJ
        player = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

        # -------------------------------------------

        PC = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

        # ciclo de 0 a 10 para repetir 10 veces un ciclo
        for i in range(0, 10):
            #Pide al usuario la ubicar sus 10 barcos
            #Selecciona una fila
            filaJ = int(input("Indique la fila en la que desea ubicar su barco: "))
            #selecciona una columna
            columJ = int(input("Indique la columna en la que desea ubicar su barco: "))

            # Mientras las filas y las columnas se encuentren entre 0 y 9 o mientras los elementos de la ubicacion ingresada PJ sean igual a Barcos
            while ((filaJ < 0 or columJ > 9 or filaJ > 9 or columJ < 0) or (player[filaJ][columJ] == 'B')):
                # imprime seleccione otra ubicacion
                print("Error, Seleccione otra ubicación.")
                # vuelve a preguntar la ubicacion en la que el jugador desea ubicar su barco
                filaJ = int(input("Idique la fila en la que desea ubicar su barco: "))
                columJ = int(input("Indique la columna en la que desea ubicar su barco: "))
            # se creaa una variable que contenga las ubicaciones de los barcos
            player[filaJ][columJ] = 'B'
            # El PC elije aleatoriamente donde colocar sus barcos
            filaPC = random.randint(0, 9)
            columPC = random.randint(0, 9)

            #mientras  las ubicaciones del PC contengan barcos
            while (PC[filaPC][columPC] == 'B'):
                filaPC = random.randint(0, 9)
                columPC = random.randint(0, 9)
            PC[filaPC][columPC] = 'B'

        #Llama a la funcion showboard para que despues de que se ambos jugadores ubique sus barcos para que muestre los tableros
        showBoard(player, user, PC)
        #dos funciones que indican la cantidad de barcos que tiene cada jugador
        barcosPC = barcosPlayer = 10
        #Llama a la funcion que inicia el juego
        inGame(player, PC, user, barcosPC, barcosPlayer)
        #vuelve a llamar al menu principal para que lo vuelva a mostrar
        mainMenu()
    # --------------------------------------------------------------------
    # Si el usuario selecciona 3 se acaba el progama
    if select == 3:
        #imprime fin del programa
        print("----- Fin del programa -----")

    #si el usuario ingresa un numero ingresa un numero dif a 1 o a 3
    elif select < 1 or select > 3:
        #imprime seleccion invalida
        print("----- ERROR: Seleccion invalida -----")


mainMenu()


