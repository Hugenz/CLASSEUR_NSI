""" SUJET : Implémenter une structure de file à l’aide de deux piles."""

# pour enfiler on empile l'element sur la premiere pile
# pour defiler on depile la deuxieme pile si elle n'est pas vide
# sinon on depile la premiere pile et on empile les elements sur la deuxieme pile


# liste des fonctions utiles

def creer_pile_vide():
    return []

def est_vide(P):
    if P==[]:
        return True
    else:
        return False

def empiler(P,e):
    P.append(e)
    return None

def depiler(P):
    e=P.pop()
    return e

def main(p1,p2):

    for i in range(len(p1)):
        empiler(p1,i)
    while not est_vide(p2):
        for i in range(len(p2)):
            empiler(p1,depiler(p2))
    else:
        for i in range(len(p1)):
            empiler(p2,depiler(p1))
    return p1,p2


print (main([1,2,3,4,5],[6,7,8,9,10]))



