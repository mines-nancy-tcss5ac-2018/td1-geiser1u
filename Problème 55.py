def inverse(N):
    Nlist = list(str(N))
    N2 = 0
    for k in range(len(Nlist)):
        N2 += int(Nlist[k])*10**k
    return N2

def Lychrel(nombre1):
    nombre2 = inverse(nombre1)
    somme1 = nombre1 + nombre2
    somme2 = inverse(somme1)
    compt = 0
    while compt < 50 and somme1 != somme2:
        nombre2 = inverse(nombre1)
        somme1 = nombre1 + nombre2
        somme2 = inverse(somme1)
        nombre1 = somme1
        compt += 1
    if somme1 != somme2:
        return True
    return False

def solve(n):
    nombre_Lychrels = 0
    for i in range(n):
        if Lychrel(i):
            nombre_Lychrels += 1
    return nombre_Lychrels

assert solve(197) == 1
print(solve(10000))