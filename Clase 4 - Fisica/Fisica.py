# dt = 0.001  # para el paso temporal (en segundos)
# numero_pasos = 1500  # el numero de pasos a simular
# g = 9.8  # la aceleracion de la gravedad en s m 2
# y0 = 0  # la posicion desde la que es lanzado el objeto en m
# vy = 10  # la velocidad con la que es lanzado el objeto en m/s
# y1 = 0.01  # la posicion en el instante t=0 + dt en m
# # import numpy as np
# def actualiz():
#     tiempos = [0, 0.001]
#     alturas = [y0, y1]
#     for i in range(1, numero_pasos - 1):
#     # actualizo la posicion
#         y_actual = alturas[i]
#         y_prev = alturas[i-1]
#         nueva_posicion = 2 * y_actual - y_prev - g * dt ** 2
#         alturas.append(nueva_posicion)
#         # actualizo el tiempo
#         nuevo_tiempo = tiempos[i] + dt
#         tiempos.append(nuevo_tiempo)
#         count = 0
#         while nueva_posicion <= 0:
#             count += 1
#         print(count)
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
m_tierra = 5972190000000000000000000
m_sol = 1898130000000000000000000000
G = 6693
dias = []
def orbit():
    for i in range(1, tiempo_total - 1):
        # calculo los deltas
        delta_x = x_sol - x_tierra[-1]
        delta_y = y_sol - y_tierra[-1]
        print(delta_x)
        # calculo la fuerza de x
        f_x = ((G*m_tierra*m_sol)/((delta_x**2)+(delta_y**2)))*(
            delta_x/((delta_x**2)+(delta_y**2))**0.5)
        # actualizo la posicion x
        x_actual = x_tierra[i]
        x_prev = x_tierra[i-1]
        x_nueva = (2 * x_actual) - x_prev + (f_x * dt ** 2) / m_tierra
        x_tierra.append(x_nueva)
        # idem para y
        # calculo la fuerza de y
        f_y = ((G * m_tierra * m_sol) / ((delta_x ** 2) + (delta_y ** 2))) * (
            delta_y / ((delta_x ** 2) + (delta_y ** 2))**0.5)
        y_actual = y_tierra[i]
        y_prev = y_tierra[i-1]
        y_nueva = (2 * y_actual) - y_prev + (f_y * dt ** 2) / m_tierra
        y_tierra.append(y_nueva)
        # actualizo el tiempo
        dias.append(i)
    print(x_tierra)
    print(y_tierra)
    return f_x




print(orbit())