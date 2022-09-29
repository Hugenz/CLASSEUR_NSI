def lire_image_P3(fichier_source):
    """
    Fonction qui lit un fichier pixmap P3 fichier_source
    les pixels sont placés dans un tableau tab_source sous forme de triplet (r,v,b)
    Chaque ligne de l'image est représentée par une liste de pixel
    L'image est représentée par une liste de ligne
    La fonction renvoie le tableau
    """
    f=open(fichier_source,'r') #ouverture du fichier en lecture
    mode=f.readline() #lecture de la première ligne (le type d'image)
    if mode!='P3\n':
        print("Ce n'est pas un fichier P3")
        return(None)
    dim=f.readline() #lecture de la ligne des dimensions
    while dim[0]=='#': # les lignes du commentaire sont ignorees
            dim=f.readline()
    t_dim=dim.split() #transformation de la chaine de caractère en liste
    largeur=int(t_dim[0])
    hauteur=int(t_dim[1])
    val_max=f.readline() #lecture de la valeur max de codage
    tab_source=[]
    for i in range(hauteur):
        tab_source.append([])
        for j in range (largeur):
                R=f.readline() #lecture du pixel
                R=R.strip('\n') #suppression des caractère "\n"
                V=f.readline() #lecture du pixel
                V=V.strip('\n') #suppression des caractère "\n"
                B=f.readline() #lecture du pixel
                B=B.strip('\n') #suppression des caractère "\n"
                tab_source[i].append((int(R),int(V),int(B)))
    f.close() #fermeture du fichier
    return(tab_source)



def lire_image_P2(fichier_source):
    """
    Fonction qui lit un fichier pixmap P3 fichier_source
    les pixels sont placés dans un tableau tab_source sous forme d'un entier
    Chaque ligne de l'image est représentée par une liste de pixel
    L'image est représentée par une liste de ligne
    La fonction renvoie le tableau
    """
    f=open(fichier_source,'r') #ouverture du fichier en lecture
    mode=f.readline() #lecture de la première ligne (le type d'image)
    if mode!='P2\n':
        print("Ce n'est pas un fichier P2")
        return(None)
    dim=f.readline() #lecture de la ligne des dimensions
    while dim[0]=='#': # les lignes du commentaire sont ignorees
            dim=f.readline()
    t_dim=dim.split() #transformation de la chaine de caractère en liste
    largeur=int(t_dim[0])
    hauteur=int(t_dim[1])
    val_max=f.readline() #lecture de la valeur max de codage
    tab_source=[]
    for i in range(hauteur):
        tab_source.append([])
        for j in range (largeur):
            pixel=f.readline() #lecture du pixel
            pixel=pixel.strip('\n') #suppression des caractère "\n"
            tab_source[i].append(int(pixel))
    f.close() #fermeture du fichier
    return(tab_source)


def creer_image_P3(tab_image,nom_du_fichier):
    """
    Fonction qui crée un fichier P3 nom_du_fichier à partir d'un tableau tab_image
    Les pixels sont un triplet de couleurs (R,V,B)
    Chaque couleur est codé sur 255 niveaux de gris
    """
    hauteur=len(tab_image)
    largeur=len(tab_image[0])
    f=open(nom_du_fichier,'w') #ouverture du fichier en écriture
    f.write('P3\n')
    f.write(str(largeur)+' '+str(hauteur)+'\n')
    f.write('255\n') #on considère ici que c'est la valeur par défaut (modifiable)
    for i in range(hauteur):
        for j in range (largeur):
            for k in range(3):
                f.write(str(tab_image[i][j][k])+'\n') #écriture du pixel dans le fichier
    f.close()


def creer_image_P2(tab_image,nom_du_fichier):
    """
    Fonction qui crée un fichier P2 nom_du_fichier à partir d'un tableau tab_image
    Chaque pixel est codé sur 255 niveaux de gris
    """
    hauteur=len(tab_image)
    largeur=len(tab_image[0])
    f=open(nom_du_fichier,'w') #ouverture du fichier en écriture
    f.write('P2\n')
    f.write(str(largeur)+' '+str(hauteur)+'\n')
    f.write('255\n') #on considère ici que c'est la valeur par défaut (modifiable)
    for i in range(hauteur):
        for j in range (largeur):
            f.write(str(tab_image[i][j])+'\n') #écriture du pixel dans le fichier
    f.close()



