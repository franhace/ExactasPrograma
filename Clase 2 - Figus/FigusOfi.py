import random

album = []

def llenar_album(n):
    for i in range (n):
        album.append(i)
        contador = 0
        lleno = False
        while not lleno:
            figu = random.randint(1, n)
            contador += 1
            album[figu-1] = 1
            suma = 0
            for i in range(n):
                suma += album
                if suma == n:
                    lleno = True
    return contador

print llenar_album(6)