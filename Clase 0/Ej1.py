nombre1 = "pepes"
nombre2 = "lucas"

def mas_larga(l1, l2):
    if len(l1) == len(l2):
        print("son iguales")
    else:
        if len(l1) > len(l2):
            return l1
        else:
            return l2

res = mas_larga(nombre1, nombre2)
print(res)

