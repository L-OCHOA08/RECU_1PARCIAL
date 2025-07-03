def buscar_caballo(caballos):
    caballo = input("Ingrese el nombre del caballo").capitalize()
    i = 0
    encontrado = False
    while not encontrado and i < len(caballos):
        if caballo == i:
            print("Encontrado")
            encontrado = True
        else:
            i += 1
    return caballo

def buscar_carrera(carreras):
    carrera = input("Ingrese el nombre de la carrera").lower()
    i = 0
    encontrado = False
    while not encontrado and i < len(carreras):
        if carrera == carreras[i]:
            print("Encontrada")
            encontrado = True
        else:
            i += 1
    return carrera

def registrar_resultado_un_caballo(carreras, caballos, resultados):
    registro = []

    # SE PIDE EL NOMBRE DE LA CARRERA
    carrera = buscar_carrera(carreras)
    registro = registro + [carrera]

    # SE PIDE EL NOMBRE DEL CABALLO
    caballo = buscar_caballo(caballos)
    registro = registro + [caballo]

    tiempo_llegada = int(input("Ingrese cuantos segundos tardó en llegar(30-300): "))
    while tiempo_llegada < 30 or tiempo_llegada > 300:
        print("Tiempo fuera de rango. El rango está entre 30 y 300.")
        tiempo_llegada = int(input("Ingrese cuantos segundos tardó en llegar(30-300): "))
        tiempo_llegada = str(tiempo_llegada)
    registro = registro + [tiempo_llegada]

    resultados += [registro]
    return resultados

def mostrar_todos_resultados_registrados(carreras, resultados):
    for i in carreras:
        print(f"Carrera {i}:")
        for j in resultados:
            if i == j[0]:
                print(j[1:])

def calcular_rendimiento_promedio(caballos, resultados):
    for i in caballos:
        contador = 0
        tiempo = 0
        for j in resultados:
            if i == j[1]:
                contador += 1
                tiempo += j[2]
        if contador > 0:
            promedio = tiempo / contador
            print(f"Promedio de {i}: {promedio}")
        else:
            print(f"Promedio de {i}: Sin datos")


def mostrar_caballo_mas_ganador(caballos_ganadores, caballos):
    for i in caballos:
        contador = 0
        for j in caballos_ganadores:
            if i == j:
                contador += 1
                if contador >= len(caballos_ganadores) / 2:
                    caballo_ganador = j
    print(f"El caballo con mejores puestos es {caballo_ganador}")
    print("---------------------------------------------")

def determinar_caballo_mas_ganador(carreras, resultados):
    caballos_ganadores = []
    for i in carreras:
        caballo_ganador = None
        mejor_tiempo = float('inf')
        for j in resultados:
            # resultados = [carrera, caballo, tiempo]
            if j[2] < mejor_tiempo and i == j[0]:
                mejor_tiempo = j[2]
                caballo_ganador = j[1]
                caballos_ganadores = caballos_ganadores + [caballo_ganador]

        if mejor_tiempo >= 30 and mejor_tiempo <= 300:
            print("---------------------------------------------")
            print(f"{i}: el caballo {caballo_ganador} tiene el primer puesto con {mejor_tiempo}")
            print("---------------------------------------------")
        else:
            print("---------------------------------------------")
            print(f"No hay una carrera registrada en la competencia")
            print("---------------------------------------------")
    return caballos_ganadores


def ordenamiento_burbuja(lista):
    n = len(lista)
    i = 0
    intercambiado = True
    while i < n and intercambiado:
        intercambiado = False
        for j in range(0, n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        i += 1
    return lista

def mostrar_nombres_caballos_ordenados(caballos):
    caballos = ordenamiento_burbuja(caballos)
    print("----- NOMBRE DE CABALLOS -----")
    for i in caballos:
        print(i)


def mostrar_mejor_puesto_por_caballo(caballos, resultados):
    caballo_a_buscar = input("Caballo que desea ver su mejor puesto alcanzado: ")
    i = 0
    encontrado = False
    while not encontrado and i < len(caballos):
            if caballo_a_buscar == caballos[i]:
                record = float('inf')
                for j in resultados:
                    if caballos[i] == j[1]:
                        if j[2] < record:
                            record = j[2]
                print(f"El mejor tiempo de {caballos[i]} fue de: {record}")
                encontrado = True
            else:
                i += 1

def calcular_tiempo_promedio_por_carrera(carreras, resultados):
    for i in carreras:
        contador = 0
        tiempo = 0
        for j in resultados:
            if i == j[0]:
                contador += 1
                tiempo += j[2]
        if contador > 0:
            promedio = tiempo / contador
            print(f"Promedio de {i}: {promedio}")
        else:
            print(f"Promedio de {i}: Sin datos")