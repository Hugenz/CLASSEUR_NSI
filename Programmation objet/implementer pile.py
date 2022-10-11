class Element:

    def __init__(self, x):
        self.val = x
        self.suivant = None

    def __str__(self):
        return str(self.val) + " | " + str(self.suivant)


class Pile:

    def __init__(self):
        self.dernier = None

    def ajoute(self, x):
        e = Element(x)
        e.suivant = self.dernier
        self.dernier = e

    def pile_vide(self):
        return self.dernier is None

    def supprime(self):
        if not self.pile_vide():
            e = self.dernier
            self.dernier = e.suivant
            return e.val

    def __str__(self):
        return str(self.dernier)

    # ----------- TEST

p = Pile()
p.ajoute(31)
p.ajoute(15)
p.ajoute(27)
print(p)
p.pile_vide()
p.supprime()
print(p)