# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:37:01 2020

@author: Admin
"""

import pygame 

WHITE = (255, 255, 255)
RED   =(255, 0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

pygame.init()
(width, height) = (600,600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawer")

clock = pygame.time.Clock()

background = pygame.image.load("99.jpg")
background.convert()

ship = pygame.image.load("9494.jpg")
ship.convert()

ship = pygame.transform.scale(ship,(100,100))
ship.set_colorkey(WHITE)

backgroundMusic = pygame.mixer.music.load("555.mp3")
pygame.mixer.music.play(loops = -1)

ship_x = 250
ship_y = 500

running = True

rect_x = 0
rect_y = 0

x,y = pygame.mouse.get_pos()

while running:
    screen.blit(background,(0,0))
    screen.blit(ship,(ship_x,ship_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    (ship_x, ship_y) = pygame.mouse.get_pos()
    
             
        
    clock.tick(1)
    
    pygame.display.flip()
pygame.quit()

            
