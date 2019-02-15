def cant_e(l1):
    i = 0
    count = 0
    while i < (len(l1)):
        if l1[i] == "e":
            count = count + 1
        i = i + 1
    return count

a = "decena"
l1 = list(a)
print(cant_e(l1))

def cuento_vocales(l1):
    i = 0
    count = 0
    while i < (len(l1)):
        if l1[i] == "a" or l1[i] == "e" or l1[i] == "i" or l1[i] == "o" or l1[i] == "u":
            count = count + 1
        i = i + 1
    return count

a = "decena"
l1 = list(a)
print(cuento_vocales(l1))
