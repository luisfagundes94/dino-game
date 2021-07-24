import pygame

class Game():

    WIDTH = 1280
    HEIGHT = 720

    def __init__(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
        pygame.quit()


