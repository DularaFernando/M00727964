import turtle
from time import sleep
import colorsys
import random
import opc

leds = [(0 , 0 , 0)] * 360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


led = 0
while led < 30:                                             # 
    for rows in range(0, 2):
        leds[59 - led + rows * 60] = (91, 24, 101)          # DarkOrchid #
    for rows in range(0, 2):                                # first three rows left to right
        leds[led + rows * 60] = (91, 24, 101)  
    for rows in range(2, 4):
        leds[29 - led + rows * 60] = (91, 24, 101)  
    for rows in range(2, 4):
        leds[30 + led + rows * 60] = (91, 24, 101)  
    for rows in range(2, 4):
        leds[59 - led + rows * 60] = (91, 24, 101)  
    for rows in range(2, 4):                                # first three rows left to right
        leds[led + rows * 60] = (91, 24, 101)               # 
    for rows in range(4, 6):
        leds[59 - led + rows * 60] = (91, 24, 101)          # 
    for rows in range(4, 6):                                # first three rows left to right
        leds[led + rows * 60] = (91, 24, 101)               #           # 
        
    client.put_pixels(leds)
    sleep(.05)
    led = led + 1


led = 0
while led < 30:                                             
    for rows in range(1, 2):
        leds[59 - led + rows * 60] = (0, 0, 0)              # 
        leds[led + rows * 60] = (0, 0, 0)                   # 
    for rows in range(3, 4):
        leds[59 - led + rows * 60] = (0, 0, 0)              # 
        leds[led + rows * 60] = (0, 0, 0)                   # 
    for rows in range(5, 6):
        leds[59 - led + rows * 60] = (0, 0, 0)              # 
        leds[led + rows * 60] = (0, 0, 0)                   # 
        
    for rows in range(0, 1):
        leds[30 + led + rows * 60] = (0, 0, 0)              # 
        leds[29 - led + rows * 60] = (0, 0, 0)              # 
    for rows in range(2, 3):
        leds[30 + led + rows * 60] = (0, 0, 0)              # 
        leds[29 - led + rows * 60] = (0, 0, 0)              # 
    for rows in range(4, 5):
        leds[30 + led + rows * 60] = (0, 0, 0)              # 
        leds[29 - led + rows * 60] = (0, 0, 0)              # 
    client.put_pixels(leds)
    sleep(.05)
    led = led + 2


led = 0
while led < 30:
    for rows in range(6):
        leds[59 - led + rows * 60] = (0, 0, 0)
        leds[led + rows * 60] = (0, 0, 0)

    client.put_pixels(leds)
    sleep(.03)
    led = led + 2
led = 1
while led < 30:
    for rows in range(6):
        leds[59 - led + rows * 60] = (0, 0, 0)
        leds[led + rows * 60] = (0, 0, 0)

    client.put_pixels(leds)
    sleep(.03)
    led = led + 2


        
