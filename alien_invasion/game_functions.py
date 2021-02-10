import sys

import pygame


def check_down(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_up(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_down(event, ship)
        elif event.type == pygame.KEYUP:
            check_up(event, ship)


def update_screen(sets, scr, ship):
    scr.fill(sets.bg_color)
    ship.blitme()
    pygame.display.flip()
