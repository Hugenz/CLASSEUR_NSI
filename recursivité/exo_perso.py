def fact_iter(n):
    if n == 0:
        return 1
    x = 1
    for i in range(1, n+1):
        x = x * i
    return x


print(fact_iter(5))


def fact_rec(n):
    if n <= 1:
        return 1
    return n*fact_iter(n-1)


print(fact_rec(7))


def fact_rec2(n):
    if n <= 0:
        return 1
    return n*fact_rec2(n-1)


print (fact_rec2(5))


def fact_iter2(n):
    if n == 0:
        return 1
    x = 1
    for i in range(1,n+1):
        x = x*i
    return x


print(fact_iter2(5))


def rebour(n):
    for i in range (n+1):
        print (n-i)


print(rebour(5))


def palindrome(ch):
    if len(ch) == 0 or len(ch) == 1:
        return True
    if ch[0] == ch[-1]:
        return palindrome(ch[1:-1])
    return False


print(palindrome("azertyuioiuytreza"))


def compteur(ch, car):
    if ch == "":
        return 0
    if ch[0] == car:
        return 1 + compteur(ch[1:], car)
    return compteur(ch[1:], car)


print(compteur("azertaayuiop", "a"))




