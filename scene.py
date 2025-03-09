import pygame
from globals import *
from sprite import Entity
from player import Player
from texturedata import solo_texture_data, atlas_texture_data
from opensimplex import OpenSimplex
from camera import Camera
class Scene:
    def __init__(self,app) -> None:
        self.app=app

        self.solo_textures=self.gen_solo_texture()
        self.atlas_textures=self.gen_atlast_textures('res/atlas.png')

        
       

        self.sprites=Camera()

        self.blocks=pygame.sprite.Group()

        self.entity=Entity([self.sprites],image=self.atlas_textures['grass'])
        Entity([self.sprites],position=(200,200),image=self.atlas_textures['stone'])


       

        self.player=Player([self.sprites],self.solo_textures['player_static'],(600,300),parameters={'block_group':self.blocks})

        self.gen_world()

    def gen_solo_texture(self):
        textures={}

        for name,data in solo_texture_data.items():
            textures[name]=pygame.transform.scale(pygame.image.load(data['file_path']).convert_alpha(),data['size'])

        return textures
    def gen_atlast_textures(self,filepath):
        textures={}
        atlas_img=pygame.transform.scale(pygame.image.load(filepath).convert_alpha(),(TILESIZE*16,TILESIZE*16))

        for name,data in atlas_texture_data.items():
            textures[name]=pygame.Surface.subsurface(atlas_img,pygame.Rect(data['position'][0]*TILESIZE,
                                                                           data['position'][1]*TILESIZE,
                                                                           data['size'][0],
                                                                           data['size'][1]))
        return textures
    def gen_world(self):
        noise_generator=OpenSimplex(seed=92564812)

        heightmap=[]
        for y in range(20):
            noise_value=noise_generator.noise2(y*0.05,0)
            height=int((noise_value+1)*4+5)
            heightmap.append(height)

        for x in range(len(heightmap)):
            for y in range(heightmap[x]):
                y_offset=5-y+6
                texture=self.atlas_textures['dirt']
                if y==heightmap[x]-1:
                    texture=self.atlas_textures['grass']
                if y<heightmap[x]-5:
                    texture=self.atlas_textures['stone']
                    
                Entity([self.sprites,self.blocks],texture,(x*TILESIZE,y_offset*TILESIZE))
    def update(self):
        self.sprites.update()

    def draw(self):
        self.app.screen.fill("lightblue")
        self.sprites.draw(self.player,self.app.screen)