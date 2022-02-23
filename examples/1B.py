import opc
from time import sleep
import random

leds = [(0, 0, 0)] * 360  # white
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


while True:
    for led in range (113):
        leds = [(255,255,255)]*120
        leds[led] = (0,0,255)
        leds[led + 1] = (255,0,255)
        leds[led + 3] = (0,0,255)
        leds[led + 4] = (255,0,255)
        leds[led + 6] = (0,0,255)
        leds[led + 7] = (255,0,255)

     #   if leds == 255:
      #      leds = 0
        client.put_pixels(leds)
        sleep(.1)
        led = led + 1

    break
