import pygame.font

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
        self.prep_score()
        
    def prep_score(self):
        # 图像创建
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, 
                                            self.ai_settings.bg_color)
                                            
        # 放置记分板
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)