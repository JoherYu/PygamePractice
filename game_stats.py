"""跟踪游戏统计信息"""
class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = True
        self.reset_stats()
        
    # 设置可用飞船数
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit