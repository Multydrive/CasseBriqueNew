import pygame

class Balle(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('assets/virus.png')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.08)
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 450
        self.velocityX = -2
        self.velocityY = -2
        self.origin_image = self.image
        self.angle = 0


    def deplacement(self):
        self.collision_mur_barre()
        self.rotate()
        self.rect.x += self.velocityX
        self.rect.y += self.velocityY

    def rotate(self):
        self.angle += 2.5
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def collision_mur_barre(self):
        for brick in self.game.wall1.wall:
            if self.game.check_collision(self, brick):
                self.game.wall1.destruction_brique(brick)
        #touche la gauche
        if self.rect.x < 0:
            self.velocityX = 2
        #touche la droite
        elif self.rect.x > 1010:
            self.velocityX = -2
        # touche le bas
        elif self.rect.y > 670:
            self.game.all_balles.remove(self)
        #touche la barre principale
        elif self.game.check_collision(self,self.game.barre):
            self.velocityY = -2
        #touche le haut
        elif self.rect.y < 35:
            self.velocityY = 2
