pal1 = "cosa"
pal2 = "cosass"

def mezclar(pal1, pal2):
    i = 0
    res = []
    while i < len(pal1) or i <len(pal2):
        if i < len(pal1):
            res.append(pal1[i])
        if i < len(pal2):
            res.append(pal2[i])
        i = i + 1
    return res

print(mezclar(pal1, pal2))