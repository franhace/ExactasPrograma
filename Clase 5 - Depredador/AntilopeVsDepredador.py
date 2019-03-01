import numpy as np
import random
import csv

# Funcion que genera un tablero de "filas" filas y "columnas" columnas
# Luego le agrega montanas en los bordes


def generar_tablero(filas, columnas):

    # Creamos tablero
    x = filas
    y = columnas
    numero_de_casilleros_activos_en_x = x + 2
    numero_de_casilleros_activos_en_y = y + 2

    tablero = np . repeat("-", numero_de_casilleros_activos_en_x*numero_de_casilleros_activos_en_y) . \
        reshape(numero_de_casilleros_activos_en_x, numero_de_casilleros_activos_en_y) # completa el array con valor entre ""

    n_fila = tablero.shape[0]
    n_col = tablero.shape[1]

    # Crear montanas
    tablero[0, :] = 'M'
    tablero[:, 0] = 'M'
    tablero[:, -1] = 'M'
    tablero[- 1, :] = 'M'

    return tablero

tablero = generar_tablero(filas=4, columnas=6)

# # podemos acceder a un elemento individual por su fila y columna :
# print ( " La posicion (1,1) tiene el elemento : ", t[(1, 2)])
# # podemos verlo con :
# print ("la posicion (1,7) tiene el elemento :", t[(1, 2)])
# # como el tablero tiene dos dimensiones , podemos accederlas como :
# print (" Mi tablero tiene ", t . shape[0], "filas y", t . shape [1] , "columnas" )

# Hace que los bordes del tablero sean montanas "M" o numeros

n_fila = tablero.shape[0]
n_col = tablero.shape[1]

# Definimos la coordenadas de nuestros personajes
# Hacer funcion que ubique "n" numero de personajes de cada tipo, por "coord"

# x = [2, 3, 4, 4, 2]
# y = [2, 3, 3, 5, 5]
# tipo = ["A", "A", "A", "L", "L"]
# # Los asignamos dentro del tablero
# for i in range(len(tipo)):
#     tablero[(x[i], y[i])] = tipo[i]

# Funcion que toma como entrada un posicion "coord_centro" y devuelve
# una lista con las 8 coordenadas adyacentes, en sentido horario, empezando
# por el casillero superior izquierdo


def mis_vecinos(coord_centro):

    c = coord_centro[1]
    f = coord_centro[0]
    coord_vecinas = [(f-1, c-1), (f-1, c), (f-1, c+1),
                     (f, c+1),(f+1, c+1), (f+1, c),
                     (f+1, c-1), (f, c-1)]
    return coord_vecinas

# print(mis_vecinos(coord_centro=(3, 3)))

# Funcion que toma 3 parametros, "tablero" , centro de busqueda "coord_centro" y "objetivo"
# que busca un tipo de valor del casillero
# si no existiera dicho objetivo buscado, devuelve una lista vacia

def buscar_adyacente(tablero, coord_centro, objetivo):

    adyacente = []
    l = mis_vecinos(coord_centro)
    for i in l:
        if tablero[i] == objetivo:
            adyacente.append(i)
            return adyacente
    return []


# print(buscar_adyacente(tablero, coord_centro=(1, 2), objetivo="-"))


def recorrer_tablero(tablero):
    n_fila = tablero.shape[0]
    n_col = tablero.shape[1]
    centros = []
    for i in range(1, n_fila -1):
        for j in range(1, n_col - 1):
            coord_centro = (i, j)
            centros.append(coord_centro)
    return centros

print(recorrer_tablero(tablero))


def fase_mover(tablero):
    objetivo = "-"
    for coord_centro in recorrer_tablero(tablero):
        if tablero[coord_centro] == "L" or tablero[coord_centro] == "A":
            letra = tablero[coord_centro]
            w = buscar_adyacente(tablero, coord_centro, objetivo)
            if len(w) != 0:
                tablero[w[0]] = letra
                tablero[coord_centro] = '-'
    return tablero


# print("\n Movimiento \n \n{}".format(fase_mover(tablero)))


def fase_alimentacion(tablero):
    objetivo = "A"
    for coord_centro in recorrer_tablero(tablero):
        if tablero[coord_centro] == "L":
            letra = tablero[coord_centro]
            w = buscar_adyacente(tablero, coord_centro, objetivo)
            if len(w) != 0:
                tablero[w[0]] = letra
                tablero[coord_centro] = '-'
    return tablero


# print("\n Alimentacion \n \n {}".format(fase_alimentacion(tablero)))


def fase_reproduccion(tablero):

    for coord_centro in recorrer_tablero(tablero):
        if tablero[coord_centro] == "A":
            objetivo = "A"
            letra = tablero[coord_centro]
            w = buscar_adyacente(tablero, coord_centro, objetivo)
            # print("Mate {}".format(w))
            if len(w) != 0:
                if tablero[w[0]] == objetivo:
                    if tablero[coord_centro]:
                        objetivo2 = "-"
                        # z busca lugar vacio
                        z = buscar_adyacente(tablero, coord_centro, objetivo2)
                        if len(z) != 0:
                            tablero[z[0]] = letra
                            # print("Posicion libre {}".format(z))


    for coord_centro in recorrer_tablero(tablero):
        if tablero[coord_centro] == "L":
            objetivo = "L"
            letra = tablero[coord_centro]
            w = buscar_adyacente(tablero, coord_centro, objetivo)
            # print("Mate {}".format(w))
            if len(w) != 0:
                if tablero[w[0]] == objetivo:
                    if tablero[coord_centro]:
                        objetivo2 = "-"
                        # z busca lugar vacio
                        z = buscar_adyacente(tablero, coord_centro, objetivo2)
                        if len(z) != 0:
                            tablero[z[0]] = letra
                            # print("Posicion libre {}".format(z))

    return tablero

# print("\n Reproduccion \n \n {}".format(fase_reproduccion(tablero)))


def evolucionar(tablero):

    tablero = fase_alimentacion(tablero)
    # print "\n Ali \n {}".format(tablero)
    tablero = fase_reproduccion(tablero)
    # print "\n Repr \n {}".format(tablero)
    tablero = fase_mover(tablero)
    # print "\n Mover \n {}".format(tablero)

    return tablero

# print(evolucionar(tablero))


def evolucionar_en_el_tiempo(tablero, tiempo_limite):
    for i in range(0, tiempo_limite):
        evolucionar(tablero)

    return tablero


# print(evolucionar_en_el_tiempo(tablero, tiempo_limite=1))


def cuantos_antilopes(tablero):
    count = 0
    for coord_centro in recorrer_tablero(tablero):
        if tablero[coord_centro] == "A":
            count += 1
    if count == 0:
        print "No hay antilopes"
    # print "\n hay {} antilopes".format(count)
    return count

# print cuantos_antilopes(tablero)

def cuantos_leones(tablero):
    count = 0
    for coord_centro in recorrer_tablero(tablero):
        if tablero[coord_centro] == "L":
            count += 1
    if count == 0:
        print "No hay leones"
    # print "\n Hay {} leones.".format(count)
    return count

# print cuantos_leones(tablero)

def cuantos_vacios(tablero):
    num = 0
    for coord_centro in recorrer_tablero(tablero):
        if tablero[coord_centro] == "-":
            num += 1
    if num == 0:
        print "\n No hay lugares vacios"
    else:
        print "\n Hay {} lugares vacios".format(num)
    return num

# print cuantos_vacios(tablero)

def cuantos_de_cada(tablero):
    l1 = []
    l1.append(cuantos_antilopes(tablero))
    l1.append(cuantos_leones(tablero))

    return l1

# print cuantos(tablero)

def mezclar_celdas(tablero):
    celdas = []
    n_fila = tablero.shape[0]
    n_col = tablero.shape[1]
    for i in range(1, n_fila - 1):
        for j in range(1, n_col - 1):
            celdas . append((i, j))
            # Ahora las mezclamos
    random . shuffle(celdas)
    return celdas

# print mezclar_celdas(tablero)

# Funcion que genera un tablero al azar


def generar_tablero_azar(filas, columnas, n_antilopes, n_leones):

    tab = generar_tablero(filas, columnas)
    azar = mezclar_celdas(tab)
    # print azar
    for i in azar[:n_antilopes]:
        n = 0
        while n < n_antilopes:
            n += 1
            tab[i] = 'A'
    # print azar[:n_antilopes]
    for s in azar[n_antilopes:n_antilopes+n_leones]:
        l = 0
        while l < n_leones:
            l += 1
            tab[s] = 'L'
    # print azar[n_antilopes:n_antilopes+n_leones]
    return tab

# print cuantos_de_cada(tablero1)


tablerox = generar_tablero_azar(filas=10, columnas=6, n_antilopes=10, n_leones=2)
print tablerox


def registrar_evolucion(tablerox, tiempo_limite):
    n = 0
    l2 = [cuantos_de_cada(tablerox)]

    while n < tiempo_limite:
        n += 1
        evolucionar_en_el_tiempo(tablerox, tiempo_limite)
        l2.append(cuantos_de_cada(tablerox))
    return l2

print(registrar_evolucion(tablerox, tiempo_limite=100))


# print tablero
# print("\n Alimentacion \n \n {}".format(fase_alimentacion(tablero)))
# print("\n Reproduccion \n \n {}".format(fase_reproduccion(tablero)))
# print("\n Movimiento \n \n{}".format(fase_mover(tablero)))
























