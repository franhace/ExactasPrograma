import numpy as np
t = np . repeat("-", 7*7) . reshape(7, 7) # completa el array con valor entre ""
# podemos verlo con:

# # podemos acceder a un elemento individual por su fila y columna :
# print ( " La posicion (1,1) tiene el elemento : ", t[(1, 2)])
# # podemos verlo con :
# print ("la posicion (1,7) tiene el elemento :", t[(1, 2)])
# # como el tablero tiene dos dimensiones , podemos accederlas como :
# print (" Mi tablero tiene ", t . shape[0], "filas y", t . shape [1] , "columnas" )
t[0, :] = 'M'
t[6, :] = 'M'
t[:, 0] = 'M'
t[:, 6] = 'M'

# definimos la coordenadas de nuestros personajes
x = [1, 2, 3, 3, 1]
y = [3, 1, 1, 3, 2]
tipo = ["A", "A", "A", "A", "L"]
# y ahora los asignamos dentro del tablero
for i in range(len(tipo)):
    t[(x[i], y[i])] = tipo[i]
# veamos como queda :


coord_centro = (1, 2)
def mis_vecinos(coord_centro):

    c = coord_centro[0]
    f = coord_centro[1]
    coord_vecinas = [(c-1, f-1), (c, f-1), (c+1, f-1),
                     (c-1, f), (c, f), (c+1, f),
                     (c-1, f+1), (c, f+1), (c+1, f+1)]


    return coord_vecinas

tablero = t

objetivo = ""

def buscar_adyacente(tablero, coord_centro, objetivo):

    adyacente = []
    l = mis_vecinos(coord_centro)
    for i in l:
        if tablero[i] == objetivo:
            adyacente.append(i)
            return adyacente
    return []

#
# def recorrer_tablero(tablero):
#     n_fila = t.shape[0]
#     n_col = t.shape[1]
#     for i in range(1, n_fila - 1):
#         for j in range(1, n_col - 1):
# para que el if de la funcion fase mover funcione, deberiamos
# para empezar recorrer el tablero con excepcion de las M
print t
def fase_mover(tablero):
    objetivo = "-"

    if tablero[coord_centro] != "-":
        s = tablero[coord_centro]
        tablero[buscar_adyacente(tablero, coord_centro, objetivo)] = s
        tablero[coord_centro] = "-"
    return tablero

print fase_mover(tablero)
print t

def fase_alimentacion(tablero):
    objetivo = "A"

    if tablero[coord_centro] == "L":
        s = tablero[coord_centro]
        tablero[buscar_adyacente(tablero, coord_centro, objetivo)] = s
        tablero[coord_centro] = "-"

    return tablero

def fase_reproduccion(tablero):
    objetivo = "-"

    if tablero[coord_centro] != "-":
        s = tablero[coord_centro]
        tablero[buscar_adyacente(tablero, coord_centro, objetivo)] = s

    return tablero
