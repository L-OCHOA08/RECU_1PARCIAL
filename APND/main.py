from funciones import *

def menu():

    lista_jugadores = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    puntajes = [0] * 22

    salir = False
    while not salir:
        print("menu de gestion")
        print("1.Asignar puntaje de rendimiento a un jugador")
        print("2.Consultar puntaje de un jugador")
        print("3.Modificar puntaje de un jugador (mejora o bajón)")
        print("4.Buscar al jugador más en forma")
        print("5.Mostrar todos los jugadores con sus puntajes")
        print("6.Salir del programa")

        opcion = int(input("ingrese un numero del 1 al 6: "))
        if opcion < 1 or opcion > 6: 
            numero_valido = False 
            while not numero_valido:
                print("ingrese un numero valido")
                opcion = int(input("ingrese un numero del 1 al 6: "))
                if opcion >= 1 and opcion <= 6:
                    numero_valido = True 

        match opcion:
            case 1:
                lista_jugadores, puntajes = asignar_puntaje(lista_jugadores, puntajes)
                print(puntajes)
            case 2:
                consultar_puntaje(lista_jugadores, puntajes)
            case 3:
                modificar_puntaje()
            case 4:
                buscar_jugador_mas_forma()
            case 5:
                mostrar_todos_los_jugadores()
            case 6:
                print("Saliendo del programa")
                salir = True

menu()