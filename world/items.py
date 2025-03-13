from globals import *
from world.sprite import *

class Item:
    def __init__(self,name:str="default",quantity:int=0) -> None:
        self.name=name
        self.quantity=quantity
    def use(self,*args,**kwargs):
        pass
    def attack(self,*args,**kwargs):
        pass
    def __str__(self):
        return f'Name:{self.name},Qunatity:{self.quantity}'
class BlockItem(Item): #可放置方塊的物品
    def __init__(self,name:str,quantity:int=1)->None:
        super().__init__(name,quantity)
    def use(self,player,position:tuple): #placing the block
        if self.quantity>0:
            items[self.name].use_type([player.group_list[group] for group in items[self.name].groups],player.textures[self.name],position,self.name)
            self.quantity -=1
            if self.quantity<=0:
                self.name="default" 
        else:
            self.name="default"

class ShortSwordIteam(Item):
    def __init__(self,name:str="default",quantity:int=0)->None:
        super().__init__(name,quantity)
    def use(self,player,position:tuple):
        print("using")
    def attack(self,player,target):
        target.kill()
class ItemData:
    def __init__(self,name:str,quantity:int=1,groups:list[str]=['sprites','block_group'],use_type:Entity=Entity,item_type:Item=Item) -> None:
        self.name=name
        self.quantity=quantity
        self.groups=groups
        self.use_type=use_type
        self.item_type=item_type
        
items:dict[str,ItemData]={
    'grass':ItemData('grass',item_type=BlockItem),
    'dirt':ItemData('dirt',item_type=BlockItem),
    'stone':ItemData('stone',item_type=BlockItem),
    'diamond':ItemData('diamond',item_type=BlockItem),
    'short_sword':ItemData('sword_sword',item_type=ShortSwordIteam)
}