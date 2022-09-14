##############################################################################################
                                        # EXERCICE 1
##############################################################################################
# On souhaite écrire une fonction qui effectue un compte à rebour, par exemple afficher 5, 4, 3, 2, 1 , 0.
# Cette fonction rebours prend en argument un entier naturel 𝑛 et affiche les nombres de 𝑛 à 0.

"""
1) Ecrire une fonction itérative rebours1 qui utilise une boucle while
"""

def rebours1(n):
    while n >= 0:
        print(n)
        n = n-1

"""
2) Ecrire une fonction itérative rebours2 qui utilise une boucle for
"""

def rebours2(n):
    for i in range(n+1):
        print(n-i)

"""
3) Ecrire une fonction récursive rebours3
"""

def rebours3(n):
    """
    <=> rebours3(5) = 5
    <=> rebours3(4) = 4
    <=> rebours3(3) = 3
    <=> rebours3(2) = 2
    <=> rebours3(1) = 1
    <=> rebours3(0) = 0
    ....

    param n: entier naturel
    type n: int
    return: affiche les nombres de n à 0
    """
    print(n)
    if n == 0:
        return None
    return rebours3(n-1)


"""
# appel des fonctions
"""
print("ex 1/ 1)", rebours1(5))
print("ex 1/ 2)", rebours2(5))
print("ex 1/ 3)", rebours3(5))


##############################################################################################
                                        # EXERCICE 2
##############################################################################################

# La valeur du pgcd (plus grand commun diviseur) de deux entiers naturels 𝑎 et 𝑏 est calculable à l’aide de
# l’algorithme d’Euclide : 𝑝𝑔𝑐𝑑(𝑎, 𝑏) = 𝑝𝑔𝑐𝑑(𝑏, 𝑟) ou 𝑟 est le reste dans la division euclidienne de 𝑎 par 𝑏.

# En voici une version itérative :

#   def pgcd(a,b) :
#       if b == 0:
#           return a
#       while b != 0:
#           a, b = b, a%b
#       return a

"""
Ecrire une version récursive de cette fonction.
"""

def pgcd(a,b):
    """
    Renvoie le plus grand commun diviseur de a et b

    param a: entier
    param b: entier
    type a: int
    type b: int
    return: pgcd de a et b
    """
    if b==0:
        return a
    return pgcd(b,a%b)


"""
# appel des fonctions
"""
print("ex2", pgcd(30,35))


##############################################################################################
                                        # EXERCICE 3
##############################################################################################

# Ecrire une fonction récursive inverse qui prend en paramètre une chaîne de caractères ch et retourne
# la chaîne obtenue en inversant l’ordre des caractères.

"""
Par exemple, inverse("pizza") a pour valeur la "azzip"
"""


def inverse_inter(ch):
    if ch == '':
        return ''
    x = ch[0]
    for i in range(1,len(ch)):
        x = ch[i] + x
    return x


"""
ch = bonjour
x = b

=> x = o + b
=> x = n + ob
=> x = j + nob
=> x = o + jnob
=> x = u + ojnob
=> x = r + uojnob
return x (qui vaut ruojnob)
"""


def inverse_recur(ch):
    """
    <=> inverse_recur("bonjour") = "ruojnob"
    <=> inverse_recur("onjour") = "uojnob"
    <=> inverse_recur("njour") = "ojnob"
    <=> inverse_recur("jour") = "jnob"
    <=> inverse_recur("our") = "nob"
    <=> inverse_recur("ur") = "ob"
    <=> inverse_recur("r") = "b"
    <=> inverse_recur("") = ""

    param ch: chaine de caractères
    type ch: str
    return: chaine de caractères inversée

    """
    if ch == '':
        return ''
    return ch[-1] + inverse_recur(ch[:-1])


def reverse(chaine):
    if chaine == '':
        return ''
    else:
        return chaine[-1] + reverse(chaine[:-1])


"""
# appel des fonctions
"""
print (inverse_inter("bonjour"))
print ("ex 3", inverse_recur("pizza"))
print (reverse("chaine"))


##############################################################################################
                                        # EXERCICE 4
##############################################################################################

"""
Comparer les fonctions fact et fact2 ci-dessous :
"""
#   def fact(n):
#       if n==0:
#           return 1
#       else:
#           return n*fact(n-1)

#   def fact2(n):
#       if n>0:
#           return n*fact(n-1)
#       else:
#           return 1


print ("ex 4 : Les deux fontions n'ont pas le meme critère d'arrêt, la première fonction s'arrete quand n = 0""\n" "La seconde fonction s'arrete quand n = 1 (n>0) donc elle effectue une itération de plus que la première fonction")

##############################################################################################
                                        # EXERCICE 5
##############################################################################################

# On dispose d’une fonction nettoie qui prend en paramètre une liste triée et élimine les éléments iden-
# tiques. Par exemple, si la liste est liste=[1,1,2,6,6,6,8,8,9,10], après l’instruction
# nettoie(liste), cette liste a pour valeur [1,2,6,8,9,10]

#   def nettoie(L):
#       n = len(L)
#       k = 0
#       while k < n-1:
#           if L[k] != L[k+1]:
#               k = k + 1
#           else:
#               del L[k]
#               n = len(L)

"""
Ecrire une version récursive de cette fonction.
"""


def nettoie(L):
    if len(L) == 1:
        return L
    if L[0] == L[1]:
        return nettoie(L[1:])
    else:
        return [L[0]] + nettoie(L[1:])


def nettoie_recur(L,k):
    """
    k est l'indice du premier élément à tester

    paramètres : L : liste triée
                k : indice du premier élément à tester
    résultat : liste triée sans doublons
    """
    if k < len(L)-1:
        if L[k] != L[k +1]:
            nettoie_recur(L,k+1)
        else:
            del L[k]
            nettoie_recur(L,k)

Liste = [1,1,2,6,6,6,8,8,9,10]
nettoie_recur(Liste,0)

"""
# appel des fonctions
"""
print ("ex 5 correction prof",Liste)
print ("ex 5:", nettoie([1,1,2,6,6,6,8,8,9,10]))


##############################################################################################
                                        # EXERCICE 1 (page 2)
##############################################################################################

"""Soit une chaine de caractères, écrire un algorithme récursif permettant de déterminer sa
longueur."""

def longueur(ch):
    """
    Renvoie la longueur de la chaine ch

    param ch: chaine de caractères
    type ch: str
    return: longueur de la chaine ch
    """
    if ch == '':
        return 0
    return 1 + longueur(ch[1:])

print ("ex 1 page 2 :", longueur("bonjour"))


##############################################################################################
                                        # EXERCICE 2 (page 2)
##############################################################################################


# Rendre récursive la fonction somme suivante :

#   def somme(L):
#       s = 0
#       for val in L:
#           s = s + val
#       return s

def somme(L):
    """
    Renvoie la somme des éléments de la liste L

    param L: liste d'entiers
    type L: list
    return: somme des éléments de la liste L
    """
    if len(L) == 0:
        return 0
    return L[0] + somme(L[1:])

print ("ex 2 page 2 :", somme([1,2,3,4,5]))


##############################################################################################
                                        # EXERCICE 3 (page 2)
##############################################################################################

# Soit la suite définie par :

    # 𝑈0 = 𝑈1 = 1
    # 𝑈𝑛 = 3𝑈𝑛−1 + 𝑈𝑛−2

"""
Ecrire un programme récursif permettant de calculer le nième terme de la suite
"""


def suite(n):
    """
    <=> u2 = 3x(u1)+(u0)
    <=> u2 = 3x1+1
    <=> u2 = 4
    <=> u3 = 3x(u2)+(u1)
    <=> u3 = 3x4+1
    <=> u3 = 13
    ....
    """
    if n == 0 or n == 1:
        return 1
    return 3*suite(n-1) + suite(n-2)


"""
# appel des fonctions
"""
print("ex 3 page 2 :", suite(5))


##############################################################################################
                                        # EXERCICE 4 (page 2)
##############################################################################################

"""
Un nombre N est pair si (N−1) est impair, et un nombre N est impair si (N−1) est pair.
Ecrire deux fonctions récursives mutuelles pair(N) et impair(N) permettant de savoir si un
nombre N est pair et si un nombre N est impair
"""


def pair(n):
    if n == 0:
        return True
    return impair(n-1)


def impair(n):
    if n == 0:
        return False
    return pair(n-1)


def pair_recur(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return not impair_recur(n - 1)


def impair_recur(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return not pair_recur(n - 1)


# print ("ex elouann :",pair_recur(5))
# print ("ex elouann :",impair_recur(5))


"""
# appel des fonctions
"""
print("ex 4 page 2 :")
print(pair(4))
print(impair(4))


##############################################################################################
                                        # EXERCICE 1 (page 3)
##############################################################################################


# Une association a remarqué que d’une année à l’autre,
# • Elle perd 5% de ses adhérents ;
# • Elle gagne 200 adhérents.

"""
1) En admettant que le nombre d’adhérents de cette association était égal à 2000 au 1er janvier 2019,
écrire en Python une fonction récursive nommée nombre(n) affichant le nombre théorique d’ad-
hérents après 𝑛 années, 𝑛 ≥ 1.

2) Dans ce même programme, afficher le nombre théorique d’adhérents au cours des 20 prochaines
années.

"""

def nombre(n):
    if n == 1:
        return 2000
    return nombre(n-1) - nombre(n-1)*0.05 + 200

print ("ex 1 page 3 :", nombre(20))


##############################################################################################
                                        # EXERCICE 2 (page 3)
##############################################################################################

"""
Ecrire une fonction récursive compteur(chaine,caractere) retournant le nombre de fois que l’on
peut compter le caractère dans la chaîne.
Remarque : la méthode count permet d’obtenir le même résultat.
"""

def compteur(ch,car):
    if ch == '':
        return 0
    if ch[0] == car:
        return 1 + compteur(ch[1:],car)
    return compteur(ch[1:],car)

print ("ex 2 page 3 :", compteur("bonjour","o"))

##############################################################################################
                                        # EXERCICE 3 (page 3)
##############################################################################################

# On considère le programme suivant :

#       def f(a,b) :
#           if b == 1:
#               return a
#           return a + f(a,b-1)
# print(f(3,10))

"""
1) Quel résultat retourne f(7,9) ? (exécuter le programme à la main)
2) En déduire la signification de la valeur retournée par cette fonction pour deux entiers naturels non
nuls 𝑎 et 𝑏 quelconques.
3) Qu’est ce qui garantit que le programme s’arrête ?
"""

"""
1) 63
2) a + a + a + a + a + a + a + a + a
3) b == 1
"""

##############################################################################################
                                        # EXERCICE 4 (page 3)
##############################################################################################

# Diagonale de Cantor

"""
Dans un repère, les points à coordonnées entières sont numérotés
selon le principe suivant ci-contra.
Ecrire une fonction récursive numero(x,y) qui retourne le numéro
du point de coordonnées (𝑥 ; 𝑦).
Par exemple, numero(3,2) doit retourner le nombre 17
"""


def numero(x,y):
    if x == 0 and y == 0:
        return 0
    if x == 0:
        return numero(x,y-1) + 2**y
    return numero(x-1,y) + 2**x

print ("ex 4 page 3 :", numero(3,2))

