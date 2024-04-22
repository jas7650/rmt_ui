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
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.row*self.width, self.col*self.height, self.width, self.height)


    def process(self):
        color = WHITE
        text = self.font.render(self.rmt_model.getText(self.row, self.col), True, BLACK, WHITE)
        self.surface.fill(color)
        self.surface.blit(text, self.rect)
        self.screen.blit(self.surface, self.rect)
