# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:37:01 2020

@author: Admin
"""

import pygame 
import random


WHITE = (255, 255, 255)
RED   =(255, 0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

pygame.init()
millisecond = pygame.time.get_ticks()



(width, height) = (600,600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawer")

clock = pygame.time.Clock()

background = pygame.image.load("99.jpg")
background.convert()

ship = pygame.image.load("9052.png")
ship.convert()

ship = pygame.transform.scale(ship,(100,100))
ship.set_colorkey(WHITE)

backgroundMusic = pygame.mixer.music.load("555.mp3")
pygame.mixer.music.play(loops = -1)

font = pygame.font.Font(None, 50)


ship_x = 250
ship_y = 500

stoneList = []
for i in range(50):
    x = random.randint(0, width)
    y = random.randint(-600, 0)
    stoneList.append([x, y])

running = True
rect_x = 0
rect_y = 0

x,y = pygame.mouse.get_pos()


score = 0


while running:
    millisecond2 = pygame.time.get_ticks()
    second = (millisecond2 - millisecond)/1000
    print("Time : " + str(second))
    
    screen.blit(background,(0,0))
    # score display
    text = font.render("Score : " + str(score),True, RED)
    screen.blit(text,(ship_x, ship_y))
    text = font.render("millisecond : " + str(second),True, RED)
    screen.blit(text,(0, 0))
    
    
    
    screen.blit(ship,(ship_x,ship_y))
    
    
    for i in range(len(stoneList)):
        stoneList[i][1] = stoneList[i][1] + 1
        
        if stoneList[i][1] > 600:
            stoneList[i][0]= random.randint(0, width)
            stoneList[i][1] = random.randint(-600,0)
            
        
        
        pygame.draw.circle(screen, WHITE,(stoneList[i][0],stoneList[i][1]),10)
        stoneList[i][1]
    # detect coLLide 
    for i in range(len(stoneList)):
        if ((stoneList[i][0] <= ship_x) and (ship_x <=stoneList[i][0] + 30)
            and (stoneList[i][1] <= ship_y) and (ship_y <= stoneList[i][1] + 30)):
                score = score + 1
                print("Score : "+ str(score))
    
                                            
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    (ship_x, ship_y) = pygame.mouse.get_pos()
    
    if score > 100:
         text = font.render(" you win ",True, RED)
         screen.blit(text,(280, 280))
    
    
    
    
    
        
    
    clock.tick(5230)
    
    pygame.display.flip()
pygame.quit()

            
