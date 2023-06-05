class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.speed = 1.5
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10  # 外星人向右撞到屏幕，向下移动的速度
        self.fleet_direction = -1   # 1表示向左移动，-1表示向右
        self.ship_limit = 3     # 拥有的飞船数

        self.speedup_scale = 1.1    # 加快游戏节奏的速度
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_drop_speed = 1

    def increase_speed(self):
        self.speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
