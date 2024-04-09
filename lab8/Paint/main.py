import pygame

pygame.init()

running = True
WIDTH = 1200
HEIGHT = 800
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

def handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def menu():
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    circle = pygame.draw.circle(screen, 'white', (35, 35), 20)
    rectangular = pygame.draw.rect(screen, 'white', [76.5, 26, 37, 20])

    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])

def active(color, shape):
    if shape == "rect":
        pygame.draw.rect(screen, color, )

while running:
    clock.tick(FPS)
    running = handler()

    menu()


    pygame.display.update()


pygame.quit()

