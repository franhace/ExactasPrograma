# Strings

nombre = "Marianito"
print("Mi nombre es:", nombre) # "coma" genera espacio, "mas" no

print(len([]))
print(len(nombre))

print(nombre[0])
print(nombre[5])
# print(nombre[10]) #IndexError

print([0, len(nombre)])

apellido = "Cachirulo"
print("Nombre completo: ", apellido, ", ", nombre)
print("Nombre completo: ", apellido + ", " + nombre)

print(len(("Nombre completo: ", apellido, ", ", nombre)))
print(len(("Nombre completo: ", apellido + ", " + nombre)))

dif_largo = (len(("Nombre completo: ", apellido, ", ", nombre))) - (len(("Nombre completo: ", apellido + ", " + nombre)))
print(dif_largo) # diferencia en el largo con coma y mas

# nombre[8] = "a" ### Error: 'str' object does not support item assignment
# porque strings son inmutables, para modificarla -> lista

milista = list(nombre) # string -> list
# milista[8] = "a" ## alternativa
milista[len(milista)-1] = "a"
print(milista)
print(nombre)



