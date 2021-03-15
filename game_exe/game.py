import pygame
import random

size = width, height = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.init()


def draw():
    for i in range(width * 10):
        screen.fill(pygame.Color('red'), (random.random() * width, random.random() * height, 1, 1))
    color = pygame.Color(255, 10, 10)
    pygame.draw.rect(screen, color, (53, 53, 100, 100), 0)
    hsv = color.hsva
    color.hsva = (hsv[0] + 5, hsv[1] + 20, hsv[2] + 20, hsv[3])
    pygame.draw.rect(screen, color, (50, 50, 100, 100), 0)
    # screen.fill(pygame.Color('red'), pygame.Rect(55, 55, 75, 75))


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
