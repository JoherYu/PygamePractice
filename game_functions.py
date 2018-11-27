import sys
import pygame

from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """监视事件"""
    for event in pygame.event.get():
        # 退出游戏
        if event.type == pygame.QUIT:
            sys.exit()
            
        # 键盘事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
                
"""游戏操作标志更新"""
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:  # 创建新子弹并添加进子弹对象组
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
        
def update_screen(ai_settings, screen, ship, bullets):
    """重绘屏幕"""
    screen.fill(ai_settings.bg_color)
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()  # 显示飞船
    pygame.display.flip()
    