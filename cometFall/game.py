import pygame
from player import Player
from monster import Monster,Mummy,Alien
from comet_event import CometFallEvent
from comet import Comet

#créer une autre classe qui va representer le jeux
class Game:

    def __init__(self):
        # définir si le jeu à commencer
        self.is_playing = False
        #generer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer les evenements
        self.comet_event = CometFallEvent(self)
        #groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        


    def start (self):
        self.is_playing =True
        self.spawn_monster(Mummy)
        # self.spawn_monster(Alien)
       

    def game_over(self):
        # remettre le jeux à neuf (retirer les monstres et remettre le joeur à 100pv)
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False


    def update(self, screen):
        #appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre d'evenement 
        self.comet_event.update_bar(screen)


        self.player.update_health_bar(screen)
        #récuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move() 
        
        # actualiser l'animation du joueur
        self.player.update_animation()

        #récuperer les monstres du jeu 
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # recuperer les comettes
        for comet in self.comet_event.all_comets:
            comet.fall()
       #afficher l'ensembles des images du groupe de projectile 
        self.player.all_projectiles.draw(screen)


        #afficher l'ensembles des images du monstre
        self.all_monsters.draw(screen)  
        # afficher l'ensemble des image de comettes
        self.comet_event.all_comets.draw(screen)

        #verifier si le joueur va a droite ou a gauche
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width< screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        



    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    #faire apparaitre les monstres en continue
    def spawn_monster(self,monster_class_name):
        # on instancie l'objet 
        self.all_monsters.add(monster_class_name.__call__(self))
