import pygame
import sys
from globals import *
from world.scene import Scene
from events import EventHandler
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.scene=Scene(self)
    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self):
        EventHandler.poll_events()
        for event in EventHandler.events:
            if event.type == pygame.QUIT:
                self.running = False
            
        self.scene.update()
        pygame.display.update()
        self.clock.tick(60)

    def draw(self):
        self.scene.draw()

    def close(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
