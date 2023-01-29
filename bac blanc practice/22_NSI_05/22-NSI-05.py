#Exercice 1:

def rechercheminmax2(tab):
    """Renvoie la plus petite et la plus grande valeur du tableau sous la forme d’un dictionnaire à deux clés ‘min’ et ‘max’."""
    dico = {}
    dico['min'] = tab[0]
    dico['max'] = tab[0]
    for i in tab:
        if i < dico['min']:
            dico['min'] = i
        if i > dico['max']:
            dico['max'] = i
    return dico

print(rechercheminmax2([1,2,3,4,5,6,7,8,9,10]))

#Exercice 2:

class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à
    13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10,
    Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur,
    carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle'][self.Couleur - 1]

class PaquetDeCarte :
    def __init__(self):
        self.contenu = []
        """Remplit le paquet de cartes"""

    def remplir(self):
        for i in range(1, 5): # 4 couleurs
            for j in range(1, 14): # 13 valeurs
                self.contenu.append(Carte(i, j)) # On ajoute la carte au paquet

    """Renvoie la Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        return self.contenu[pos] # On renvoie la carte à la position pos



unPaquet = PaquetDeCarte()
unPaquet.remplir()
uneCarte = unPaquet.getCarteAt(20)
print(uneCarte.getNom(), "de", uneCarte.getCouleur())

