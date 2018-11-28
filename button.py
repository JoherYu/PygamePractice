import pygame.font

class Button():
    
    def __init__(self, ai_settings,screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 按钮设置
        self.width, self.height = 200, 50
        self.button_color = (225, 225, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        # 创建按钮
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)  # 标签
        
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, 
                                          self.button_color)  # 渲染为图像
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)  # 绘制按钮
        self.screen.blit(self.msg_image, self.msg_image_rect)