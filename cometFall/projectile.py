import pygame

#definir la classe du projectile

class Projectile(pygame.sprite.Sprite):

    #def le constructeur du projectile
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 5
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x +120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner le projectile
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
    def remove(self):
        self.player.all_projectiles.remove(self)

        #deplacer le projectile 
    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #verifier si le projectile frappe le monstre 
        for monster in  self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le projectile 
            self.remove()
            monster.damage(self.player.attack)
        if self.rect.x > 1080:
            #suppriler le projectile dés qu'il sort de l'ecran
            self.remove
        