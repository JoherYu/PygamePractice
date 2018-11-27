import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        
        # 在(0,0)处创建子弹矩形
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # 设置子弹初始位置(小数)
        self.y = float(self.rect.y)
        
        # 其他设置
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    # 更新子弹位置
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    # 在屏幕上绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)