def max_puissance_10(N):
    mp10 = 0
    p10 = 0
    while int(N/10**p10) > 0:
        mp10 = p10
        p10 += 1
    return mp10

def solve(n):
    somme = 0
    N = 2**n
    for i in range(max_puissance_10(N),-1,-1):
        digit = int(N/10**i)
        somme += digit
        N -= digit*10**i
    return somme

assert solve(15) == 26
print(solve(1000))