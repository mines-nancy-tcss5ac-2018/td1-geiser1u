f = open("p022_names.txt", "r")
noms_en_desordre = []
for ligne in f:
    noms_en_desordre += ligne.split(",")

def nombre_lettre(l):
    alphabet = ['"',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for j in range(len(alphabet)):
        if alphabet[j] == l:
            return j

def solve(noms):
    noms_classes = sorted(noms)    
    somme = 0
    for i in range(len(noms_classes)):
        score = 0
        for lettre in noms_classes[i]:
            score += nombre_lettre(lettre)
        score *= i+1
        somme += score
    return somme

assert solve(["PAUL","MARIE"]) == 146
print(solve(noms_en_desordre))