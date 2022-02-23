import opc
from time import sleep
import random

leds = [(0, 0, 0)] * 360  # white
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

for led in range(3 , 5):                                  
    for rows in range(2 , 3):
        leds[led + rows * 60] = (225 , 0 , 0)
client.put_pixels(leds)
sleep(.01)
for led in range(6 , 8):  # oblack
    for rows in range(2 , 3):
        leds[led + rows * 60] = (225 , 0 , 0)
client.put_pixels(leds)
sleep(.01)
for led in range(5 , 6):  # oblack
     for rows in range(3 , 4):
        leds[led + rows * 60] = (225 , 0 , 0)
client.put_pixels(leds)
sleep(.01)
for led in range(3 , 4):  # oblack
    for rows in range(3 , 4):
        leds[led + rows * 60] = (225 , 255 , 0)
client.put_pixels(leds)
sleep(.01)
for led in range(4 , 7):  # oblack
     for rows in range(4 , 5):
        leds[led + rows * 60] = (225 , 255 , 0)
client.put_pixels(leds)
sleep(.01)
for led in range(7 , 8):  # oblack
    for rows in range(3 , 4):
        leds[led + rows * 60] = (225 , 255 , 0)
client.put_pixels(leds)
sleep(.01)

#sadface

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
for led in range(51 , 52):  # oblack
    for rows in range(3 , 4):
        leds[led + rows * 60] = (225 , 255 , 0)
client.put_pixels(leds)
sleep(.01)
for led in range(52 , 55):  # oblack
     for rows in range(4 , 5):
        leds[led + rows * 60] = (225 , 255 , 0)
client.put_pixels(leds)
sleep(.01)
for led in range(55 , 56):  # oblack
    for rows in range(3 , 4):
        leds[led + rows * 60] = (225 , 255 , 0)
client.put_pixels(leds)
sleep(.01)
