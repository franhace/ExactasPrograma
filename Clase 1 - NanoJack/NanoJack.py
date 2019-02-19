import random

n = 2


# Funcion que genera un mazo de 52 cartas

def crear_mazo():

    a = 0
    cartas = []
    while a < 4:
        for c in range(1, 14):
            cartas.append(c)
        a = a + 1
    return cartas


# Funcion que mezcla la cantidad "n" de mazos con la cual se quiera jugar

def generar_mazos(n):

    a = 0
    mazo = crear_mazo()
    c = 0
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

        while s < 21:
            r = m.pop(c)  # saca carta seleccionada
            s = s + r  # suma carta seleccionada al puntaje total
            cartas_sacadas.append(r)

        # print(cartas_sacadas)
        # print(s)
        return s  # puntaje final


# s = jugar(m)
# print(s)
# print(m)
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
print(resultados)


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
print(ver_quien_gano(resultados))


# Funcion que juega "rep" veces con "n" jugadores y devuelve cuantas veces gano cada uno

rep = 5# num de veces que juega cada jugador
n = 17 # num de jugadores

def experimentar(rep, n):
    l = 0
    b = 0
    l2 = [] # resultados
    l3 = [] # 0 o 1
    while b < rep:

        l3.append(jugar_varios(m, n))
        b = b + 1

        while l < n:
            l = l + 1
            l2.append(ver_quien_gano(l3))

        print(l2)

        return l3


print(experimentar(rep, n))



# falta un return que devuelva el resultado 0 o 1

