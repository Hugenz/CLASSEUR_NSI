""" création de la classe noeud """
class Noeud:
    def __init__(self,key):
        self.gauche = None
        self.droit = None
        self.val = key


""" hauteur d'un arbre """
def Hauteur(noeud):
    if noeud is None:
        return 0
    else:
        lheight = Hauteur(noeud.gauche)
        rheight = Hauteur(noeud.droit)
        return 1+max(lheight, rheight)

""" taille d'un arbre """
def Taille(noeud):
    if noeud is None:
        return 0
    else:
        ltaille = Taille(noeud.gauche)
        rtaille = Taille(noeud.droit)
        return 1+ltaille+rtaille

""" insérer un noeud dans un arbre binaire de recherche """
def ArbreInserer(noeud, k):
    if noeud is None:
        noeud = Noeud(k)
    else:
        if noeud.val < k:
            if noeud.droit is None:
                noeud.droit = Noeud(k)
            else:
                ArbreInserer(noeud.droit, k)
        else:
            if noeud.gauche is None:
                noeud.gauche = Noeud(k)
            else:
                ArbreInserer(noeud.gauche, k)

def infixe(Noeud):
    """
    parcours de l'arbre en infixe
    """
    if Noeud == None: # si le noeud est vide
        return # on sort de la fonction
    if Noeud.gauche != None: # si le noeud gauche n'est pas vide
        infixe(Noeud.gauche) # on affiche le noeud gauche
    print(Noeud.val) # on affiche la valeur du noeud
    if Noeud.droit != None: # si le noeud droit n'est pas vide
        infixe(Noeud.droit) # on affiche le noeud droit

def prefixe(Noeud):
    """
    parcours de l'arbre en préfixe
    """
    if Noeud == None: # si le noeud est vide
        return # on sort de la fonction
    print(Noeud.val) # on affiche la valeur du noeud
    if Noeud.gauche != None: # si le noeud gauche n'est pas vide
        prefixe(Noeud.gauche) # on affiche le noeud gauche
    if Noeud.droit != None: # si le noeud droit n'est pas vide
        prefixe(Noeud.droit) # on affiche le noeud droit

def suffixe(Noeud):
    """
    parcours de l'arbre en suffixe
    """
    if Noeud == None: # si le noeud est vide
        return # on sort de la fonction
    if Noeud.gauche != None: # si le noeud gauche n'est pas vide
        suffixe(Noeud.gauche)  # on affiche le noeud gauche
    if Noeud.droit != None: # si le noeud droit n'est pas vide
        suffixe(Noeud.droit) # on affiche le noeud droit
    print(Noeud.val) # on affiche la valeur du noeud

def afficher_niveau(Noeud, niveau):
    """
    affiche les noeuds du niveau passé en argument
    """
    if Noeud == None: # si le noeud est vide
        return # on sort de la fonction
    if niveau == 1: # si le niveau est égal à 1
        print(Noeud.val) # on affiche la valeur du noeud
    elif niveau > 1: # si le niveau est supérieur à 1
        afficher_niveau(Noeud.gauche, niveau-1) # on affiche le niveau du noeud gauche
        afficher_niveau(Noeud.droit, niveau-1) # on affiche le niveau du noeud droit

def largeur(Noeud):
    """
    parcours de l'arbre en largeur
    """
    h = Hauteur(Noeud)
    for i in range(1, h+1): # i = 1, 2, 3, 4, 5 car h = 5
        afficher_niveau(Noeud, i) # affiche les noeuds du niveau i

def arbre_recherche(Noeud, valeur):
    """
    retourne vrai si la valeur passée en argument est dans l'arbre.
    """
    if Noeud == None: # si le noeud est vide
        return False # on retourne faux
    if Noeud.val == valeur: # si la valeur du noeud est égale à la valeur passée en argument
        return True # on retourne vrai
    return arbre_recherche(Noeud.gauche, valeur) or arbre_recherche(Noeud.droit, valeur) # on retourne vrai si la valeur est dans le noeud gauche ou dans le noeud droit


""" Création d'un arbre binaire de recherche """
racine = Noeud(10)
ArbreInserer(racine,3)
ArbreInserer(racine,1)
ArbreInserer(racine,5)
ArbreInserer(racine,79)
ArbreInserer(racine,78)
ArbreInserer(racine,80)

print("---------parcour infixe-----------")
infixe(racine)
print("---------parcour prefixe-----------")
prefixe(racine)
print("---------parcour suffixe-----------")
suffixe(racine)
print("---------parcour en largeur-----------")
largeur(racine)
print("---------noeud par niveau-----------")
afficher_niveau(racine, 3)
print("---------recherche de nombre-----------")
print(arbre_recherche(racine, 78))



print("\nHauteur de l'arbre :",Hauteur(racine))

print("\nTaille de l'arbre :",Taille(racine))