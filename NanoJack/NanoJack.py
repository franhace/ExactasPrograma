import random

n = 2

def crear_mazo():

    a = 0
    cartas = []
    while a < 4:
        for c in range(1, 4):
            cartas.append(c)
        a = a + 1
    return cartas


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

m = generar_mazos(n)
print(m)

def jugar(m):

    m = generar_mazos(n)
    for c in m:
        suma = 0
        while suma < 21:
            m.pop(0)
        return suma
    return m



s = jugar(m)
print(s)




