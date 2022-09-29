#----------------exercice 1

def somme(n):
    if n == 1:
        return 1
    return somme(n-1) + n

assert somme(10) == 55


#----------------exercice 2

def carre(n):
    if n < 0 :
        n = -n
    if n == 0:
        return 0
    return(carre(n-1)+2*n-1)

assert carre(10) == 100
assert carre(-10) == 100


#----------------exercice 3

def fib_rec(n):
    if n==0 or n==1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

def fib_it(n):
    if n==0 or n==1:
        return 1
    else:
        a,b = 1,1
        for i in range(2,n):
            a,b = b,a+b
        return a+b


assert fib_rec(2) == 2
assert fib_rec(3) == 3
assert fib_rec(4) == 5
assert fib_rec(5) == 8
assert fib_it(5) == 8


#----------------exercice 4

def testtri(T):
    if len(T) < 2:
        return True
    if T[0] > T[1]:
        return False
    return testtri(T[1:])

tableau1 = [1, 2, 3, 4, 4, 5, 7, 8]
tableau2 = [1, 2, 3, 4, 4, 5, 8, 7]
assert testtri(tableau1) == True
assert testtri(tableau2) == False


