import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():

    # 初始化游戏、设置、创建屏幕对象
    pygame.init()
    pygame.display.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(screen, sets=ai_settings)

    # 游戏主循环
    while True:

        # 监听键盘鼠标事件
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
