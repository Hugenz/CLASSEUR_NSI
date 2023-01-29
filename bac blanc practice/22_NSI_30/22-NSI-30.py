def fusion(tab1 , tab2):
    """ renvoie tableau trié dans l'ordre croissanet contenant l'esemble des éléments de tab1 et tab2 """

    tab = []
    i = 0 # indice de parcours de tab1
    j = 0 # indice de parcours de tab2
    while i < len(tab1) and j < len(tab2): # tant qu'on n'a pas parcouru tout tab1 et tout tab2
        if tab1[i] < tab2[j]: # si l'élément courant de tab1 est plus petit que celui de tab2
            tab.append(tab1[i]) # on ajoute l'élément courant de tab1 à tab
            i += 1 # on passe à l'élément suivant de tab1
        else: # si l'élément courant de tab2 est plus petit que celui de tab1
            tab.append(tab2[j]) # on ajoute l'élément courant de tab2 à tab
            j += 1 # on passe à l'élément suivant de tab2
    if i < len(tab1): # si on a parcouru tout tab2 mais pas tout tab1
        tab.extend(tab1[i:]) # on ajoute à tab le reste de tab1
    else: # si on a parcouru tout tab1 mais pas tout tab2
        tab.extend(tab2[j:]) # on ajoute à tab le reste de tab2
    return tab # on renvoie le tableau trié

print(fusion([3,5],[2,5]))


def rom_to_dec(nombre):
    """ Renvoie l’écriture décimale du nombre donné en chiffres romains """

    dico = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    if len(nombre) == 1:
        return dico[nombre] # on renvoie la valeur associée à la clé nombre
    else:
        nombre_droite = nombre[1:] # on supprime le premier caractère de la chaîne contenue dans la variable nombre

        if dico[nombre[0]] >= dico[nombre[1]]: # si la valeur associée à la clé nombre[0] est plus grande ou égale à la valeur associée à la clé nombre[1]
            return dico[nombre[0]] + rom_to_dec(nombre_droite) # on renvoie la valeur associée à la clé nombre[0] plus la valeur associée à la clé nombre_droite
        else:
            return rom_to_dec(nombre_droite) - dico[nombre[0]] # on renvoie la valeur associée à la clé nombre_droite - la valeur associée à la clé nombre[0]


print (rom_to_dec("C"))
print (rom_to_dec("CXLII"))
print (rom_to_dec("MCMXCIX"))