def verifie(tab):
    """renvoie True si le tableau est trié, False sinon"""
    for i in range(len(tab) - 1):
        if tab[i] > tab[i+1]:
            return False
    return True


print (verifie([1,2,3,4,5,6,7,8,9,10]))



Urne = ['Oreilles sales', 'Oreilles sales', 'Oreilles sales', 'Extra Vomit',
'Lady Baba', 'Extra Vomit', 'Lady Baba', 'Extra Vomit', 'Lady Baba', 'ExtraVomit']

def depouille(urne):
    """renvoie le résultat dans un dictionnaire dont les clés sont les noms des artistes et les valeurs le nombre de votes en leur faveur."""
    resultat = {} # dictionnaire vide
    for bulletin in urne: # pour chaque bulletin
        if bulletin in resultat: # si le bulletin est deja dans le dictionnaire
            resultat[bulletin] = resultat[bulletin] + 1 # on incremente le nombre de voix
        else:
            resultat[bulletin] = 1 #sinon on ajoute le bulletin au dictionnaire
    return resultat # on renvoie le dictionnaire

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election: # pour chaque candidat
        if election[candidat] > nmax : # si le nombre de voix est plus grand que le nombre de voix du vainqueur actuel
            nmax = election[candidat] # on met a jour le nombre de voix du vainqueur actuel
            vainqueur = candidat # on met a jour le vainqueur actuel
    liste_finale = [nom for nom in election if election[nom] == nmax] # on cree une liste des candidats ayant le meme nombre de voix que le vainqueur
    return liste_finale # on renvoie la liste des candidats ayant le meme nombre de voix que le vainqueur


print (depouille(Urne))
print (vainqueur(depouille(Urne)))