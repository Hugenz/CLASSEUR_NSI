#Exercice 1 :

dico = {'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}

def max_dico(dico):
    max_value, max_key = 0, ""
    for key, value in dico.items():
        if value > max_value:
            max_value, max_key = value, key
    return max_value, max_key

print(max_dico(dico))

#Exercice 2 :

class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie le booléen True si la pile est vide, False sinon."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l’élément placé au sommet de la pile,
        si la pile n’est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    """Renvoie le résultat de l'expression contenue dans le tableau tab"""
    p = Pile() # On crée une pile
    for element in tab: # On parcourt le tableau
        if element != '+' and element != '*': # Si l'élément n'est pas un opérateur
            p.empiler(element) # On empile l'élément
        else:
            if element == '+': # Si l'élément est un +
                resultat = p.depiler() + p.depiler() # On dépile les deux derniers éléments et on les additionne
            else: # Si l'élément est un *
                resultat = p.depiler() * p.depiler() # On dépile les deux derniers éléments et on les multiplie
            p.empiler(resultat) # On empile le résultat
    return p.depiler() # On renvoie le résultat


print(eval_expression([2, 3, '+', 5, '*']))

