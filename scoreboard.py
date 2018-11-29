import pygame.font

from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    
    def __init__(self, ai_settings, screen, stats):
        # 必要属性
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # 记分板属性
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #创建记分板矩形
        self.prep_score()  # 得分
        self.prep_high_score()  # 最高分
        self.prep_level()  # 等级
        self.prep_ships()  # 飞船剩余
        
    def prep_score(self):
        # 图像创建
        rounded_score = round(self.stats.score, -1)  # 圆整分数
        score_str = "{:,}".format(rounded_score)  # 格式化分数
        self.score_image = self.font.render(score_str, True, self.text_color, 
                                            self.ai_settings.bg_color)
                                            
        # 放置记分板
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        # 图像创建
        high_score = round(self.stats.high_score, -1)  # 圆整分数
        high_score_str = "{:,}".format(high_score)  # 格式化分数
        self.high_score_image = self.font.render(high_score_str, True, 
                                    self.text_color, self.ai_settings.bg_color)
                                            
        # 放置记分板
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top =  self.score_rect.top
        
    def prep_level(self):
        # 图像创建
        self.level_image = self.font.render(str(self.stats.level), True, 
                                     self.text_color, self.ai_settings.bg_color)
                                            
        # 放置等级计数板
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)