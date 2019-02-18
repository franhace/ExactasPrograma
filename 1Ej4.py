a = "elet"
b = "cucs"

l1 = list(a)
l2 = list(b)

def mas_corta(l1, l2):
    if len(l1) == len(l2):
        print("son iguales")
    else:
        if len(l1) < len(l2):
            return l1
        else:
            return l2

res2 = (mas_corta(l1, l2))


def mezclar(l1, l2):
    i = 0
    l3 = []
    while i < len(mas_corta(l1, l2)):
        l3.append(l1[i])
        l3.append(l2[i])
        i = i + 1

    return l3

print(type(res2))
print(mezclar(l1, l2))









