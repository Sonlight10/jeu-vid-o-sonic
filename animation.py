import pygame

# definir une classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    # definir les choses à faire à la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0 # commencer l'animation à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # definir une methode pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    # definir une methode pour animer le sprite
    def animate(self, loop=False):

        # verifier si l'animation est active
        if self.animation :

            # passer à l'image suivante
            self.current_image += 1

        # verifier si on a atteint la fin de l'animation
        if self.current_image >= len(self.images):
            # remettre l'animation au départ
            self.current_image = 0

            # verifier si l'animation n'est pas en mode boucle
            if loop is False :
                # desactivation de l'animation
                 self.animation = False

        # modifier l'image précédente par la suivante
        self.image = self.images[self.current_image]

# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # recuperer le chemin du dossier pour ce sprite
    path = f'assets/{sprite_name}/{sprite_name}'

    # boucler sur chaque image dans ce dossier
    for num in range(1,10):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'images
    return images


# definir un dictionnaire qui va contenir les images chargées de chaque sprite
# gamma -> [...gamma1.png, ...gamma2.png, ...]
# sonic -> [...sonic1.png, ...sonic2.png, ...]
animations = {
    'gamma' : load_animation_images('gamma'),
    'sonic' : load_animation_images('sonic')
}
