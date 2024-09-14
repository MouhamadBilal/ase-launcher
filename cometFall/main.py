import pygame
pygame.init()

from game import Game

from player import Player


from monster import Monster


#générer la fenetre de mon jeu
pygame.display.set_caption("comet fall Game")
screen = pygame.display.set_mode((1000,720))

#importer de charcher l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')


# importer la bannière 
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner,(500, 500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() /4

# importer le bouton pour lancer la partie 

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button,(400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() /3.33
play_button_rect.y = screen.get_height() /2
#charger le jeu 
game = Game()

#charger le joueur
player = Player(game)



running= True
#boucle tant que cette condition est vrai
while running:

    #appliquer l'arrière plan du jeux
    screen.blit(background, (0, -200))
 
    # verifier si le jeux tourne 
    if game.is_playing:
        # declencher mes instructions de la partie
        game.update(screen)
    
    else:
        screen.blit(play_button,play_button_rect)
        screen.blit(banner, banner_rect)
        


    #mettre a jour l'ecran
    pygame.display.flip()


    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():

        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('fermeture du jeu')

        #touches de déplacements et d'actions
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        #touches du projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key]= False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier si la souris clic sur le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode "lancé"
                game.start()
