import tkinter as tk
import random

class Carte:
    def __init__(self, hauteur, couleur):
        self.hauteur = hauteur
        self.couleur = couleur

    def __repr__(self):

        valeur = str(self.hauteur)
        famille = self.couleur

        if self.hauteur > 10:
            if self.hauteur == 11:
                valeur = "valet"
            if self.hauteur == 12:
                valeur = "dame"
            if self.hauteur == 13:
                valeur = "roi"
            if self.hauteur == 14:
                valeur = "as"

        if self.couleur == 'P':
            famille = "Pique"
        if self.couleur == 'T':
            famille = "Trèfle"
        if self.couleur == 'C':
            famille = "Coeur"
        if self.couleur == 'K':
            famille = "Carreau"

        return valeur + " de " + famille


    def image(self):
        fichier = "./Cartes/"+str(self.hauteur)+self.couleur+".gif"
        fenetre = tk.Tk()
        fenetre.geometry('135x192+1000+400')
        image_carte = tk.PhotoImage(file=fichier)
        label = tk.Label(fenetre,image= image_carte)
        label.pack()
        fenetre.mainloop()


carte=Carte(14,'T')
#print (carte.image())

"""Ajoutez une méthode est_vide à la classe PaquetDeCartes qui renvoie un booléen égal à True si
le paquet ne contient aucune carte et False sinon."""

class PaquetDeCarte:
    def __init__ (self, contenu):
        self.contenu = contenu

    def __repr__(self):
        return str(self.contenu)

    def est_vide(self):
        if self.contenu == []:
            return True
        else:
            return False

    def taille(self):
        return len(self.contenu)

    def battre(self):
        random.shuffle(self.contenu)
        return self.contenu

    def tirer_carte(self):
        return self.contenu.pop(0)

    def ajouter_carte(self, carte):
        self.contenu.append(carte)
        return self.contenu

    def ajouter_paquet(self, paquet):
        self.contenu.append(paquet)
        return self.contenu

    def distribuer(self, nb_joueurs):
        paquet_joueur = []
        for i in range(nb_joueurs):
            paquet_joueur.append(PaquetDeCarte([]))
        while len(self.contenu) > 0:
            for i in range(nb_joueurs):
                paquet_joueur[i].ajouter_carte(self.tirer_carte())
        return paquet_joueur



paquet = PaquetDeCarte([Carte(7,'C'),Carte(14,'P')])
print(paquet)
print(paquet.est_vide())
print(paquet.taille())
print(paquet.battre())
print(paquet.tirer_carte())
print(paquet.ajouter_carte(Carte(12,'T')))
print(paquet.ajouter_paquet(PaquetDeCarte([Carte(4,'K'),Carte(11,'P')])))
print(paquet.distribuer(3))

