import pygame
import numpy as np
import sys
from objects.Model import Model
from objects.ModelTemp import ModelTemp
import math
import argparse

BLACK = pygame.Color('black')
WHITE = pygame.Color('grey')
GREEN = pygame.Color('green3')
RED = pygame.Color('red3')
YELLOW = pygame.Color('yellow3')
BROWN = pygame.Color('burlywood4')


def main():
    global SCREEN, CLOCK, HEADER_HEIGHT, HEADER_WIDTH
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', dest="windows", default=False, action='store_true', required=False, help="Specify to run on windows")
    args = parser.parse_args()
    if args.windows == True:
        rmt_model = ModelTemp(10, 10)
    else:
        rmt_model = Model(10, 10)

    pygame.init()
    info = pygame.display.Info()
    screen_width, screen_height = info.current_w, info.current_h

    BLOCK_WIDTH = screen_width/4
    HEADER_HEIGHT = 40
    HEADER_WIDTH = 4*BLOCK_WIDTH - 40
    BLOCK_HEIGHT = screen_height/4 - HEADER_HEIGHT

    SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    CLOCK = pygame.time.Clock()

    while True:
        drawGUI(BLOCK_WIDTH, BLOCK_HEIGHT, rmt_model)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    if y > HEADER_HEIGHT:
                        row = math.floor((y-HEADER_HEIGHT)/BLOCK_HEIGHT)
                        col = math.floor(x/BLOCK_WIDTH)
                        if row == 2:
                            if col == 0:
                                rmt_model.increment_mode()
                            elif col == 1:
                                rmt_model.increase_speed()
                            elif col == 2:
                                rmt_model.increase_spin()
                            else:
                                rmt_model.set_start()
                        elif row == 3:
                            if col == 0:
                                rmt_model.decrement_mode()
                            elif col == 1:
                                rmt_model.decrease_speed()
                            elif col == 2:
                                rmt_model.decrease_spin()
                            else:
                                rmt_model.set_stop()
                    else:
                        if x > HEADER_WIDTH:
                            pygame.quit()
                            sys.exit()


            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def drawGUI(BLOCK_WIDTH, BLOCK_HEIGHT, rmt_model):
    font = pygame.font.SysFont('Arial', 25)

    outline = pygame.Rect(0, 0, HEADER_WIDTH, HEADER_HEIGHT)
    header = pygame.Rect(0, 0, HEADER_WIDTH-2, HEADER_HEIGHT-2)

    text = font.render("Roundnet Multifunctional Trainer", True, BLACK, WHITE)
    text_rect = text.get_rect(center = header.center)

    pygame.draw.rect(SCREEN, BLACK, outline, 2)
    pygame.draw.rect(SCREEN, WHITE, header)

    SCREEN.blit(text, text_rect)

    outline = pygame.Rect(HEADER_WIDTH, 0, 40, 40)
    header = pygame.Rect(HEADER_WIDTH, 0, 40-2, 40-2)

    text = font.render("X", True, BLACK, RED)
    text_rect = text.get_rect(center = header.center)

    pygame.draw.rect(SCREEN, BLACK, outline, 2)
    pygame.draw.rect(SCREEN, RED, header)

    SCREEN.blit(text, text_rect)

    for row in range(0, 4):
        for col in range(0, 4):
            outline = pygame.Rect(col*BLOCK_WIDTH, row*BLOCK_HEIGHT + HEADER_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
            button = pygame.Rect(col*BLOCK_WIDTH, row*BLOCK_HEIGHT + HEADER_HEIGHT, BLOCK_WIDTH-2, BLOCK_HEIGHT-2)
            
            text = font.render(rmt_model.getText(row, col), True, BLACK, WHITE)
            text_rect = text.get_rect(center = button.center)
            
            pygame.draw.rect(SCREEN, BLACK, outline, 2)
            pygame.draw.rect(SCREEN, WHITE, button)

            SCREEN.blit(text, text_rect)


if __name__ == "__main__":
    main()
