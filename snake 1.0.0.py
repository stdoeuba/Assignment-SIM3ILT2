# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:49:02 2020
Home Assignment - SIM3IL 
Programmming the game snake
@author: domin
"""
    #adding bibs
from turtle import *
from random import randrange
from freegames import square, vector


    #adding vectors
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

    #Change snake direction
def change(x, y):
   
    aim.x = x
    aim.y = y
    
    #Return True if head inside boundary values
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190
    
    #Move snake forward one segment
def move():
    head = snake[-1].copy()             #moves snake
    head.move(aim)

    if not inside(head) or head in snake:  #conditions: if the head hits the boundary it is out, if snake hits itself it is out"
        square(head.x, head.y, 9, 'red')   #"additional square in red if conditions are outside the boundaries"
        update()
        return

    snake.append(head)                   # "if conditions are within the boundaries "

    if head == food:                        #"condition if the head meets food"
        print('Snake:', len(snake))         #"prints length of the current snake"
        food.x = randrange(-15, 15) * 10    #"random food location in x direction"
        food.y = randrange(-15, 15) * 10   # "random food location in y direction"
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 100)


hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()