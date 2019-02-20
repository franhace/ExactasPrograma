import random

n = 2


# Funcion que genera un mazo de 52 cartas

def crear_mazo():

    a = 0
    cartas = []
    while a < 4:
        for car in range(1, 14):
            cartas.append(car)
        a = a + 1
    return cartas


# Funcion que mezcla la cantidad "n" de mazos con la cual se quiera jugar

def generar_mazos(n):

    a = 0
    mazo = crear_mazo()

    mazo_mezclado = []

    while a < n:
        for c in mazo:
            mazo_mezclado.append(c)
        a = a + 1

    random.shuffle(mazo_mezclado)
    return mazo_mezclado

# Mazo
m = generar_mazos(n)


# Funcion que toma cartas del mazo(m) hasta que el valor sea superior o igual a 21

def jugar(m):

    # Mano sacó el jugador
    cartas_sacadas = []

    for c in m:

        s = 0  # Puntaje del jugador
        # if len(m) <= 0: # QUE PASA SI NOS QUEDAMOS SIN CARTAS
        #     print(0)
        #     break

        while s < 21:
            r = m.pop(c)  # saca carta seleccionada
            s = s + r  # suma carta seleccionada al puntaje total
            cartas_sacadas.append(r)


        # print(cartas_sacadas)
        # print(s)
        return s  # puntaje final


# s = jugar(m)
# print(s)
print("numero de cartas: {}".format(len(m)))
# print(len(m))


# Numero de jugadores

j = 3


# Funcion que juega con "j" jugadores, con el mazo "m"

def jugar_varios(m, j):

    resultados = []

    i = 0
    while i < j:
        resultados.append(jugar(m))
        i = i + 1
    return resultados


resultados = jugar_varios(m, j)
print("resultados: {}".format(resultados))


# Funcion que se fija quien gano y devulve 1 en caso positivo

def ver_quien_gano(resultados):

    l1 = []

    for c in resultados:
        #print(c) # muestra el resultado

        if c == 21:
            s = 1
            l1.append(s)
        else:
            s = 0
            l1.append(s)
    return l1


y = ver_quien_gano(resultados)
# print(ver_quien_gano(resultados))

#
# # Funcion que juega "rep" veces con "n" jugadores y devuelve cuantas veces gano cada uno

rep = 2  # num de veces que juega cada jugador
n = 5  # num de jugadores

r = jugar_varios(m, rep)
y2 = ver_quien_gano(r)
print("r: {}".format(r))

# Funcion que toma n jugadores ,  los hace jugar rep veces y devuelve cuantas veces gano/perdio c/u

def experimentar(n, rep):

    l1 = []
    l2 = []
    i = 0
    s = []
    # while i < rep:
    #     l1.append(y2)
    #     i += 1
    #     while s < n:
    #         l2.append(r)
    #         s += 1
    count = 0
    for c in range(n):
        l1.append(r)

        while i < rep :
            l2.append(r)

            i += 1
            print("jugador {} {} puntos ".format(i, s))


    print("l1: {}".format(l1))
    print("l2: {}".format(l2))
    return l2


# print(r)
print(experimentar(n, rep))
print("numero de cartas: {}".format(len(m)))

#
# # falta un return que devuelva el resultado 0 o 1

