# Fonction récursive
# qui calcule le nombre de façons d’obtenir la somme s avec n dés.

# Principe : les 10 façons d’obtenir 15 avec 3 dés à 6 faces (dé1, dé2 et dé3).
# On note que, dans cet exemple, chaque dé est supérieur à 2. En effet, il est impossible de d’obtenir
# une somme égale à 15 avec 3 dés dont la valeur d’un des dés est 2 : de_min = 3.

def nbr_de_facons(somme, nb_de, de_min):
    if somme == 0 or nb_de == 0:
        return 0
    if somme < nb_de * de_min:
        return 0
    return 1 + nbr_de_facons(somme - de_min, nb_de - 1, de_min)


print(nbr_de_facons(15, 3, 3))