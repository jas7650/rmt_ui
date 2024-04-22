import pygame

BLACK = pygame.Color('black')
WHITE = pygame.Color('grey')
GREEN = pygame.Color('green3')
RED = pygame.Color('red3')
YELLOW = pygame.Color('yellow3')
BROWN = pygame.Color('burlywood4')

class RMTButton(object):

    def __init__(self, row, col, width, height, screen, rmt_model):
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.screen = screen
        self.rmt_model = rmt_model
        self.font = pygame.font.SysFont('Arial', 25)


    def process(self):
        self.text = self.font.render(self.rmt_model.getText(self.row, self.col), True, BLACK, WHITE)
        self.rect = self.text.get_rect()
        self.rect.update(self.col * self.width + self.width/2.0, self.row * self.height + self.height/2.0, self.width, self.height)
        print(type(self.rect))
        print(type(self.text))
        self.screen.blit(self.text, (self.col * self.width + self.width/2.0, self.row * self.height + self.height/2.0))
        self.screen.blit()
