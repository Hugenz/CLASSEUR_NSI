tour1 = [10,9,8,7,6,5,4,3,2,1]
tour2 = []
tour3 = []


def result():
    print(tour1,tour2,tour3)

def deplace2elements(tour1,tour2,tour3):
    """
    deplacer 2 elements de tour1 vers tour2 en passant par tour3
    """
    result()
    tour3.append(tour1.pop())
    result()
    tour2.append(tour1.pop())
    result()
    tour2.append(tour3.pop())
    result()


def deplace3elements(tour1,tour2,tour3):
    """
    deplacer 3 elements de tour1 vers tour2 en passant par tour3
    """
    deplace2elements(tour1,tour3,tour2)
    tour2.append(tour1.pop())
    deplace2elements(tour3,tour2,tour1)


def deplace4elements(tour1,tour2,tour3):
    """
    deplacer 4 elements de tour1 vers tour2 en passant par tour3
    """
    deplace3elements(tour1,tour3,tour2)
    tour2.append(tour1.pop())
    deplace3elements(tour3,tour2,tour1)


def deplace_n_elements(n,tour1,tour2,tour3):

    if n > 0:
        deplace_n_elements(n-1,tour1,tour3,tour2)
        tour2.append(tour1.pop())
        deplace_n_elements(n-1,tour3,tour2,tour1)
        result()


deplace_n_elements(10,tour1,tour2,tour3)

print("resultat :",tour1,tour2,tour3)