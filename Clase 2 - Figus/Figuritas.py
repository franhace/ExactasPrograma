import random
import numpy as np


# random.random()
# a = np.arange(10)
# len(a)
# a[:3]
# random.shuffle(a)
# np.mean(a)
# random.randint(1, 6)


# LLena album y se fija cuantas figuritas tuvo que sacar

def cuantas_figus(figus_total= 669):
    count = 0
    figuritas_sacadas = []
    while not (len(figuritas_sacadas) == figus_total):
        figurita = random.randint(1, figus_total)

        if figurita not in figuritas_sacadas:
            figuritas_sacadas.append(figurita)
            count += 1
        else:
            count += 1

    # print figuritas_sacadas
    # figuritas_sacadas.sort()
    return count


# Promedio de cantidad de figus que hubo que sacar para completar "nrep" albumes
def promedio_figus(nrep=1000, figus_total=669):
    i = 0
    l1 = []
    while i < nrep:
        r = cuantas_figus(figus_total)
        l1.append(r)
        i += 1
    promedio = np.mean(l1)
    return promedio


# Lista que contiene el numero de figuritas que hubo que sacar

def lista_num_figuritas(n_repeticiones=10, cantidad_de_figuritas=669):
    i = 0
    l1 = []
    while i < n_repeticiones:
        r = cuantas_figus(n_repeticiones)
        l1.append(r)
        i += 1
    return l1


# Funcion que nos genera un paquete

def generar_paquete(figus_total, figus_paquete):
    paquete = random.sample(range(figus_total + 1), figus_paquete)
    return paquete

# Funcion que nos devuelve cuantos paquetes hubo que sacar para completar el album de "figus_total" figuritas y "figus_paquete"
# figuritas por paquete.

def cuantos_paquetes(figus_total, figus_paquete):
    count = 0
    repetidas = 0
    num_paquetes = 0
    conjunto_paquetes = []
    while not (len(conjunto_paquetes) == figus_total):
        paquete = random.sample(range(figus_total + 1), figus_paquete)
        num_paquetes += 1
        for f in paquete:
            if f not in conjunto_paquetes:
                conjunto_paquetes.append(f)
                count += 1
            else:
                count += 1
                repetidas += 1

    # print("num de paquetes: {}".format(num_paquetes))
    # print("num de repetidas: {}".format(repetidas))
    # print("num total de figus: {}".format(count))
    return num_paquetes

# Funcion que nos devuelve el promedio de paquetes que hubo que comprar para completar "n_repeticiones" albumes,
# de "figus_total" figuritas y "figus_paquete" figuritas por paquete

def promedio_paquetes(n_repeticiones, figus_total, figus_paquete):
    i = 0
    rep = []
    # lleno = False y cambiarlo en vez de "n_repeticiones" -> while not lleno
    while i < n_repeticiones:
        rep.append(cuantos_paquetes(figus_total, figus_paquete))
        i += 1
        s = np.mean(rep)
    # print(i)
    return s


# Funcion que devuelve el porcentaje de alb completados con 850 paquetes o menos

def promedio_850(n_repeticiones=10, figus_total=669, figus_paquete=5):
    i = 0  # cuenta repeticiones totales
    rep = []  # lista de paquetes totales sacados para completar alb
    s = []  # lista de alb completados con 850 paquetes o menos
    t = 0  # cuenta cuantas repeticiones no se completaron con 850 paquetes
    while i < n_repeticiones:
        rep.append(cuantos_paquetes(figus_total, figus_paquete))
        i += 1
    for numpak in rep:
        if numpak <= 850:
            s.append(numpak)
            t += 1
    print (t)
    print("i: {}".format(i))
    print (rep)
    promedio = (t / i ) * 100

    return promedio

print (promedio_850(n_repeticiones=10, figus_total=669, figus_paquete=5))
# Funcion que se fija cuantas repeticion habria que hacer para que
# las chances de completar el album con 850 figuritas sea mayor al 90%
#
# def cuantos_paq_90p():
#
#     z = 100
#     while (promedio_850(n_repeticiones=z, figus_total=669, figus_paquete=5)) < 90:
#         z += 1
#         print(z)
#     return z
#
# print(cuantos_paq_90p())
#
