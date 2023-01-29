# Exercice 1 :

def moyenne(tab):
    """renvoie la moyenne des valeurs de tab"""
    somme = 0
    for i in range(len(tab)):
        somme += tab[i]
    return somme / len(tab)


print (moyenne([5,3]))


# Exercice 2

coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], \
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0], \
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], \
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], \
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], \
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont repreente par 
        des "*" , les 0 par deux espaces "  " '''
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *",end="")
            else:
                print("  ",end="")
        print()


def zoomListe(liste_depart,k):
    '''renvoie une liste contenant k fois chaque element de liste_depart'''
    liste_zoom = [] # liste vide
    for elt in liste_depart: # pour chaque element de liste_depart
        for i in range(k): # on ajoute k fois l'element a la liste
            liste_zoom.append(elt) # on ajoute l'element a la liste
    return liste_zoom # on renvoie la liste

def zoomDessin(grille,k):
    '''renvoie une grille ou les lignes sont zoomees k fois ET repetees k fois'''
    grille_zoom=[] # liste vide
    for elt in grille: # pour chaque ligne de la grille
        liste_zoom = zoomListe(elt,k) # on zoome la ligne
        for i in range(k): # on ajoute k fois la ligne zoomee a la grille
            grille_zoom.append(liste_zoom) # on ajoute la ligne zoomee a la grille
    return grille_zoom # on renvoie la grille

print (zoomDessin(coeur,2))