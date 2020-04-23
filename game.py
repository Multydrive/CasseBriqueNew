import pygame
import random
from barre import Barre
from balle import Balle
from brique import Brick, Wall
from Protector import protector
from bonus import Bonus


class Game:

    def __init__(self):
        #générer le joueur
        self.barre = Barre()
        self.pressed = {}
        self.all_balles = []
        self.wall1 = Wall(self)
        self.Protector = protector()
        self.balle_actuelle = 0
        self.balle_vie = 3
        self.all_bonus = []
        self.points = 0
        #self.type_bonus = Bonus(self)

    def lancer_balle(self):
        if self.balle_actuelle == 0 and self.balle_vie > 0:
            self.balle = Balle(self)
            self.all_balles.append(self.balle)
            self.balle_actuelle = 1
            self.balle_vie -= 1
            print(self.balle_vie)
        elif self.balle_actuelle == 1:
            print("Balle deja existante")
        elif self.balle_vie == 0:
            print("Plus de vie")

    def spawn_bonus(self, x, y):
        self.choix = random.randint(0,1)
        if self.choix > 1:
            print("raté")
        elif self.choix == 0:
            self.image = pygame.image.load('assets/BonusLigne.png')
            self.bonus = Bonus(self, x, y,self.image)
            self.all_bonus.append(self.bonus)
            self.bonus.different = 1
        elif self.choix == 1:
            self.image = pygame.image.load('assets/bonus.png')
            self.bonus = Bonus(self, x, y,self.image)
            self.all_bonus.append(self.bonus)
            self.bonus.different = 0

    def check_collision(self, sprite1, sprite2):
        return pygame.sprite.collide_rect(sprite1, sprite2)
