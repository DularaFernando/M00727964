import turtle
import opc
import time
import random


delay = 0.1
score = 0
high_score = 0

wn = turtle.Screen() #creating a window screen
wn.title("Snake Game")
wn.bgcolor("yellow")

wn.setup(width=600, height=600)
wn.tracer(0) #turns automatic screen updates on or off and also sets the update()delay
