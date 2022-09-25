# Exercice : écrire une fonction python fusion(L1,L2) qui prend en argument deux listes triées L1 et L2
# et qui retourne une liste triée L3 qui est la fusion de L1 et L2

# Par exemple :
# liste1 = [1, 5, 7]
# liste2 = [1, 4, 6]
# liste3 = fusion(liste1, lite2)
# liste3 = [1, 1, 4, 5, 6, 7]

# Proposer une version récursive et une version itérative


def fusion(t1,t2):
    if t1 == []:
        return t2
    elif t2 == []:
        return t1
    elif t1[0] < t2[0]:
        return [t1[0]] + fusion(t1[1:],t2)
    else:
        return [t2[0]] + fusion(t1,t2[1:])


def fusion_it(t1,t2):
    i1, i2, n1, n2 = 0, 0, len(t1), len(t2)
    t=[]
    while i1 < n1 and i2 < n2:
        if t1[i1] < t2[i2]:
            t.append(t1[i1])
            i1 += 1
        else:
            t.append(t2[i2])
            i2 += 1
    if i1 == n1:
        t.extend(t2[i2:])
    else:
        t.extend(t1[i1:])
    return t


L1 = [1,3,5]
L2 = [2,4]
L3 = fusion(L1,L2)
L4 = fusion_it(L1,L2)
#print("*** L3 *** :",L3)
#print("*** L4 *** :",L4)

