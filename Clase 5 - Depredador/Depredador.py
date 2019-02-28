import numpy as np
t = np . repeat("-", 7*7) . reshape(7, 7) # completa el array con valor entre ""
# podemos verlo con:

# # podemos acceder a un elemento individual por su fila y columna :
# print ( " La posicion (1,1) tiene el elemento : ", t[(1, 2)])
# # podemos verlo con :
# print ("la posicion (1,7) tiene el elemento :", t[(1, 2)])
# # como el tablero tiene dos dimensiones , podemos accederlas como :
# print (" Mi tablero tiene ", t . shape[0], "filas y", t . shape [1] , "columnas" )

# Hace que los bordes del tablero sean montañas "M"
t[0, :] = range(0, 7)
t[6, :] = range(0, 7)
t[:, 0] = range(0, 7)
t[:, 6] = range(0, 7)

# Definimos la coordenadas de nuestros personajes
x = [1, 2, 3, 3, 4, 1]
y = [3, 1, 1, 3, 2,  2]
tipo = ["A", "A", "A", "A", "A", "L"]
# Los asignamos dentro del tablero
for i in range(len(tipo)):
    t[(x[i], y[i])] = tipo[i]
tablero = t
print(tablero)

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
    for i in range(1, n_fila - 1):
        for j in range(1, n_col - 1):
            coord_centro = (i, j)
            centros.append(coord_centro)
    return centros


# print(recorrer_tablero(tablero))


def fase_mover(tablero):
    objetivo = "-"
    for coord_centro in recorrer_tablero(tablero):
        if tablero[coord_centro] == "L" or tablero[coord_centro] == "A":
            letra = tablero[coord_centro]
            w = buscar_adyacente(tablero, coord_centro, objetivo)
            tablero[w[0]] = letra
            tablero[coord_centro] = '-'
    return tablero


print("\n Movimiento \n {}".format(fase_mover(tablero)))


def fase_alimentacion(tablero):
    objetivo = "A"
    for coord_centro in recorrer_tablero(tablero):
        if tablero[coord_centro] == "L":
            letra = tablero[coord_centro]
            w = buscar_adyacente(tablero, coord_centro, objetivo)
            tablero[w[0]] = letra
            tablero[coord_centro] = '-'
    return tablero


print("\n Alimentacion \n {}".format(fase_alimentacion(tablero)))


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
                        z = buscar_adyacente(tablero, coord_centro, objetivo2)
                        tablero[z[0]] = letra
                        # print("Posicion libre {}".format(z))
                        tablero[w[0]] = letra

    return tablero

print("\n Reproduccion \n {}".format(fase_reproduccion(tablero)))
