import random

import numpy as np
random.random()



# def hacer_bosque(n):
#     for i in range(n):
#         bosque.append(i)
#         contador = 0
#         lleno = False
#         while not lleno:
#             arbol = np.random.randint(2, size=n)
#             contador += 1
#             bosque[arbol-1] = 1
#             suma = 0
#             for i in range(n):
#                 suma += bosque
#                 if suma == n:
#                     lleno = True
#         return contador
#
# print hacer_bosque(10)

# Funcion que hace un bosque de n arboles
def bosque(n):
    bosquecito = []
    x = np.random.randint(-1, 2, size=n)
    for i in x:
        bosquecito.append(i)
    return bosquecito

# print bosque(n=10)

# bosque.copy # hacer una copia y devolver una copia

# Tira un numero al azar y devuelve un bool, si la prob es mayor
# a la pedida

def suceso_aleatorio(prob):
    p = random.random()
    if p > prob:
        i = True
    else:
        i = False
    return i


def brotes(bosque):
    r = bosque(n=10)
    print r
    for i in range(len(r)):
        if suceso_aleatorio(prob) == True
        r[i]=1


    return r

print brotes(bosque)



# Devuelve la cantidad de posiciones en las que hay un arbol lleno, vacio o quemado
# def cuantos(bosque, n):
#     for i in bosque:
#         cuantos_hay = bosque.count(n)
#         return cuantos_hay
#
# print cuantos(bosque, n=10)



