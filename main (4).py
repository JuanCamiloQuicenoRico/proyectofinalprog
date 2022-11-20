# !/usr/bin/env python3
"""En el siguiente modulo se realizara un juego similar a batalla naval"""
#importamos libreria random
import random

""" la siguiente función nos ayudara a mostrar los tabletos del
jugador o usuario y el computador"""
def showBoard( player, user, PC ):
  if user == "":
    user = "PJ"
  print( "=====PC======" )
  #organizamos el rango de los tableros
  for i in range( 0, 9 ):
    for j in range( 0, 9 ):
      if PC[ i ][ j ] == 'B':
        print( 'O', end="" )
      else:
        print( PC[ i ][ j ], end="" )
        #ponemos el salto de linea para que los tableros queden de la forma
        #solicitada
    print( "\n", end="" )
  print( "\n=============\n" )
  print( "=====", user, "======" )
  for i in range( 0, 9 ):
    for j in range( 0, 9 ):
      print( player[ i ][ j ], end="" )
    print( "\n", end="" )
  return 0
"""con esta función nos aseguramos que no se permita ubicar barcos en
columnas y filas donde ya los hay"""
def inGame( player, PC, user, barcosPC, barcosPlayer ):
  print( "   ¡ES TU TURNO!" )
  filaJ = int(input( "Introduzca la fila: " ))
  columJ = int(input( "Introduzca la columna: " ))
  #filaJ = random.randint( 0, 9 )
  #columJ = random.randint( 0, 9 )
  #iniciamos ciclo para que nos muestre si el impacto ha sudo fallado, acertado
  # o invalido
  while( ( filaJ < 0 or columJ > 9 or filaJ > 9 or columJ < 0 ) or ( PC[ filaJ ][ columJ ] != 'O' and PC[ filaJ ][ columJ ] != 'B' ) ):
    print( "Disparo invalidado." )
    filaJ = int(input( "Introduzca la fila: " ))
    columJ = int(input( "Introduzca la columna: " ))
    #filaJ = random.randint( 0, 9 )
    #columJ = random.randint( 0, 9 )
  if PC[ filaJ ][ columJ ] == 'B':
    print( "  Impacto!" )
    PC[ filaJ ][ columJ ] = 'D'
    barcosPC = barcosPC - 1
  else:
    print( "  Disparo fallado" )
    PC[ filaJ ][ columJ ] = 'X'

  if barcosPC > 0:
    filaPC = random.randint( 0, 9 )
    columPC = random.randint( 0, 9 )
    while( player[ filaPC ][ columPC ] != 'O' and player[ filaPC ][ columPC ] != 'B' ):
     filaPC = random.randint( 0, 9 )
     columPC = random.randint( 0, 9 )
    if player[ filaPC ][ columPC ] == 'B':
      print( "  Impacto Enemigo!" )
      player[ filaPC ][ columPC ] = 'D'
      #si el jugador dispara y le da a un barco el número de barcos se resta 
      barcosPlayer = barcosPlayer - 1
    else:
      print( "  Disparo enemigo fallado" )
      player[ filaPC ][ columPC ] = 'X'

    if barcosPlayer == 0:
      print( "  JUEGO TERMINADO" )
      print( "  EL GANADOR ES EL PC" )
      input( "  presione ENTER para continuar: " )
      return 0

  else:
    if user == "":
      user = "PJ"
    print( "  JUEGO TERMINADO" )
    print( "EL GANADOR ES:", user )
    input( "presione ENTER para continuar: " )
    return 0
  showBoard( player, user, PC )
  inGame( player, PC, user, barcosPC, barcosPlayer )
"""La siguiente función nos indica si el tiro del enemigo fue acertado o
incorrecto y también imprime los tableros del PC y del jugador """
def mainMenu():
# Menú principal
        user = ""
        print("-----Los Caracteres Especiales -----")
        print("-----Batalla naval-----")
        print("-----Menú principal-----")
        print("1. Introducir nombre del jugador")
        print("2. Iniciar juego")
        print("3. Cerrar programa")
        # Interacciones del usuario
        print("---------------------------------------------------")
        select = int(input("Introduzca un numero de los mostrados anteriromente: "))
        if select == 1:
            user = input("Introduzca el nombre del jugador: ")
            print("------------------------------------------------------")
            print("", "Hola", user, "")
            mainMenu()

            #Iniciar juego

        elif select == 2:
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
            for i in range( 0, 10 ):
                filaJ = int(input("Indique la fila en la que desea ubicar su barco: "))
                columJ = int(input("Indique la columna en la que desea ubicar su barco: "))
                while( ( filaJ < 0 or columJ > 9 or filaJ > 9 or columJ < 0 ) or ( player[ filaJ ][ columJ ] == 'B' ) ):
                   print( "Error, Seleccione otra ubicación." )
                   filaJ = int(input("Idique la fila en la que desea ubicar su barco: "))
                   columJ = int(input("Indique la columna en la que desea ubicar su barco: "))
                player[ filaJ ][ columJ ] = 'B'
                filaPC = random.randint( 0, 9 )
                columPC = random.randint( 0, 9 )
                while( PC[ filaPC ][ columPC ] == 'B' ):
                   filaPC = random.randint( 0, 9 )
                   columPC = random.randint( 0, 9 )
                PC[ filaPC ][ columPC ] = 'B'
            showBoard( player, user, PC )
            barcosPC = barcosPlayer = 10
            inGame( player, PC, user, barcosPC, barcosPlayer )
            mainMenu()
        #--------------------------------------------------------------------
        if select == 3:
                print("----- Fin del programa -----")

        elif select < 1 or select > 3:
                print("----- ERROR: Seleccion invalida -----")

mainMenu()

