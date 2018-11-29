#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化游戏
    pygame.init()
    ai_settings = Settings()  #设置
    stats = GameStats(ai_settings)  # 游戏统计信息
    
    # 创建游戏屏幕对象及游戏元素
    screen = pygame.display.set_mode((ai_settings.screen_width, 
                                      ai_settings.screen_height))  #屏幕
    ship = Ship(ai_settings, screen)  #飞船
    play_button = Button(ai_settings, screen, "Play")  # 游戏按钮
    sb = Scoreboard(ai_settings, screen, stats)
    aliens = Group()  #外星人对象组
    bullets = Group()  # 子弹对象组
    
    gf.create_fleet(ai_settings,screen,aliens, ship)  # 创建(添加)外星人舰队
    
    pygame.display.set_caption("外星人入侵")
    
    # 游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, play_button, stats, 
                        aliens, sb)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship, 
                              stats, sb)
            gf.update_aliens(ai_settings, aliens, ship, bullets, screen, stats, 
                             sb)
        
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, 
                         play_button, stats, sb)
        
run_game()