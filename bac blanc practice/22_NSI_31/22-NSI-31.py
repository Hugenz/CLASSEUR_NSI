def recherche(nb,tab):
    """renvoie le nombre d'occurences de nb dans tab"""
    nb_occurences = 0
    for i in range(len(tab)):
        if tab[i] == nb:
            nb_occurences += 1
    return nb_occurences

print (recherche(2,[1,5,4,2,3,2,8,2]))


def rendu_monnaie_centimes(s_due, s_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = []
    a_rendre = s_versee - s_due
    i = len(pieces) - 1
    while a_rendre > 0 :
        if pieces[i] <= a_rendre : # si la piece est plus petite que le reste a rendre
            rendu.append(pieces[i]) # on ajoute la piece au rendu
            a_rendre = a_rendre - pieces[i] # on retire la piece du reste a rendre
        else :
            i = i - 1  # on passe a la piece suivante
    return rendu

