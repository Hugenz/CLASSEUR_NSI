import pygame
from pygame.locals import *
import time
from random import *

"""
initialisation des paramètres de jeu
"""
h = 2**9 #dimension du plateau carré (puissance de 2)
c = h//(2**4) #taille d'un élément (puissance de 2)
n = h//c #nombre de positions sur une longueur
coul1 = (100,100,50) #couleur de la tete
coul2 = (200,200,100) #couleur de la queue
coul3 = (255,0,0) #couleur de la cible
coul4 = (10,50,10) #couleur du fond
coul5 = (200,200,200)
delay = 200 #délais entre deux affichages

"""
snake est une liste de tuples
au démarrage :
placement aléatoire de la tête seule
"""
x = randint(1,n-1)
y = randint(1,n-1)
snake = [(x,y)]

"""
la cible est un carré
placé aléatoirement
"""
xc = randint(1,n-1)
yc = randint(1,n-1)


# coordonnées de la bombe
position_bombe_x = randint(1,n-1)
position_bombe_y = randint(1,n-1)
# couleur de la bombe
coul_bombe = (10,10,10)


pygame.init()

ecran = pygame.display.set_mode((h,h)) #affichage du plateau
pygame.display.set_caption("Snake") #affichage du titre
ecran.fill(coul4) #mise en couleur du fond

#placement de la cible
pygame.draw.rect(ecran, coul3, (xc*c, yc*c, c, c))

#démarrage vers la droite
left,right,up,down = False,True,False,False


t1 = time.time()


continuer = True
while continuer:

    t2 = time.time()

    pygame.time.delay(delay) #temporisation
##    print(snake)
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == KEYDOWN :
            if event.key == K_ESCAPE:
                continuer = False
            # changement de direction, demi-tour interdit
            elif event.key == K_LEFT and not right:
                left,right,up,down = True,False,False,False
            elif event.key == K_RIGHT and not left:
                left,right,up,down = False,True,False,False
            elif event.key == K_UP and not down:
                left,right,up,down = False,False,True,False
            elif event.key == K_DOWN and not up:
                left,right,up,down = False,False,False,True

    temp_last = snake[-1] #position l'extremité de la queue
    snake[1:] = snake[:-1] #décalage de la queue
    #changement de position de la tête
    temp_head = (x,y) #position de la tête avant le déplacement
    if left:
        x -= 1
    elif right:
        x += 1
    elif up:
        y -= 1
    elif down:
        y += 1
    #position modulo la largeur du plateau
    x %= n
    y %= n
    snake[0] = (x,y) #nouvelle position de la tête

    #placement de la tête
    pygame.draw.rect(ecran, coul1, (x*c, y*c, c, c))

    #placement du premier élément de la queue
    pygame.draw.rect(ecran, coul2, (temp_head[0]*c, temp_head[1]*c, c, c))

    # cible atteinte
    if (x,y) == (xc,yc):
        snake.append(temp_last)
        #placement d'une nouvelle cible
        encore = True
        while encore:
            xc = randint(1,n-1)
            yc = randint(1,n-1)
            if (xc,yc) not in snake:
                pygame.draw.rect(ecran, coul3, (xc*c, yc*c, c, c))
                encore = False
    else:
        #effacement du dernier élément de la queue
        pygame.draw.rect(ecran, coul4, (temp_last[0]*c, temp_last[1]*c, c, c))

    #update de l'affichage
    pygame.display.update()


    if t2 - t1 >= 3:
        pygame.draw.rect(ecran, coul4, (position_bombe_x * c, position_bombe_y * c, c, c)) # effacement de la bombe
        position_bombe_x = randint(1,n-1) # nouvelle position de la bombe
        position_bombe_y = randint(1,n-1) # nouvelle position de la bombe
        pygame.draw.rect(ecran, coul_bombe, (position_bombe_x*c, position_bombe_y*c, c, c)) # placement de la bombe
        pygame.display.update()
        t1 = t2 # mise à jour du temps

    if (x, y) == (position_bombe_x, position_bombe_y):
        continuer = False



    #test de fin de partie si la tête touche la queue
    if snake.count(snake[0]) != 1:
        pygame.time.delay(1000)
        continuer = False

pygame.quit()


