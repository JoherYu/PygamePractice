# 绘制飞船
import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # 将飞船放在屏幕底部居中
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)  # 飞船位置的小数值
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        
    # 显示飞船
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    # 根据移动标志移动飞船
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        self.rect.centerx = self.center  # 返回小数位置给位置变量