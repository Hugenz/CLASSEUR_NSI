""" SUJET : Implémenter une structure de file à l’aide de deux piles."""

# pour enfiler on empile l'element sur la premiere pile
# pour defiler on depile la deuxieme pile si elle n'est pas vide
# sinon on depile la premiere pile et on empile les elements sur la deuxieme pile


def creer_pile_vide():
    return []

def creer_file_vide():
    return [creer_pile_vide(),creer_pile_vide()]

def est_vide(P):
    if P==[]:
        return True
    else:
        return False

def empiler(P,e):
    P.append(e)
    return None

def enfiler(F,e):
    return empiler(F[0],e)

def depiler(P):
    e=P.pop()
    return e

def defiler(F):
    if est_vide(F[1]):
        while not est_vide(F[0]):
            empiler(F[1], depiler (F[0]))
    return depiler(F[1])



F= creer_file_vide()
enfiler(F,1)
enfiler(F,2)
enfiler(F,3)
enfiler(F,4)
print(F)
defiler(F)
print(F)


