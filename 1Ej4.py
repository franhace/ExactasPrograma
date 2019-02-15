a = "elemento"
b = "cucharas"

l1 = list(a)
l2 = list(b)

def mas_larga(l1, l2):
    if len(l1) == len(l2):
        print("son iguales")
    else:
        if len(l1) > len(l2):
            return l1
        else:
            return l2
res = mas_larga(a, b)

def mezclar(l1, l2):
    i = 0
    l3 = []
    while i < len(l1):
        l3.append(l1[i])
        l3.append(l2[i])
        i = i + 1
    return l3

print(mezclar(l1, l2))









