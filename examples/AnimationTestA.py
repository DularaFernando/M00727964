import opc
from time import sleep
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

for led in range(8,9):
    for rows in range(0,2):
        leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(0,9):
    for rows in range(2,3):
        leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)
