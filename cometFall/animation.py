import pygame

#définir une classe qui va s'occuper de lanimation
class AnimateSprite(pygame.sprite.Sprite):

    #je définir les choses a faire pour la création des entités
    def __init__(self,sprite_name):
        super().__init__()
        # appeler dirrectement l'image d'animation dans le dossier
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image= 0 #commencer l'animation a l'image 0
        self.images = animations.get(sprite_name)


    def start_animation(self):
        self.animation = True

    # definir une methode pour animer mon sprite 
    def animate(self, loop=False):

        # verifier si l'animation est active
        # if self.animation :
            # passer à l'image suivante
            self.current_image += 1

            # verifier si j'ai attein la fin de l'animation
            if self.current_image >=len(self.images):
                # remettre l'anim au départ
                self.current_image = 0
                # modifier limage précédente par la suivante 
                self.image = self.images[self.current_image]
                if loop is False:
                    self.animation = False
                   
#définir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    #charger toute les images de ce sprite dans le dossier
    images =[]
    #prendre le chemin du dossier
    path = f"../assets/{sprite_name}/{sprite_name}"

    #boucler sur chaque images dans ce dossier
    for num in range (1,24):
        image_path = path + str(num) + '.png'
        pygame.image.load(image_path)
        images.append(pygame.image.load(image_path))
        
        # renvoi du contenu de la liste
        return images
        # ADMIsions@efrei.fr


# definir le dictionnaire  qui contiendra les images chargé
# mummy -> [...mummy1.png,...mummy2.png,...]
animations = {
    'mummy': load_animation_images('mummy'),
    'player':load_animation_images('player'),
}