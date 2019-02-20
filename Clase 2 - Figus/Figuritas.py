import random
import numpy as np
#
#
# # random.random()
# # a = np.arange(10)
# # len(a)
# # a[:3]
# # random.shuffle(a)
# # np.mean(a)
# # random.randint(1, 6)
#
# album_completo = range(1, 7)
#
# n = 6 # numero de figuritas total del album
#
# # LLena album y se fija cuantas figuritas tuvo que sacar
# def llenar_album(n):
#
#     count = 0
#     figuritas_sacadas = []
#     while not (len(figuritas_sacadas) == n):
#         figurita = random.randint(1, n)
#
#         if figurita not in figuritas_sacadas:
#             figuritas_sacadas.append(figurita)
#             count += 1
#         else:
#             count += 1
#
#     # print figuritas_sacadas
#     # figuritas_sacadas.sort()
#     return count
#
# # print llenar_album(n)
#
#
# figus_total = 669
#
# def cuantas_figus(figus_total):
#
#     return llenar_album(figus_total)
#
# # print cuantas_figus(figus_total)
#
#
#  # numero de repeticiones
# nrep = 10
#
# # Promedio de cantidad de figus que hubo que sacar para completar album
# def cantidad_de_figuritas(n):
#     n = nrep
#     i = 0
#     l1 = []
#     while i < n:
#         r = cuantas_figus(figus_total)
#         l1.append(r)
#         i += 1
#     promedio = np.mean(l1)
#     return promedio
#
# print cantidad_de_figuritas(n)
#
# # Lista que contiene el numero de figuritas que hubo que sacar
# n_repeticiones = 10
# def lista_num_figuritas(n_repeticiones):
#     n = n_repeticiones
#     i = 0
#     l1 = []
#     while i < n:
#         r = cantidad_de_figuritas(n)
#         l1.append(r)
#         i += 1
#     return l1
#
# print lista_num_figuritas(n_repeticiones)

n = 8 # num de figus del album
l = 5 # num de figus del paquete


def paquete_de_n_figuritas(n):

    count = 0
    figuritas_sacadas = []
    i = 0
    paquete = []
    while not (len(figuritas_sacadas) == n):
        while (len(paquete) != l):
            figurita = random.randint(1, n)
            figuritas_sacadas.append(paquete)
            if paquete not in figuritas_sacadas:
                figuritas_sacadas.append(paquete)
                count += 1
            else:
                count += 1

        print paquete

        print figuritas_sacadas
    # figuritas_sacadas.sort()
    return count

print paquete_de_n_figuritas(n)