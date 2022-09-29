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

def hauteur_pile(P):
    Q=creer_pile_vide()
    n=0
    while not(est_vide(P)):
        n+=1
        x=depiler(P)
        empiler(Q,x)
    while not(est_vide(Q)):
        x=depiler(Q)
        empiler(P,x)
    return n

def max_pile(P,n):
    Q=creer_pile_vide()
    max=0
    for i in range(n):
        x=depiler(P)
        if x>max:
            max=x
            indice=i+1
        empiler(Q,x)
    while not(est_vide(Q)):
        empiler(P,depiler(Q))
    return indice

def retourner(P,n):
    Q1=creer_pile_vide()
    Q2=creer_pile_vide()
    for i in range(n):
        empiler(Q1,depiler(P))
    while not(est_vide(Q1)):
        empiler(Q2,depiler(Q1))
    while not(est_vide(Q2)):
        empiler(P,depiler(Q2))
    return None

def tri_pile(P):
    h=hauteur_pile(P)
    while h!=1:
        max=max_pile(P,h)
        retourner(P,max)
        retourner(P,h)
        h+=-1
    return None

pile1 = creer_pile_vide()

empiler (pile1,5)
empiler (pile1,6)
empiler (pile1,9)
empiler (pile1,7)
empiler (pile1,10)
empiler (pile1,8)
print(pile1)
tri_pile(pile1)
print(pile1)

