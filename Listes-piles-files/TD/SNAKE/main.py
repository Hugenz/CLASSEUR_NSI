import pygame, time, random


# Variable #

dimensions = largeur, hauteur = 900, 600
couleur_fond = 0, 0, 0
couleur_snake = 0, 255, 0
couleur_pomme = 255, 0, 0
blocsec = 5
timer = time.time()
clock = pygame.time.Clock()
score = 0

# Pygame #

pygame.init()
fenetre = pygame.display.set_mode((dimensions))
pygame.display.set_caption("Snake by Hugenz")
pygame.display.flip()
coordsnake = [[450, 300]]
coordpomme = [random.randrange(0, largeur, 30), random.randrange(0, hauteur, 30)]

# creation de la direction
snake_direction_x = 0
snake_direction_y = 0




continuer = True
while continuer:

    fenetre.fill((40, 100, 40))
    for i in range(30):
        for j in range(30):
            pygame.draw.rect(fenetre, (70, 130, 70), (i * 30, j * 30, 30, 30), 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False



    # recoloration de l'ecran
    # fenetre.fill(couleur_fond)

    # creation tete du snake
    pygame.draw.rect(fenetre, couleur_snake, (coordsnake[0][0], coordsnake[0][1], 30, 30))


    # deplacement du snake dans la fenetre

    if coordsnake[0][0] < 0:
        coordsnake[0][0] = largeur
    if coordsnake[0][0] > largeur:
        coordsnake[0][0] = 0
    if coordsnake[0][1] < 0:
        coordsnake[0][1] = hauteur
    if coordsnake[0][1] > hauteur:
        coordsnake[0][1] = 0

    # affichage de la pomme

    pygame.draw.rect(fenetre, couleur_pomme, (coordpomme[0], coordpomme[1], 30, 30))

    # lorque le snake mange une pomme il grandit de 1 bloc et une nouvelle pomme apparait

    if coordsnake[0][0] == coordpomme[0] and coordsnake[0][1] == coordpomme[1]:
        coordpomme = [random.randrange(0, largeur, 30), random.randrange(0, hauteur, 30)]
        coordsnake.append([coordsnake[-1][0], coordsnake[-1][1]+30])
        score += 1
        print(score)
        print (coordsnake)

    # afficher la liste des coordonnées du snake

    for i in range(1, len(coordsnake)):
        coordsnake[i][0] = coordsnake[i-1][0]
        coordsnake[i][1] = coordsnake[i-1][1]
        pygame.draw.rect(fenetre, couleur_snake, (coordsnake[i][0], coordsnake[i][1], 30, 30))






    # affichage du score

    font = pygame.font.SysFont("comicsansms", 30)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    fenetre.blit(text, (0, 0))


    # deplacement du snake avec les fleches


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            snake_direction_x = -1
            snake_direction_y = 0
        elif event.key == pygame.K_RIGHT:
            snake_direction_x = 1
            snake_direction_y = 0
        elif event.key == pygame.K_UP:
            snake_direction_x = 0
            snake_direction_y = -1
        elif event.key == pygame.K_DOWN:
            snake_direction_x = 0
            snake_direction_y = 1

    if time.time() - timer >= 1 / blocsec:
        coordsnake[0][0] += snake_direction_x * 30
        coordsnake[0][1] += snake_direction_y * 30
        timer = time.time()



    # ralentir le snake

    clock.tick(50)

    pygame.display.flip()

pygame.quit()



