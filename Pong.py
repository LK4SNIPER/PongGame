import pygame
import sys

# General setup
pygame.init()
clock = pygame.time.Clock()
screen_widght = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_widght, screen_height))
pygame.display.set_caption("Pong")

# Game rectanles
ball = pygame.Rect(screen_widght/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_widght - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)

    # Updating window
    pygame.display.flip()
    clock.tick(60)
