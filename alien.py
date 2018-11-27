import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 载入外星人图像并设置rect属性
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        
        # 设置外星人起始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)  # 小数
        
    # 显示外星人
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    # 外星人的移动
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * 
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
    # 检查是否触及边缘并设置边缘检查标志
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:  
            return True
        elif self.rect.left <= 0:
            return True
        