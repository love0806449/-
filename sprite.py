import pygame

from globals import *
import math
class Entity(pygame.sprite.Sprite):
    def __init__(self, groups,image=pygame.Surface((TILESIZE,TILESIZE)),position=(0,0)):
       super().__init__(groups)
       self.in_groups=groups
       self.image = image
       self.rect = self.image.get_rect(topleft=position)
    def update(self):
        pass
       
class Mob(Entity):
    def __init__(self, groups, image=pygame.Surface((TILESIZE,TILESIZE)),position=(0,0),parameters=None):
        super().__init__(groups, image, position)
        
        if parameters:
            self.block_group=parameters['block_group']
            self.player=parameters['player']

        self.velocity=pygame.math.Vector2()
        self.mass=5
        self.speed=0.5
        self.termianl_velocity=TERMINALVELOCITY*self.mass

        #states
        self.attacking=True
        self.grounded=False
    def move(self):
        self.velocity.y+=GRAVITY*self.mass
        #terminal velocity check
        if self.velocity.y>self.termianl_velocity:
            self.velocity.y=self.termianl_velocity

        if abs(math.sqrt((self.rect.x-self.player.rect.x)**2+(self.rect.y-self.player.rect.y)**2))<TILESIZE*10:
            #within range
            if self.rect.x>self.player.rect.x:
                self.velocity.x=-self.speed
            elif self.rect.x<self.player.rect.x:
                self.velocity.x=self.speed
            self.attacking=True
        else:
            self.attacking=False
            self.velocity.x=0

        self.rect.x+=self.velocity.x*PLAYERSPEED #apply hor velocity

        self.check_collisions('horizontal')

        self.rect.y+=self.velocity.y #apply ver velocity

        self.check_collisions('vertical')


        if self.grounded and self.attacking and abs(self.velocity.x)<0.1:
            self.velocity.y=-8
    def check_collisions(self,direction):
        if direction=='horizontal':
            for block in self.block_group:
                if block.rect.colliderect(self.rect):
                    if self.velocity.x>0: #to right
                        self.rect.right=block.rect.left
                    if self.velocity.x<0: #to left
                        self.rect.left=block.rect.right
                    
                    self.velocity.x=0
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
        self.move()