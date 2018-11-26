#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
    # 初始化游戏
    pygame.init()
    ai_settings = Settings()  #设置
    
    # 创建游戏屏幕对象
    screen = pygame.display.set_mode((ai_settings.screen_width, 
                                      ai_settings.screen_height))  #屏幕
    ship = Ship(ai_settings, screen)  #飞船
    pygame.display.set_caption("外星人入侵")
    # 游戏主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        
run_game()