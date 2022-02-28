import turtle
from time import sleep
import colorsys
import random
import opc

leds = [(0 , 0 , 0)] * 360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

def sadface2():
    for led in range(51 , 53):                                  
        for rows in range(2 , 3):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(54 , 56):  # oblack
        for rows in range(2 , 3):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(53 , 54):  # oblack
         for rows in range(3 , 4):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(51 , 56):  # oblack
         for rows in range(4 , 5):
            leds[led + rows * 60] = (225 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def snake():
    for led in range (113):
        leds = [(255,255,255)]*120
        leds[led] = (0,0,255)
        leds[led + 1] = (255,0,255)
        leds[led + 3] = (0,0,255)
        leds[led + 4] = (255,0,255)
        leds[led + 6] = (0,0,255)
        leds[led + 7] = (255,0,255)

        
