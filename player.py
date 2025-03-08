import pygame
from globals import *
from events import EventHandler
class Player(pygame.sprite.Sprite):
    def __init__(self,groups,image:pygame.Surface,position:tuple,parameters)->None:
        super().__init__(groups)
        self.image = image
        self.rect=self.image.get_rect(topleft=position)

        #parameters
        self.block_group=parameters['block_group']

        self.velocity=pygame.math.Vector2()
        self.mass=5
        self.termianl_velocity=self.mass*TERMINALVELOCITY

        #is grounded
        self.grounded=True
    def input(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.velocity.x=-1
        if keys[pygame.K_d]:
            self.velocity.x=1
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.velocity.x=0

        #jumping
        if self.grounded and EventHandler.keydown(pygame.K_SPACE):
            self.velocity.y=-PLAYERJUMPPOWER

    def move(self):
        self.velocity.y+=GRAVITY*self.mass
        #terminal velocity check
        if self.velocity.y>self.termianl_velocity:
            self.velocity.y=self.termianl_velocity

        self.rect.x+=self.velocity.x*PLAYERSPEED #apply hor velocity

        self.check_collisions('horizontal')

        self.rect.y+=self.velocity.y #apply ver velocity

        self.check_collisions('vertical')
    def check_collisions(self,direction):
        if direction=='horizontal':
            for block in self.block_group:
                if block.rect.colliderect(self.rect):
                    if self.velocity.x>0: #to right
                        self.rect.right=block.rect.left
                    if self.velocity.x<0: #to left
                        self.rect.left=block.rect.right
        elif direction=='vertical':
            collisions=0
            for block in self.block_group:
                if block.rect.colliderect(self.rect):
                    if self.velocity.y>0: #to down
                        collisions+=1
                        self.rect.bottom=block.rect.top
                    if self.velocity.y<0: #to up
                        self.rect.top=block.rect.bottom
            if collisions>0:
                self.grounded=True
            else:
                self.grounded=False
                    
    def update(self):
        self.input()
        self.move()
