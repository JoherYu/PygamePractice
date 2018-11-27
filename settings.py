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
        # 外星人设置
        self.fleet_drop_speed = 10  # 外星人降落速度
        self.fleet_direction = 1  # 方向乘子（"-1"表示向左移动）
        # 飞船设置
        self.ship_limit = 3
        # 游戏元素速度设置
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 3