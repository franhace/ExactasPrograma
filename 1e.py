# Conditional Statements

mivalor = 7
if mivalor == 2:
    mivalor = 5
    if mivalor == 5:
        mivalor = 4
        print(mivalor)
    else:
        mivalor = 2
else:
    mivalor = 8

print(mivalor)

def multiplo_raro(a):
    if a == 2:
        res = a*a+1
    elif a == 3:
        res = a+a-1
    elif a == 7:
        res = a*a+5
    elif a == 11:
        res = a*(a-2)+9
    else:
        res = a*a-2
    return res

prueba = multiplo_raro(3)
print(prueba)
