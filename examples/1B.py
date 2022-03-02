import opc
from time import sleep
import random

leds = [(0, 0, 0)] * 360  # white
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


def sadface1(x):
    for led in range(3+x , 5+x):                                  
        for rows in range(2 , 3):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(6+x , 8+x):                 # oblack
        for rows in range(2 , 3):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(5+x , 6+x):                 # oblack
         for rows in range(3 , 4):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(3+x , 8+x):                 # oblack
         for rows in range(4 , 5):
            leds[led + rows * 60] = (225 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

