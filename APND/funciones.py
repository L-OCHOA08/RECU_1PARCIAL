def ingresar_jugador():
    numero_jugador = int(input("Ingrese el numero del jugador: "))
    while numero_jugador < 1 or numero_jugador > 22:
        print("Numero de jugador inválido. Ingrese un numero entre el 1 y el 22")
        numero_jugador = int(input("Ingrese el numero del jugador: "))
    return numero_jugador

def asignar_puntaje(lista_jugadores, puntajes):
    numero_jugador = ingresar_jugador()
    encontrado = False
    i = 0
    while not encontrado and i < len(lista_jugadores):
        if numero_jugador == i:
            puntaje_a_agregar = int(input("Cantidad de puntaje que desea asignarle: "))
            while puntaje_a_agregar <= 0:
                print("Ingrese una cantidad de puntaje válido")
                puntaje_a_agregar = int(input("Cantidad de puntaje que desea asignarle: "))
            puntajes[i-1] = puntaje_a_agregar
            encontrado = True
        else:
            i += 1
    return lista_jugadores, puntajes

def consultar_puntaje(lista_jugadores, puntajes):
    numero_jugador = ingresar_jugador()
    encontrado = False
    i = 0
    while not encontrado and i < len(lista_jugadores):
        if numero_jugador == i:
            print(f"El puntuaje del jugador {numero_jugador} es de {puntajes[i-1]}")
            encontrado = True
        else:
            i += 1

def modificar_puntaje(lista_jugadores, puntajes):
    numero_jugador = ingresar_jugador()
    operacion = input("Ingrese la operacion que desee hacer(+/-): ")
    match operacion:
        case "+":
            cantidad_sumar = int(input("Cantidad que desea sumar: "))
            while cantidad_sumar < 0:
                print("Cantidad Inválida.")
                cantidad_sumar = int(input("Cantidad que desea sumar: "))
                encontrado = False
                i = 0
                while not encontrado and i < len(lista_jugadores):
                        if numero_jugador == i:
                            puntajes[i] += cantidad_sumar
                            encontrado = True
                        else:
                            i += 1
        case "-":
            cantidad_restar = int(input("Cantidad que desea sumar: "))
            while cantidad_restar < 0:
                print("Cantidad Inválida.")
                cantidad_restar = int(input("Cantidad que desea sumar: "))
                encontrado = False
                i = 0
                while not encontrado and i < len(lista_jugadores):
                        if numero_jugador == i:
                            puntajes[i] -= cantidad_restar
                            encontrado = True
                        else:
                            i += 1
                