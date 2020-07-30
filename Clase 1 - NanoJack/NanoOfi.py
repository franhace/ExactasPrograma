import random

n = 1

def generar_mazos(n):

    mazo = []

    for jug in range(n):
        for palos in range(4):
            for cartas in range(1, 14):
                mazo.append(cartas)
    random.shuffle(mazo)
    return mazo

s = generar_mazos(n)
print(s)

def jugar(m):

    puntos = 0
    while (not puntos <= 21) and len(m) > 0:
        c = m.pop(0)
        puntos += c

    return puntos

print(jugar(s))