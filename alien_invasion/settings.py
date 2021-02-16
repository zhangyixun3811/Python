class Settings():
    """存储《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        # 子弹设置
        self.bullet_speed = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 外星人设置
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
