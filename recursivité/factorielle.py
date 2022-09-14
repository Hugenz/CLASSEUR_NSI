def factorielle(n):
    if n == 0:
        return 1
    return n*factorielle(n-1)

print(factorielle(7))



def fact(n):
    if n!=0:
        return n*fact(n-1)
    return 1

print(fact(7))