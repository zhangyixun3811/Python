import sys

import pygame
from bullet import Bullet
from alien import Alien


def check_down(event, sets, scr, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(sets, scr, ship)
        bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()


def check_up(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(sets, scr, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_down(event, sets, scr, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_up(event, ship)


def update_screen(sets, scr, ship, bullets, aliens):
    scr.fill(sets.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(scr)
    pygame.display.flip()


def get_num_aliens_x(sets, alien_width):
    vaild_space_x = sets.screen_width - 2 * alien_width
    number_aliens_x = int(vaild_space_x / (2 * alien_width))
    return number_aliens_x


def get_num_rows(sets, ship_height, alien_height):
    vaild_space_y = (sets.screen_height - (3 * alien_height) - ship_height)
    num_rows = int(vaild_space_y / (2 * alien_height))
    return num_rows


def create_alien(sets, scr, aliens, num, rows):
    alien = Alien(sets, scr)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * num
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rows
    aliens.add(alien)


def create_fleet(sets, scr, ship, aliens):
    alien = Alien(sets, scr)
    number_aliens_x = get_num_aliens_x(sets, alien.rect.width)
    num_rows = get_num_rows(sets, ship.rect.height, alien.rect.height)

    for row_num in range(num_rows):
        for alien_number in range(number_aliens_x):
            create_alien(sets, scr, aliens, alien_number, row_num)


def check_fleet_edges(sets, aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(sets, aliens)
            break


def change_fleet_direction(sets, aliens):
    for alien in aliens.sprites():
        alien.rect.y += sets.fleet_drop_speed
    sets.fleet_direction *= -1


def update_aliens(sets, aliens):
    check_fleet_edges(sets, aliens)
    aliens.update()


def update_bullets(sets, scr, ship, aliens, bullets):
    pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(sets, scr, ship, aliens)
