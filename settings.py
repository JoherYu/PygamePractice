# 游戏设置文件
class Settings():

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (135, 206, 235)
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 11  # 允许屏幕同时存在的子弹数
        # 外星人降落速度设置
        self.fleet_drop_speed = 10  
        # 可用飞船数设置
        self.ship_limit = 3
        # 游戏加速乘子
        self.speedup_scale = 1.1  
        # 动态参数设置
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        # 游戏元素速度设置
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 3
        # 乘子与基数
        self.fleet_direction = 1  # 方向乘子（"-1"表示向左移动）
        self.score_scale = 1.5  # 分数乘子
        self.alien_points = 50  # 分数基数
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        