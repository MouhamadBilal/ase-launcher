import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self,comet_event):
        super().__init__()
        # définir l'image de la comète
        self.image = pygame.image.load('assets/comet.png')
        self.rect=self.image.get_rect()
        self.velocity = random.randint(3,5)
        self.rect.x = random.randint(20, 700)
        self.rect.y = - random.randint(0, 700)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        # si le nombre de cometes sont a zero
        if len(self.comet_event.all_comets) == 0:
            print ("retour des monstres")
        #remettre la barre a zero
        self.comet_event.reset_percent()
        # refaire apparaitre les monstres
        self.comet_event.game.spawn_monster()
        

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >=600:
            print ("sol")
            # retirer la comete
            self.remove()
            if len(self.comet_event.all_comets) ==0:
                print ('retour des monstres')
                #remmettre la jauge au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

         #si la comette touche le joueur        
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            print ("joueur touché")
            self.remove()
            # le faire subir des dégats
            self.comet_event.game.player.damage(20)
