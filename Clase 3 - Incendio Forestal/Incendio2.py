import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
from scipy.interpolate import interp1d
from scipy import interpolate


# Funcion que hace un bosque de n arboles
def bosque_vacio(n):
    bosquecito = []
    x = np.random.randint(0, 1, size=n)
    for i in x:
        bosquecito.append(i)
    return bosquecito


def bosque_limpio(n):
    bosquecito = []
    x = np.random.randint(0, 2, size=n)
    for i in x:
        bosquecito.append(i)
    return bosquecito


def bosque_quemado(n):
    bosquecito = []
    x = np.random.randint(-1, 2, size=n)
    for i in x:
        bosquecito.append(i)
    return bosquecito


# bosque.copy # hacer una copia y devolver una copia

# Tira un numero al azar y devuelve un bool, si la prob es mayor
# a la pedida

def suceso_aleatorio(prob):
    d = random.random()

    if d > prob:
        i = True
    else:
        i = False
    return i


# print(suceso_aleatorio(prob=0.6))



# Funcion que a partir de un bosque y de un valor p, genere un arbol
# en cada celda vacia con probabilidad p

def brotes(bosque, p):
    cont = 0

    for i in range(0, len(bosque)):
        if (suceso_aleatorio(p) == True):
            if bosque[i] != 1:
                bosque[i] = 1
                cont += 1
    # print("{} arboles crecieron".format(cont))
    return bosque


# Devuelve la cantidad de posiciones en las que hay un arbol lleno,
# vacio o quemado

def cuantos(bosque, tipo_celda):
    x = bosque.count(tipo_celda)
    # print("hay {} arboles de tipo {}".format(x, tipo_celda))
    return x


f = 0.02


# Funcion que hace caer rayos sobre el bosque con probabilidad f
def rayos(bosque, f):
    count = 0
    for i in range(0, len(bosque)):
        if suceso_aleatorio(f) == False:
            if bosque[i] == 1:
                bosque[i] = -1
                count += 1
    # print("{} arboles fueron electrocutados".format(count))
    return bosque


def propagacion(bosque):
    count = 0
    for i in range(0, len(bosque) - 1):
        if bosque[i] == -1:
            if bosque[i + 1] == 1:
                bosque[i + 1] = -1
                count += 1
    bosque.reverse()
    for i in range(0, len(bosque) - 1):
        if bosque[i] == -1:
            if bosque[i + 1] == 1:
                bosque[i + 1] = -1
                count += 1
    bosque.reverse()
    # print("{} arboles fueron quemados por propagacion".format(count))
    return bosque


# w = cuantos(bosque, tipo_celda=1), cuantos(bosque, tipo_celda=0), cuantos(bosque, tipo_celda=-1)


# Funcion que limpia los arboles quemados , y genera un espacio vacio en su lugar
def limpieza(bosque):
    count = 0
    for i in range(0, len(bosque)):
        if bosque[i] == -1:
            bosque[i] = 0
            count += 1

    # print("{} arboles fueron limpiados".format(count))
    return bosque


# Funcion que toma "n_rep" años y va ciclando por el mismo bosque durante
# esos años y nos devuelve el promedio de arboles que sobrevivieron.

# Durante estos años hay 4 eventos que son:
# Primavera -> brota arboles con probabilidad "p"
# Rayos -> hace caer rayos con probabilidad "f"
# Propaga -> propaga el fuego desde arboles quemados a los contiguos
# Limpieza -> limpia arboles quemados
#


def incendio_forestal(anios, p):
    f = 0.4  # proba de electrocucion
    t = 0  # Año
    l1 = []  # lista de numero de arboles que sobrevivieron
    l2 = []  # lista de p's

    foret = bosque_vacio(n=1000)

    while t < anios:
        # print("\n Año {} \n".format(t))
        t += 1
        # p = random.random()

        l2.append(p)

        brotes(foret, p)

        rayos(foret, f)

        propagacion(foret)

        limpieza(foret)

        x = cuantos(foret, tipo_celda=1)  # num de arboles que sobrevivieron

        l1.append(x)

        # print("Este año {} sobrevivieron {} arboles".format(t, x))

    w = max(l1)
    z = l1.index(w)
    # print("\nmaximo numero de arboles: {}\n"
    #       "Año: {}\n"
    #       "p = {} \n".format(w, z, l2[z]))

    return l1


# print("\n Sobrevivieron en promedio {} arboles por año \n".format(incendio_forestal(n_rep)))

# print(incendio_forestal(anios, p))

# Funcion que dependiendo de la facilidad "f" de un bosque para prenderse
# fuego, nos devuelve el valor optimo de arboles que deberian nacer por
# # año
# # f= 0.02
muestra = 1000  # "vuelta" que equivale a p's crecientes que toma, para distintos bosques
anios = 10  # numero de años que va a tener un bosque


def valor_optimo(muestra, anios):
    i = 0
    l1 = []  # cantidad de total de arboles que sobrevivieron por vuelta
    l2 = []  # p por vuelta
    p = 0.01
    while i < muestra and p < 0.99999:
        # print("vuelta {}".format(i))
        i += 1
        p += 0.001
        l2.append(p)
        w = incendio_forestal(anios, p)
        l1.append(w[-1])
        # print("\nal final de la vuelta {} sobrevivieron {} arboles, con p= {}\n".format(i-1, w[-1], p))

    print(l1)
    plt.plot(l2, l1)
    # plt.subplot(221)
    # plt.plot(l1)
    # plt.plot(l2)
    # plt.subplot(222)
    # (interpolate.splrep(l2, l1, s))
    print(len(l1))

    return l2


print(valor_optimo(muestra, anios))

plt.title("Cantidad de arboles que sobrevivieron, tomando bosques con distintos p's")
plt.xlabel("p (probabilidad de caida de rayos)")
plt.ylabel("Cantidad de arboles (por bosque)")
plt.show()