###############################################################################
# Question numero 5 de l'examen de type bac de recursivite
###############################################################################

# consigne : Question 5
# On veut créer la fonction récursive somme_max ayant pour paramètres un tableau T, un entier i et un
# entier j. Cette fonction renvoie la somme maximale pour tous les chemins possibles allant de la case (0,0)
# à la case (i,j).
# 1. Ecrire en Python la fonction récursive somme_max.
# 2. Ecrire le programme qui appelle la fonction somme_max pour résoudre le problème initial.


def somme_max(T,i,j):
    """
    retourne la somme maximale des elements de T
    en partant de T[0][0] et en se deplacant
    vers la droite ou vers le bas
    """
    if (i,j) == (0,0):
        return T[i][j]
    elif i==0:
        return T[i][j]+somme_max(T,0,j-1)
    elif j==0:
        return T[i][j]+somme_max(T,i-1,0)
    else:
        return T[i][j]+max(somme_max(T,i-1,j),somme_max(T,i,j-1))


tableau=[[4,1,1,3],[2,0,2,1],[3,1,5,1]]
print(somme_max(tableau,2,3))


