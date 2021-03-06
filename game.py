import pygame
import random
import os
from barre import Barre
from balle import Balle
from brique import Brick, Wall
from Protector import Protector
from bonus import Bonus


class Game:

    #Constructeur du jeu
    def __init__(self):
        self.barre = Barre()
        self.pressed = {}
        self.all_balles = []
        self.protector = Protector()
        self.balle_vie = 3
        self.all_bonus = []
        self.points = 0
        self.vit = 5
        self.randomMin = 0
        self.spawn_balle(self.vit)
        self.spawn_mur(self.randomMin)
        self.click = False

    #Apparition de la balle
    def spawn_balle(self,vit):
        if self.balle_vie > 0:
            self.balle = Balle(self,vit)
            self.all_balles.append(self.balle)

    #Apparition des briques
    def spawn_mur(self,randomMin):
        self.randomMin = randomMin
        self.wall1 = Wall(self,self.randomMin)

    #Apparition des bonus aleatoire
    def spawn_bonus(self, x, y):
        self.choix = random.randint(0,8)
        if self.choix == 0:
            self.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/BonusLigne.png'))
            self.bonus = Bonus(self, x, y,self.image)
            self.all_bonus.append(self.bonus)
            self.bonus.different = 1

        elif self.choix == 1:
            self.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/bonus.png'))
            self.bonus = Bonus(self, x, y,self.image)
            self.all_bonus.append(self.bonus)
            self.bonus.different = 0

        elif self.choix == 2:
            self.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/malus.png'))
            self.bonus = Bonus(self, x, y,self.image)
            self.all_bonus.append(self.bonus)
            self.bonus.different = 2

    #Verification des collisions
    def check_collision(self, sprite1, sprite2):
        return pygame.sprite.collide_rect(sprite1, sprite2)

    #Configuration ecran de fin de partie
    def loose(self):
        self.button_1 = pygame.Rect(440, 250 , 200 , 50)
        self.button_2 = pygame.Rect(440, 350, 200 , 50)
        self.rectangle = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/gameover.png'))
        self.rectangle = pygame.transform.scale(self.rectangle, (500,500))
        self.rectangles = self.rectangle.get_rect()
        self.rectangles.x = 280
        self.rectangles.y = 50
        self.option = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/restart.png'))
        self.option = pygame.transform.scale(self.option , (200,50 ))
        self.options = self.option.get_rect()
        self.options.x = 430
        self.options.y = 250
        self.exit = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/exit.jpg'))
        self.exit = pygame.transform.scale(self.exit, (200,50))
        self.exits = self.option.get_rect()
        self.exits.x = 430
        self.exits.y = 350
