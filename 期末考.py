# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 11:43:15 2020

@author: Admin
"""

import pygame


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

class Ball(pygame.sprite.Sprite):
    x = 0
    y = 0
    dx = 0
    dy = 0
    
    def __init__(self, ox, oy, radius, speedx, speedy):
        super().__init__()
        self.image = pygame.image.load("5252.jpg")
        self.image = pygame.transform.scale(self.image,(radius * 2, radius * 2))
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        self.rect.x = ox
        self.rect.y = oy
        
        self.dx = speedx
        self.dy = speedy
        self.x = ox
        self.y = oy
        
        
        
pygame.init()
ball = Ball(200, 200, 20, 5, 7)
ballGroup = pygame.sprite.Group()
ballGroup.add(ball)


clock = pygame.time.Clock()
size = [700, 600]
width = 700
hight = 600
screen = pygame.display.set_mode(size)

pygame.display.set_caption("")
done = False
score = 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawer")
clock = pygame.time.Clock()  



        
running = True
while running:
    
                
    ball.update()       
    ballGroup.draw(screen) 
                
                
    clock.tick(10)
    pygame.display.flip()
pygame.quit()