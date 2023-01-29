Pieces = [100,50,20,10,5,2,1]

def rendu_glouton(arendre, solution=[], i=0):
    """
    Fonction récursive pour rendre la monnaie
    """
    if arendre == 0: # Si la somme à rendre est nulle, on renvoie la solution
        return solution # On renvoie la solution
    p = Pieces[i] # On prend la pièce de valeur p
    if p <= arendre: # Si la pièce est inférieure à la somme à rendre
        solution.append(p) # On ajoute la pièce à la solution
        return rendu_glouton(arendre-p, solution, i) # On appelle la fonction récursive
    else: # Sinon, on passe à la pièce suivante
        return rendu_glouton(arendre, solution, i+1) # on appelle la fonction recursive i+1 pour passer à la pièce suivante

print (rendu_glouton(173))


def recherche (car,mot):
    compteur = 0
    if car in mot:
        for i in mot:
            if i == car:
                compteur += 1
        return compteur
    else:
        return 0

print (recherche('i',"mississippi"))