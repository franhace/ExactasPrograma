import matplotlib.pyplot as plt
from scipy import constants

# dt = 0.001  # para el paso temporal (en segundos)
# numero_pasos = 3000  # el numero de pasos a simular
# g = 9.8  # la aceleracion de la gravedad en s m 2
# y0 = 0  # la posicion desde la que es lanzado el objeto en m
# vy = 10  # la velocidad con la que es lanzado el objeto en m/s
# y1 = 0.01  # la posicion en el instante t=0 + dt en m
# import numpy as np
#
# def actualiz():
#     tiempos = [0, 0.001]
#     alturas = [y0, y1]
#     count = 0
#     for i in range(1, numero_pasos - 1):
#     # actualizo la posicion
#         y_actual = alturas[i]
#         y_prev = alturas[i-1]
#         nueva_posicion = 2 * y_actual - y_prev - g * dt ** 2
#         print(nueva_posicion)
#         alturas.append(nueva_posicion)
#         # actualizo el tiempo
#         nuevo_tiempo = tiempos[i] + dt
#         tiempos.append(nuevo_tiempo)
#
#
#     print("conteo {}".format(count))
#     print("volvio! {}".format(alturas[count]))
#     print(len(alturas))
#     print(tiempos[-1])
#     return alturas[-1]
#
# print(actualiz())

x_tierra = [-147095000000.0, -147095000000.0]
y_tierra = [2617920000.0, 0.0]
dt = 60 * 60 * 24  # para que el paso del tiempo sea un dı́a en segundos.
tiempo_total = 400  # para simular un poco más de un año.
x_sol = 0
y_sol = 0
m_tierra = 5972*10**24
m_sol = 2*10**30
G = constants.G

dias = []
distancias = []
fuerza_x = []
fuerza_y = []
fuerza_total = []
velocidad_final = []
def orbit():
    for i in range(1, tiempo_total - 1):

        # Calculo los deltas
        delta_x = x_sol - x_tierra[-1]
        delta_y = y_sol - y_tierra[-1]

        # Calculo la fuerza de x
        f_x = ((G*m_tierra*m_sol)/((delta_x**2)+(delta_y**2)))*(
            delta_x/((delta_x**2)+(delta_y**2))**0.5)
        fuerza_x.append(f_x)

        # Actualizo la posicion en x
        x_actual = x_tierra[i]
        x_prev = x_tierra[i-1]
        x_nueva = (2 * x_actual) - x_prev + (f_x * dt ** 2) / m_tierra
        x_tierra.append(x_nueva)

        # Idem para y
        # Calculo la fuerza de y
        f_y = ((G * m_tierra * m_sol) / ((delta_x ** 2) + (delta_y ** 2))) * (
            delta_y / ((delta_x ** 2) + (delta_y ** 2))**0.5)
        fuerza_y.append(f_y)

        # Actualizo la pos en y
        y_actual = y_tierra[i]
        y_prev = y_tierra[i-1]
        y_nueva = (2 * y_actual) - y_prev + (f_y * dt ** 2) / m_tierra
        y_tierra.append(y_nueva)

        # Fuerza tot
        s = (f_x**2 + f_y**2)**0.5
        fuerza_total.append(s)

        # Velocidad
        Vfx = (x_nueva - x_actual) / dt
        Vfy = (y_nueva - y_actual) / dt
        Vf = (Vfx**2 + Vfy**2)**0.5
        velocidad_final.append(Vf)

        # Actualizo el tiempo
        dias.append(i)

        # Calculo distancia sol - tierra
        l = (x_actual**2 + y_actual**2)**0.5
        distancias.append(l)

    return distancias


print(orbit())


R = (max(orbit())+min(orbit())/2)
yies = []
for x in range(0, int(R), int(int(R)/50)):
    y = (R**2 - x**2)**0.5
    yies.append(y)
for x in range(0, int(R), int(int(R) / 50)):
    y = ((R ** 2 - x ** 2) ** 0.5)*(-1)
    yies.append(y)
for x in range(-int(R), 0, int(int(R) / 50)):
    y = ((R ** 2 - x ** 2) ** 0.5)*(-1)
    yies.append(y)
for x in range(-int(R), 0, int(int(R)/50)):
    y = (R**2 - x**2)**0.5
    yies.append(y)
yies.sort()
plt.plot(yies)
print(yies)


plt.subplot2grid((1, 3), (0, 0))
plt.title("Rel posicion x-y")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x_tierra, y_tierra)
# plt.plot(fuerza_x)
# plt.plot(fuerza_y)
plt.subplot2grid((1, 3), (0, 2))
plt.title("Fuerza - Dia")
plt.xlabel("Dias")
plt.ylabel("Fuerza")
plt.plot(fuerza_total)
plt.subplot2grid((1, 3), (0, 1))
plt.title("Variacion velocidad con los dias")
plt.xlabel("Dias")
plt.ylabel("Velocidad")
plt.plot(velocidad_final)
plt.show()

