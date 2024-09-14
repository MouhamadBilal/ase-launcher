import pygame
import random


import animation

#créer la classe de gestion des monstres

class Monster(animation.AnimateSprite):

    def __init__(self, game,name):
        super().__init__(name)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        self.rect = self.image.get_rect()
        self.rect.x = 1000  + random.randint(0,250)
        self.rect.y = 540
        self.velocity = random.randint (1,2)
        self.start_animation()
        
    def damage(self,amount):
        # infliger les dégat du monstre
        self.health -= amount

        # tuer le montre 
        if self.health <= 0:
            # réapparaitre 
            self.rect.x = 1000 + random.randint(0,250)
            self.health = self.max_health

            #verifier si la barre est chargée 
            if self.game.comet_event.is_full_loaded():
                #retirer le monstre
                self.game.all_monsters.remove(self)
                
                # déclencher les commetes 
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
      
        #dessiner la barre de pv
        pygame.draw.rect(surface, (60,63,60), [self.rect.x +10, self.rect.y -20, self.max_health, 5])

        pygame.draw.rect(surface, (111,210,46), [self.rect.x +10, self.rect.y -20, self.health, 5])
        

    def forward(self):
        #le deplacement se fait que si ya pas de contact avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le montre est en colision
        else:
            # inflige les dégat au joueur
            self.game.player.damage(self.attack)

# definir une classe pour la momie
class Mummy(Monster):

    def __init__(self,game):
        super().__init__(game, "mummy")

# ajouter un alien
# class Alien(Monster):

#     def __init__(self, game):
#         super().__init__(game, "alien")