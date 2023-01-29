#Exercice 1

def taille(arbre,lettre):
    if arbre[lettre][0]!="" and arbre[lettre][1]!="": # Si les deux fils ne sont pas vides
        return 1+taille(arbre,arbre[lettre][0])+taille(arbre,arbre[lettre][1]) # On retourne 1 + la taille du fils gauche + la taille du fils droit
    elif arbre[lettre][0]=="" and arbre[lettre][1]!="": # Si le fils gauche est vide et le fils droit n'est pas vide
        return 1+taille(arbre,arbre[lettre][1]) # On retourne 1 + la taille du fils droit
    elif arbre[lettre][0]!="" and arbre[lettre][1]=="": # Si le fils gauche n'est pas vide et le fils droit est vide
        return 1+taille(arbre,arbre[lettre][0]) # On retourne 1 + la taille du fils gauche
    else : # Si les deux fils sont vides
        return 1 # On retourne 1

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'],'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}

print(taille(a,'F'))


#Exercice 2

def tri_iteratif(tab):
    for k in range( len(tab)-1 , 0, -1): # On parcourt le tableau de la fin vers le début de 1 en 1
        imax = k # On initialise l'indice du maximum à la fin du tableau
        for i in range(0 , k ): # On parcourt le tableau de 0 à k-1
            if tab[i] > tab[imax] : # Si l'élément courant est plus grand que le maximum
                imax = i # On met à jour l'indice du maximum
        if tab[imax] > tab[k] : # Si le maximum est plus grand que l'élément courant
            tab[k] , tab[imax] = tab[imax] , tab[k] # On échange les deux éléments
    return tab


print(tri_iteratif([41, 55, 21, 18, 12, 6, 25]))