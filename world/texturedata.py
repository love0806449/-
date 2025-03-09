from globals import *

atlas_texture_data={
    'grass':{'type':'block','size':(TILESIZE,TILESIZE),'position':(0,0)},
    'dirt':{'type':'block','size':(TILESIZE,TILESIZE),'position':(0,1)},
    'stone':{'type':'block','size':(TILESIZE,TILESIZE),'position':(1,0)}
}
solo_texture_data={
    'player_static':{'type':'player','file_path':'res/player.jpg','size':(TILESIZE,TILESIZE)},
    'fish_static':{'type':'enemy','file_path':'res/fish.png','size':(TILESIZE,TILESIZE)}
}