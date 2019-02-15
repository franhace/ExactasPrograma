# Funciones

ojito = [2]

def tres_variables(a, b, c):
    x = (a-b)*c
    y = (a*a - b*b) / c
    r = (x - y)*(x - y) / (x+y)
    return r

ojito.append(tres_variables(2, 4, 7))
print(ojito)
