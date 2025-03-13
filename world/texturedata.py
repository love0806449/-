from globals import *

atlas_texture_data={
    'grass':{'type':'block','size':(TILESIZE,TILESIZE),'position':(0,0)},
    'dirt':{'type':'block','size':(TILESIZE,TILESIZE),'position':(0,1)},
    'stone':{'type':'block','size':(TILESIZE,TILESIZE),'position':(1,0)},
    'diamond':{'type':'block','size':(TILESIZE,TILESIZE),'position':(2,3)}
}
solo_texture_data={
    'player_static':{'type':'player','file_path':'res/player.jpg','size':(TILESIZE*4,TILESIZE*4)},
    'fish_static':{'type':'enemy','file_path':'res/fish.png','size':(TILESIZE*4,TILESIZE*4)},
    'short_sword':{'type':'weapon','file_path':'res/weapons/shortsword.png','size':(TILESIZE,TILESIZE)}
}