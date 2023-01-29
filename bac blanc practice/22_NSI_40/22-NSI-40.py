def recherche (nb, tab):
    """renvoie le tableau des indices de nb dans tab si nb est dans tab, [] sinon"""
    indices = []
    for i in range(len(tab)):
        if tab[i] == nb:
            indices.append(i)
    return indices

print (recherche(2,[1,5,4,2,3,2,8,2]))


#Exercice 2

resultats = {'Dupont':{'DS1' : [15.5, 4],
                       'DM1' : [14.5, 1],
                       'DS2' : [13, 4],
                       'PROJET1' : [16, 3],
                       'DS3' : [14, 4]},
             'Durand':{'DS1' : [6 , 4],
                       'DM1' : [14.5, 1],
                       'DS2' : [8, 4],
                       'PROJET1' : [9, 3],
                       'IE1' : [7, 2],
                       'DS3' : [8, 4],
                       'DS4' :[15, 4]}}


def moyenne(nom):
    """renvoie la moyenne de l'élève nom arrondie au dixième"""
    if nom in resultats: # si l'élève est dans le dictionnaire
        notes = resultats[nom] # on recupere les notes de l'élève
        total_points = 0 # on initialise le total des points a 0
        total_coefficients = 0 # on initialise le total des coefficients a 0
        for valeurs in notes.values(): # pour chaque note
            note , coefficient = valeurs # on recupere la note et le coefficient
            total_points = total_points + note * coefficient # on ajoute la note multipliee par le coefficient au total des points
            total_coefficients = total_coefficients + coefficient # on ajoute le coefficient au total des coefficients
        return round( total_points / total_coefficients , 1 )  # on renvoie la moyenne arrondie au dixieme
    else:
        return -1 # si l'élève n'est pas dans le dictionnaire, on renvoie -1
