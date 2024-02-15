import sys

import pygame
from pygame import Surface


def show_static_image(image: Surface, screen, is_last=False):
    screen.blit(image, (0, 0))  # Draw the image on the screen
    pygame.display.flip()  # Update the display

    # Wait for the player to press space
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and not is_last:
                if event.key == pygame.K_SPACE:
                    waiting = False
