"""
Нарисуйте при помощи случайных поворотов и перемещений картину броуновских движений.
https://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
https://realpython.com/pygame-a-primer/
"""
import random
import pygame

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = [400, 300]

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Рандомное дважение')
my_display = pygame.display.Info()
display_w = my_display.current_w
display_h = my_display.current_h

x0 = display_w // 2
y0 = display_h // 2
max_div = 10

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            done = True

    x = x0 + random.randint(-max_div, max_div)
    y = y0 + random.randint(-max_div, max_div)

    screen.fill(WHITE)
    pygame.draw.line(screen, RED, [x0, y0], [x, y], 2)
    x0, y0 = x, y
    if x0 > display_w:
        x0 -= display_w
    if x0 < 0:
        x0 = display_w - x0
    if y0 > display_h:
        y0 -= display_h
    if y0 < 0:
        y0 = display_h - y0

    pygame.display.flip()
