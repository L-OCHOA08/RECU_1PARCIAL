from funciones import *

def menu():

    # VARIABLES
    CARRERAS = ["gran premio ciudad", "copa del sur", "desafio de la plata", "clasico del litoral", "copa patagonica"]
    CABALLOS = ["Tormenta", "Relámpago", "Flecha", "Centella", "Huracán", "Trueno", "Amanecer", "Galán", "Pampero", "Titán", "Bestia", "Veloz"]
    resultados = []

    salir = False
    while not salir:
        print("----- Sistema de rendimiento en Carreras de Caballos -----")
        print("1. Registrar resultado de un caballo en una carrera")
        print("2. Mostrar todos los resultados registrados")
        print("3. Calcular el rendimiento promedio de cada caballo")
        print("4. Determinar el caballo más ganador")
        print("5. Ordenar y mostrar los nombres de los caballos")
        print("6. Ver mejor puesto alcanzado por cada caballo")
        print("7. Calcular el tiempo promedio de cada carrera")
        print("8. Salir del programa")

        opcion = int(input("ingrese un numero del 1 al 8: "))
        if opcion < 1 or opcion > 8: 
            numero_valido = False 
            while not numero_valido:
                print("ingrese un numero valido")
                opcion = int(input("ingrese un numero del 1 al 8: "))
                if opcion >= 1 and opcion <= 8:
                    numero_valido = True 

        match opcion:
            case 1:
                resultados = registrar_resultado_un_caballo(CARRERAS, CABALLOS, resultados)
                print(resultados)
            case 2:
                mostrar_todos_resultados_registrados(CARRERAS, resultados)
            case 3:
                calcular_rendimiento_promedio(CABALLOS, resultados)
            case 4:
                determinar_caballo_mas_ganador()
            case 5:
                mostrar_nombres_caballos_ordenados(CABALLOS)
            case 6:
                mostrar_mejor_puesto_por_caballo(CABALLOS, resultados)
            case 7:
                calcular_tiempo_promedio_por_carrera(CARRERAS, resultados)
            case 8:
                print("Saliendo del programa...")
                salir = True

menu()