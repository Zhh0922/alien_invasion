class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.score = None
        self.ships_left = None
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True
        self.high_score = 0     # 任何情况下都不应该重置最高得分
        self.level = 1

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
