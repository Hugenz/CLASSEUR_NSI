###############################################################################
# Ecrire une fonction récursive qui calcule la somme des entiers de 1 à n
###############################################################################


def somme(n):
    if n == 1:  # Cas de base
        return 1
    else:
        return n + somme(n-1)


print(somme(5))


###############################################################################
# Ecrire une fonction recursive qui calcule le carré d'un entier n
###############################################################################


def carre(n):
    if n == 0:
        return 0
    else:
        return 2 * n - 1 + carre(n-1)


print(carre(5))


###############################################################################
# les nombre de Fibonacci sont definis de la facon suivante :
# F0 = F1 = 1
# Fn = Fn-1 + Fn-2 pour n >= 2
# Ecrire une fonction recursive qui calcule le n-ieme nombre de Fibonacci
# Eccire une fonction iterative qui calcule le n-ieme nombre de Fibonacci
###############################################################################


def fibo(n):
    if n == 0 or n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)


print (fibo(5))


def fibo2(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a


print (fibo2(5))


###############################################################################
# Ecrire une fonction recursive testtri(T) qui teste si un tableau T est trié ou non
###############################################################################


def testtri(T):
    if len(T) == 1:
        return True
    if T[0] <= T[1]:
        return testtri(T[1:])
    else:
        return False


print(testtri([1, 2, 3, 4, 5, 6, 7, 8, 9]))


###############################################################################