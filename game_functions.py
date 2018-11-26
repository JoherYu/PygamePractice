import sys
import pygame

def check_events(ship):
    """监视事件"""
    for event in pygame.event.get():
        # 退出游戏
        if event.type == pygame.QUIT:
            sys.exit()
            
        # 移动(更改移动标志)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
                
def update_screen(ai_settings, screen, ship):
    # 重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()  # 显示飞船
    pygame.display.flip()
    
def check_keydown_events(event, ship):
    # 按下方向键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        
def check_keyup_events(event, ship):
    # 松开方向键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False