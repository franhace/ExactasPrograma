import random

# Funcion que genera un mazo de 52 cartas

def crear_mazo():

    a = 0
    cartas = []
    while a < 4:
        for carta in range(1, 14):
            cartas.append(carta)
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

        return s  # puntaje final


# Funcion que juega con "j" jugadores, con el mazo "m"

def jugar_varios(m, j):

    resultados = []

    i = 0
    while i < j:
        resultados.append(jugar(m))
        i = i + 1
    return resultados


# Funcion que se fija quien gano y devulve 1 en caso positivo

def ver_quien_gano(resultados):
    l1 = []
    for jugador, resultado in enumerate(resultados):
        if resultado == 21:
            s = 1
            l1.append(s)
            print("jugador {} ganó".format(jugador+1))
        else:
            s = 0
            l1.append(s)
            print("jugador {} perdió".format(jugador+1))

    return l1


# Devuelve cantidad de veces que el jugador saco 21 puntos
def puntaje_total_jugador(lista_resultados):
    puntaje = lista_resultados.count(21)
    return puntaje


# Devuelve cantidad de veces que cada jugador saco 21 puntos
def puntaje_por_jugador(res_experimentar):
    lista_puntajes = []
    for i in res_experimentar:
        lista_puntajes.append(puntaje_total_jugador(i))
    return lista_puntajes


# Funcion que toma n jugadores ,  los hace jugar rep veces y devuelve cuantas veces gano/perdio c/u

def experimentar(n, rep):

    lists = [[] for _ in range(n)]
    i = 0
    while i < rep:
        for jugador in range(n):
            mazo = generar_mazos(1)
            x = jugar_varios(mazo, n)


            i += 1
            lists[jugador].extend(x)
            # print("jugador {} {} puntos ".format(i, s))

    return lists


ress = experimentar(2, 10)
print((ress))
print(puntaje_por_jugador(ress))

## Vemos si lista contiene listas,
# ya que estaria bueno ver un puntaje final x jugador
print(any(isinstance(el, list) for el in ress))
