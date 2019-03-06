import random

npart = 2
lim_caja = 10
const_F = 10
cant_pasos = 3
dt = 10
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
print pos

print vels
def pos_vel_nuevas(cant_pasos):
    n = 0
    while n < cant_pasos:
        n += 1
        for i in pos:
            for j in vels:
                # estudiamos nuestra pos en x
                i[0] += j[0] * dt
                # estudiamos nuestra pos en y
                i[1] += j[1] * dt
                if i[0] > xmax:
                    j[0] = -(j[0])
                    i[0] += j[0] * dt
                if i[1] > ymax:
                    j[1] = -(j[1])
                    i[1] += j[1] * dt
                if i[0] < 0:
                    j[0] = -(-j[0])
                    i[0] += j[0] * dt
                if i[1] < 0:
                    j[1] = -(-j[1])
                    i[1] += j[1] * dt

    return pos
print pos_vel_nuevas(cant_pasos)

print vels


def velocidades_choque(xy):
    Vx = 2
    for i in xy:
        for X in [i][0]:
            if X > xmax:
                Vx = -(Vx)
                X = X - 2 * (X - xmax)
                print X
# print velocidades_choque(pos)
# Funcion que se fija si particula choco
# con los bordes

# def choque(x, xmax, ymax ):
#     for i in x:
#         if x[i] > xmax:
#             x[i]




















