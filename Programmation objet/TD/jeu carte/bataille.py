"""
III. Création d’un jeu de Bataille

La bataille est un jeu de cartes qui se joue habituellement à deux. Le jeu commence en distribuant aux
joueurs, de manière équitable, l’intégralité du paquet de 52 cartes. Les joueurs disposent devant eux, face
cachée, leurs paquets de cartes. À chaque tour, chaque joueur retourne la première carte de son paquet.
Celui qui a la carte de plus grande hauteur remporte le pli : il prend les cartes posées et les range face cachée
sous son paquet.
En cas d’égalité de hauteurs, on dit qu’il y a bataille : les joueurs commencent par placer une première
carte face cachée puis une seconde carte face visible. En cas de nouvelle égalité, la procédure est répétée. À
la fin, le joueur gagnant remporte toutes les cartes posées, qu’il place sous son paquet.
Lorsqu’un joueur a en sa possession toutes les cartes du jeu, la partie se termine et il est déclaré gagnant
(elle peut aussi se terminer au bout d’un certain nombre de tours lorsque les deux joueurs en ont marre !
On désigne alors gagnant le joueur qui a le plus de cartes dans son paquet).

Mini-projet : Créer une simulation du jeu de la Bataille entre deux joueurs A et B en utilisant les classes
Carte et PaquetDeCartes codées précédemment.

Conseil : au départ, pour simplifier la conception de votre jeu, commencez par exclure les cas de bataille
en modifiant temporairement la règle de la Bataille : en cas d’égalité de hauteur des deux cartes tirées, le
joueur A remporte le pli. Une fois que votre jeu simplifié est opérationnel, penchez-vous sur le traitement
des cas de Bataille.
"""

class Bataille:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2

    def __repr__(self):
        return "Bataille entre " + str(self.joueur1) + " et " + str(self.joueur2)

    def jouer(self):
        self.joueur1.battre()
        self.joueur2.battre()
        self.joueur1.distribuer(2)
        self.joueur2.distribuer(2)
        while self.joueur1.taille() > 0 and self.joueur2.taille() > 0:
            carte1 = self.joueur1.tirer_carte()
            carte2 = self.joueur2.tirer_carte()
            if carte1.hauteur > carte2.hauteur:
                self.joueur1.ajouter_carte(carte1)
                self.joueur1.ajouter_carte(carte2)
            elif carte1.hauteur < carte2.hauteur:
                self.joueur2.ajouter_carte(carte1)
                self.joueur2.ajouter_carte(carte2)
            else:
                self.joueur1.ajouter_carte(carte1)
                self.joueur2.ajouter_carte(carte2)
        if self.joueur1.taille() > self.joueur2.taille():
            return self.joueur1
        else:
            return self.joueur2

