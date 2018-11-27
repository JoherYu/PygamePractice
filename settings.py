# 游戏设置文件
class Settings():

    def __init__(self):
        # 初始化屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (135, 206, 235)
        # 初始化游戏元素
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        
        self.bullets_allowed = 11