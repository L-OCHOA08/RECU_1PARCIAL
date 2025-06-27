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
                            print("Se le sumó puntaje correctamente.")
                            encontrado = True
                        else:
                            i += 1
        case "-":
            cantidad_restar = int(input("Cantidad que desea restar: "))
            while cantidad_restar < 0:
                print("Cantidad Inválida.")
                cantidad_restar = int(input("Cantidad que desea restar: "))
            encontrado = False
            i = 0
            while not encontrado and i < len(lista_jugadores):
                    if numero_jugador == i:
                        if puntajes[i-1] - cantidad_restar <= 0:
                            print("Error al restar. No puede quedar en 0 o menos.")
                            encontrado = True
                        else:
                            puntajes[i-1] -= cantidad_restar
                            print("Se le restó puntaje correctamente.")
                            encontrado = True
                    else:
                        i += 1
    return lista_jugadores, puntajes

def buscar_jugador_mas_forma(puntajes):
    mayor_puntaje = float('-inf')
    for i in range(len(puntajes)):
        if puntajes[i] > mayor_puntaje:
            mayor_puntaje = puntajes[i]
            jugador_mayor_puntaje = i+1
            if mayor_puntaje > 0:
                print(f"El jugador {jugador_mayor_puntaje} tiene el puntaje mas alto: {mayor_puntaje}")
            else:
                print("Nadie ha sido evaluado.")

def mostrar_todos_los_jugadores(lista_jugadores, puntajes):
    for puntaje in range(len(puntajes)):
        if puntajes[puntaje] > 0:
            print(f"Jugador {lista_jugadores[puntaje]}: {puntajes[puntaje]}")
        else:
            print(f"Jugador {lista_jugadores[puntaje]}: sin evaluar.")