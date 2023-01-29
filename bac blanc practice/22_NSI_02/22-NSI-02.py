
def pascal(n):
    C= [[1]] # On initialise la liste avec la première ligne
    for k in range(1,n+1): # On parcourt les lignes
        Ck = [1] # On initialise la ligne k avec le premier 1
        for i in range(1,k): # On parcourt les éléments de la ligne k
            Ck.append(C[k-1][i-1]+C[k-1][i]) # On ajoute l'élément de la ligne précédente
        Ck.append(1) # On ajoute le dernier 1
        C.append(Ck) # On ajoute la ligne à la liste
    return C

print (pascal(5))



def moyenne (liste):
    """renvoie la moyenne des valeurs de liste"""
    note = 0
    coeff = 0
    for i in liste:
        note = note + i[0]*i[1] # on multiplie la note par le coefficient
        coeff = coeff + i[1] # on ajoute le coefficient
    return note/coeff # On renvoie la moyenne

print (moyenne([(15,2),(9,1),(12,3)] ))


