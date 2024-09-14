import pygame

from projectile import Projectile

import animation

class Player(animation.AnimateSprite):
    
    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 30
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y =  500

    def damage (self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else : 
            # si le joueur n'a plus de pv
            self.game.game_over()


    def update_animation(self):
        self.animate()


    def update_health_bar(self, surface):
          
    #dessiner la barre de pv
        pygame.draw.rect(surface, (60,63,60), [self.rect.x +50, self.rect.y +20, self.max_health, 5])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x +50, self.rect.y +20, self.health, 5])
        

    def launch_projectile(self):
        #créer une instance de la classe du projectile
       
        self.all_projectiles.add(Projectile(self))
        # animer le lancer de projectile
        self.start_animation()



        #deplacement du joueur 
    def move_right(self):
        #si le joueur n'est pas en contact avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity
