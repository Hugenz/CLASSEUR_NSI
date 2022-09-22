# Exercice : écrire une fonction python fusion(L1,L2) qui prend en argument deux listes triées L1 et L2
# et qui retourne une liste triée L3 qui est la fusion de L1 et L2

# Par exemple :
# liste1 = [1, 5, 7]
# liste2 = [1, 4, 6]
# liste3 = fusion(liste1, lite2)
# liste3 = [1, 1, 4, 5, 6, 7]

# Proposer une version récursive et une version itérative.


""" Version récursive """


def fusion_recur(L1, L2):
    L3 = []
    if len(L1) == 0:                               # Si L1 est vide
        return L2                                  # On retourne L2
    if len(L2) == 0:                               # Si L2 est vide
        return L1                                  # On retourne L1
    if L1[0] < L2[0]:                              # Si le premier élément de L1 est plus petit que le premier élément de L2
        L3.append(L1[0])                           # On ajoute le premier élément de L1 à L3
        L3.extend(fusion_recur(L1[1:], L2))        # On ajoute le résultat de la fusion de L1[1:] et L2 à L3
    else:                                          # Sinon
        L3.append(L2[0])                           # On ajoute le premier élément de L2 à L3
        L3.extend(fusion_recur(L1, L2[1:]))        # On ajoute le résultat de la fusion de L1 et L2[1:] à L3
    return L3                                      # On retourne L3


print (fusion_recur([1, 5, 7], [1, 4, 6]))


""" Version itérative """


def fusion_iter(L1, L2):
    L3 = []
    while len(L1) > 0 and len(L2) > 0:      # Tant que les deux listes ne sont pas vide
        if L1[0] < L2[0]:                   # Si le premier élément de L1 est plus petit que le premier élément de L2
            L3.append(L1[0])                # On ajoute le premier élément de L1 à L3
            L1 = L1[1:]                     # On supprime le premier élément de L1
        else:                               # Sinon
            L3.append(L2[0])                # On ajoute le premier élément de L2 à L3
            L2 = L2[1:]                     # On supprime le premier élément de L2
    if len(L1) == 0:                        # Si L1 est vide
        L3.extend(L2)                       # On ajoute L2 à L3
    else:                                   # Sinon
        L3.extend(L1)                       # Sinon on ajoute L1 à L3
    return L3


print (fusion_iter([1, 5, 7], [1, 4, 6]))

