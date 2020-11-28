# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 09:11:15 2020

@author: Admin
"""



import pygame
import random


WHITE = (255, 255, 255)
RED   =(255, 0, 0)
GREEN = (0, 255,0)
BLACK = (0, 0, 0)



class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
class Apple(pygame.sprite.Sprite):
    def __init__(self, picturePath, width, height):
        super().__init__()
        self.image = pygame.image.load(picturePath)      
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
        
        
pygame.init()
(width, height) = (600, 600)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawer")
clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()




apple = Apple("9052.png", 100, 100)
all_apple_list = pygame.sprite.Group()
all_apple_list.add(apple)
all_apple_list.draw(screen)

for i in range(30):
    block = Block(BLACK, 30, 50)
    block.rect.x = random.randint(0, width -20)
    block.rect.y = random.randint(0, height -20)
    


    print(block.rect.x)
    print(block.rect.y)
    print(block.rect.width)
    print(block.rect.height)

    
    all_sprites_list.add(block)
score = 0

font = pygame.font.Font(None, 50)
running = True
while running:
    screen.fill(RED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    hit_list = pygame.sprite.spritecollide(apple, all_sprites_list, True)        
    if len(hit_list) > 0:
        score = score + 1
        print("Score : " + str(score))   
            
    if score > 40:
        running = False      
    if score >40:       
        running = True  
            
            
    (apple_x,apple_y) = pygame.mouse.get_pos()
    apple.rect.x = apple_x       
    apple.rect.y = apple_y       
    
    
    for sprite in all_sprites_list.sprites():
        sprite.rect.x = random.randint(0, width -20)
        sprite.rect.y = random.randint(0, height -20)
        
        if score >10:
             text = font.render(" you win ",True, BLACK)
             screen.blit(text,(280, 280))
            
    all_sprites_list.draw(screen) 
    all_apple_list.draw(screen)      
    clock.tick(30)
    pygame.display.flip()
pygame.quit()

