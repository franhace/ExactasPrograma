def cambio_vocales(l1):
    i = 0
    while i < (len(l1)):
        if l1[i] == "a" or l1[i] == "e" or l1[i] == "i" or l1[i] == "o" or l1[i] == "u":
            l1[i] = "-"
        i = i + 1
    return l1

a = "decena"
l1 = list(a)
palabra_guionada = cambio_vocales(l1)
print(cambio_vocales(l1))
print(str(palabra_guionada))

