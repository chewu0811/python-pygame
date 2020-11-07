# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame
import random

num = random.randint(1,100)
print(num)

minNum = 1
maxNum = 100
right = False


while not right:
    guess = input ("Enter a number between"+str(minNum)+"~"+str(maxNum) )
    if str(num) == guess:
        print("Right")
        right = True
    elif int(guess) < num and int (guess) > minNum:
        minNum = int(guess)
        
    elif int(guess) > num and int (guess) < maxNum:
        maxNum = int(guess)
        
    else:
        print("Enter another number")
        
    
