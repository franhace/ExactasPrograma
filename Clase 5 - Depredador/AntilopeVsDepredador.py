import numpy as np
import random
import csv
import matplotlib.pyplot as plt


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


# tablero = generar_tablero(filas=4, columnas=6)

# n_fila = tablero.shape[0] ## elige la fila como primer valor
# n_col = tablero.shape[1] ## columna como segundo

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


# Funcion que recorre los casilleros activos del tablero

def recorrer_tablero(tablero):
    n_fila = tablero.shape[0]
    n_col = tablero.shape[1]
    centros = []
    for i in range(1, n_fila -1):
        for j in range(1, n_col - 1):
            coord_centro = (i, j)
            centros.append(coord_centro)
    return centros


# Funcion que define el movimiento de cada personaje.
# 1º se fija si hay un personaje en el centro
# 2º busca si hay un lugar vacio adyacente
# 3º Mueve el personaje a ese lugar y lo borra del lugar anterior

def fase_mover(tablero):
    objetivo = "-"
    for coord_centro in recorrer_tablero(tablero):
        if tablero[coord_centro] == "L" or tablero[coord_centro] == "A":
            letra = tablero[coord_centro]
            w = buscar_adyacente(tablero, coord_centro, objetivo)
            print(coord_centro)
            print(w)
            if len(w) != 0:
                tablero[w[0]] = letra
                tablero[coord_centro] = '-'
    return tablero

# print("\n Movimiento \n \n{}".format(fase_mover(tablero)))

# Funcion para la alimentacion de los leones
# Busca leon y si hay un A adyacente lo mueve a esa pos

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

# Funcion para la reproduccion de los personajes
# 1º busca si el personaje es antilope o leon
# 2º se fija si hay un personaje del mismo tipo en la cercania
# 3º se fija si hay un lugar vacio en la cercania, y produce ese personaje
# 4º de no haberlo no se reproduce

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


# Funcion que define el orden de las fases

def evolucionar(tablero):

    tablero = fase_alimentacion(tablero)
    print("A{}".format(tablero))
    # print("\n Ali \n {}".format(tablero))
    tablero = fase_reproduccion(tablero)
    print("R {}".format(tablero))
    # print("\n Repr \n {}".format(tablero))
    tablero = fase_mover(tablero)
    print("M {}".format(tablero))
    # print("\n Mover \n {}".format(tablero))

    return tablero


# Funcion que define un tiempo limite de evolucion

def evolucionar_en_el_tiempo(tablero, tiempo_limite):
    for i in range(0, tiempo_limite):
        evolucionar(tablero)

    return tablero

# print(evolucionar_en_el_tiempo(tablero, tiempo_limite=1))


### Funciones que cuentan cuantos personajes o lugares vacios hay

def cuantos_antilopes(tablero):
    count = 0
    for coord_centro in recorrer_tablero(tablero):
        if tablero[coord_centro] == "A":
            count += 1

    # print "\n hay {} antilopes".format(count)
    return count


def cuantos_leones(tablero):
    count = 0
    for coord_centro in recorrer_tablero(tablero):
        if tablero[coord_centro] == "L":
            count += 1
    if count == 0:
         print ("No hay leones")
    # print "\n Hay {} leones.".format(count)
    return count


def cuantos_vacios(tablero):
    num = 0
    for coord_centro in recorrer_tablero(tablero):
        if tablero[coord_centro] == "-":
            num += 1
    if num == 0:
        print ("\n No hay lugares vacios")
    else:
        print ("\n Hay {} lugares vacios".format(num))
    return num

###


# Funcion que devuelve una lista con 1ºnº A, 2ºnº de L
def cuantos_de_cada(tablero):
    l1 = []
    l1.append(cuantos_antilopes(tablero))
    l1.append(cuantos_leones(tablero))
    print("A : {} ; L : {}".format(cuantos_antilopes(tablero),
                                   cuantos_leones(tablero)))

    return l1


# Funcion que devuelve una lista de posiciones activas de un tablero,
# al azar

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


<<<<<<< HEAD
=======
# Funcion que genera un tablero con personajes, filas y columnas
# deseadas, y posiciona los personajes al azar

>>>>>>> c9a90db4c69d8f457794b2aa7e0a65e58077ad79
def generar_tablero_azar(filas, columnas, n_antilopes, n_leones):

    tab = generar_tablero(filas, columnas)
    azar = mezclar_celdas(tab)
    for i in azar[:n_antilopes]:
        n = 0
        while n < n_antilopes:
            n += 1
            tab[i] = 'A'
    for s in azar[n_antilopes:n_antilopes+n_leones]:
        l = 0
        while l < n_leones:
            l += 1
            tab[s] = 'L'
    return tab


tablero = generar_tablero_azar(filas=5, columnas=5,
                                n_antilopes=3, n_leones=2)

# Funcion que devuelve una lista, con cuantos A y L
# quedaron luego de cada ciclo hasta un tiempo limite

def registrar_evolucion(tablero, tiempo_limite):
    n = 0
    l2 = [cuantos_de_cada(tablero)]

    while n < tiempo_limite:
        n += 1
        print("\n Ciclo {} ".format(n))
        print(evolucionar_en_el_tiempo(tablero, tiempo_limite))
        l2.append(cuantos_de_cada(tablero))
        x = l2[-1]
        y = x[0]
        z = x[1]
        print(tablero)

        if y == 0 or z == 0:
            print("\n Se acabó la diversidad en el ciclo {} \n".format(n))
            break

    return l2


z = (registrar_evolucion(tablero, tiempo_limite=2))

plt.plot(z)
plt.show()

registro = z


# Crea un tabla en un archivo llamado predpres, que toma con datos
# la cantidad de A y de L luego de cada turno

with open("predpres.csv", "w", newline="") as csvfile:
    file_writer = csv.writer(csvfile)
    file_writer.writerow(["antilopes", "leones"])
    file_writer.writerows(registro)


