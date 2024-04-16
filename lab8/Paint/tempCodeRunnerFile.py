import pygame

pygame.init()
running = True
WIDTH, HEIGHT = 1200, 800
FPS = 60
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont("Verdana", 20)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

rectangular = pygame.Rect(10, 10, 20, 20)
circle_radius = 10
circle_center = (50, 20)

blue = pygame.Rect(1090, 10, 20, 20)
red = pygame.Rect(1130, 10, 20, 20)
green = pygame.Rect(1170, 10, 20, 20)
pos = (400,400)
color = "white"
shape = "rectangular"
eraser = pygame.image.load("eraser.png")
eraser_rect = eraser.get_rect()
eraser_rect.center = (1050, 10)
drawings = []

# Handler
def handler():
    global pos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
    return True

def menu():
    pygame.draw.aaline(screen, "black", (0, 40), (1200, 40))
    pygame.draw.rect(screen, "black", rectangular)
    pygame.draw.circle(screen, "black", circle_center, circle_radius)
    screen.blit(eraser, eraser_rect.center)
    pygame.draw.rect(screen, "blue", blue)
    pygame.draw.rect(screen, "red", red)
    pygame.draw.rect(screen, "green", green)

    

def choose_shape(pos):
    global shape
    if rectangular.collidepoint(pos):
        shape = "rectangular"
    elif ((circle_center[0] - pos[0])**2 + (circle_center[1] - pos[1])**2) <= circle_radius**2:
        shape = "circle"
    elif eraser_rect.collidepoint(pos):
        global color
        color = "white"
        shape = "rectangular"


def choose_color(pos):
    global color
    if red.collidepoint(pos):
        color = "red"
    if blue.collidepoint(pos):
        color = "blue"
    if green.collidepoint(pos):
        color = "green"

def active(color = "black", shape = "rectangular"):
    if shape == "rectangular":
        pygame.draw.rect(screen, color, (600, 10, 20, 20))
    elif shape == "circle":
        pygame.draw.circle(screen, color, (605, 18), 10)

def drawing(color = "white", shape = "rectangular", pos = pos):
    if pos[1] > 40:
        if shape == "rectangular":
            pygame.draw.rect(screen, color, [pos[0], pos[1], 20, 20])
        elif shape == "circle":
            pygame.draw.circle(screen, color, pos, 10)
    return color, shape, pos


# Game cycle
while running:
    clock.tick(FPS)
    screen.fill("white")
    running = handler()
    menu()
    choose_shape(pos)
    choose_color(pos)
    active(color, shape)

    drawings.append(drawing(color, shape, pos))
    for art in drawings:
        drawing(art[0], art[1], art[2])
    





    pygame.display.update()




pygame.quit()
