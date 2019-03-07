import random

npart = 2
lim_caja = 10
const_F = 10
cant_pasos = 200
dt = 2
xmax = 15
ymax = 15
xmin = 0
ymin = 0
vels = [[3, 2], [2, 2]]
vy = [2, 2]

# Funcion que nos da una lista de listas
# de posiciones iniciales

def pos_ini(npart):
    x = []
    y = []
    coord_ini = []
    n = 0
    while n < npart:
        n += 1
        xs = random.randint(0, 16)
        ys = random.randint(0, 16)
        # Evitamos que haya coord iguales
        if xs not in x:
            if ys not in y:
                x.append(xs)
                y.append(ys)

        coord_ini.append([xs, ys])

    return coord_ini

pos = pos_ini(npart)
print("pos ini {}".format(pos))

print("vels ini {}".format(vels))
def pos_vel_nuevas(cant_pasos):
    j = [[3, 2], [2, 2]]
    n = 0
    count = 0
    while n < cant_pasos:
        n += 1
        for i in pos:
            count += 1
            print("\nparticula {}".format(count))
            x = i[0]
            y = i[1]
            print("x  {}".format(x))
            print("y  {}".format(y))
            print(j[0][0])
            #estudiamos nuestra pos en x
            i[0] += j[0][0] * dt
            ifx = i[0]
            # estudiamos nuestra pos en y
            i[1] += j[0][1] * dt
            ify = i[1]

            print("xf{}  {}".format(count, ifx))
            print("yf{}  {}".format(count, ify))

            # Estudiamos las posiciones de c part
            # en x
            if ifx >= xmax or ifx < 0 :
                if ifx > xmax:
                    print("se pasó x por arriba")

                    j[0][0] = (j[0][0]) * -1

                    i[0] += j[0][0] * dt
                    print(i[0])
                elif ifx < 0:
                    print("se pasó x por abajo")

                    j[0][0] = (j[0][0]) * -1

                    i[0] += j[0][0] * dt
                    print(i[0])
            # Estudiamos las posiciones de c part
            # en y
            if ify >= ymax or ify < 0:
                if ify > ymax:
                    print("se pasó y por abajo")
                    j[0][1] = (j[0][1]) * -1

                    i[1] += j[0][1] * dt
                    print(i[1])
                elif ify < 0:
                    print("se pasó y por abajo")

                    j[0][1] = (j[0][1]) * -1

                    i[1] += j[0][1] * dt
                    print(i[1])

            print("i {}".format(i))
            # for j in vels:
            #
            #     # estudiamos nuestra pos en x
            #     i[0] += j[0] * dt
            #     x = i[0]
            #     # estudiamos nuestra pos en y
            #     i[1] += j[1] * dt
            #     y = i[1]
            #     print("x  {}".format(x))
            #     print("y  {}".format(y))
            #     if i[0] > xmax:
            #         j[0] = -(j[0])
            #         i[0] += j[0] * dt
            #     elif i[1] > ymax:
            #         j[1] = -(j[1])
            #         i[1] += j[1] * dt
            #     print(count)
                # elif i[0] < 0:
                #     print("epa")
                #     print(j[0])
                #     j[0] = (j[0])*-1
                #     print(j[0])
                #     i[0] += j[0] * dt
                # elif i[1] < 0:
                #     j[1] = (j[1])*-1
                #     i[1] += j[1] * dt

    return pos
print (pos_vel_nuevas(cant_pasos))


def velocidades_choque(xy):
    Vx = 2
    for i in xy:
        for X in [i][0]:
            if X > xmax:
                Vx = -(Vx)
                X = X - 2 * (X - xmax)
                print (X)
# print velocidades_choque(pos)
# Funcion que se fija si particula choco
# con los bordes

# def choque(x, xmax, ymax ):
#     for i in x:
#         if x[i] > xmax:
#             x[i]




















