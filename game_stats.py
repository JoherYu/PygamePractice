"""跟踪游戏统计信息"""
class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = False
        self.reset_stats()
        
    # 设置可用飞船数，用于重新开始游戏时重置游戏信息
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0