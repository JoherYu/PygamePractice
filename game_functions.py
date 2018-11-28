import sys
import pygame

from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ai_settings, screen, ship, bullets, play_button, stats, 
                 aliens):
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
        # 鼠标事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, 
                              ai_settings, screen, ship, aliens, bullets)
    
def check_play_button(stats, play_button, mouse_x, mouse_y, 
                      ai_settings, screen, ship, aliens, bullets):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    
    if button_clicked and not stats.game_active:  # 防止在游戏进行中重启游戏
        
        pygame.mouse.set_visible(False)  # 游戏开始后隐藏光标
        
        stats.reset_stats()  # 重置游戏统计信息
        stats.game_active = True  # 更改游戏状态标志
        
        aliens.empty()
        bullets.empty()
        
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()
        
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
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
        
def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats):
    """重绘屏幕"""
    screen.fill(ai_settings.bg_color)
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()  # 绘制飞船
    aliens.draw(screen)  # 绘制外星人
    
    if not stats.game_active:
        play_button.draw_button()
    
    pygame.display.flip()  # 刷新
    
def update_bullets(bullets, aliens, ai_settings, screen, ship):
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
    
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # 检查是否有子弹击中外星人，若有则删除相应对象
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 若外星人被全灭则创建新的外星人组并清空屏幕上的子弹
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)
            
def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建新子弹并添加进子弹对象组
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        
def create_fleet(ai_settings, screen, aliens, ship):
    alien = Alien(ai_settings, screen)  #不加入组中，只用来获得参数
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, 
                                  alien.rect.height)
    
    # 创建外星人对象组    
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,row_number)
        
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    
    # 计算外星人位置
    alien.rect.x = alien_width + 2 * alien_width * alien_number  
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.x = alien.rect.x # 外星人左右移动时的初始位置，若不设置则均为rect.x
    aliens.add(alien)
    
def get_number_aliens_x(ai_settings, alien_width):
    # 获取每行外星人数
    available_space_x = ai_settings.screen_width - 2 * alien_width# 每行可用空间
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x  
    
def get_number_rows(ai_settings, ship_height, alien_height):
    # 获取行数
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - 
                         ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    
def update_aliens(ai_settings, aliens, ship, bullets, screen, stats):
    # 更新外星人位置
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # 检查外星人是否与飞船相撞或是否有外星人到达屏幕底部
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, aliens, ship, bullets, screen, stats)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
    
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, aliens, ship, bullets, screen, stats)
            break
    
def ship_hit(ai_settings, aliens, ship, bullets, screen, stats):
    """相应飞船撞击事件"""
    if stats.ships_left > 0:
        # 可用飞船数减1
        stats.ships_left -= 1
        # 清空屏幕并将(新)飞船居中
        aliens.empty()
        bullets.empty()
        ship.center_ship()
        # 创建新外星人组
        create_fleet(ai_settings, screen, aliens, ship)
        # 失败画面的暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        
def check_fleet_edges(ai_settings, aliens):
    # 检查(标志)是否有(一个)外星人到达屏幕边缘
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
            
def change_fleet_direction(ai_settings, aliens):
    # 所有外星人下移后改变移动方向乘子
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1