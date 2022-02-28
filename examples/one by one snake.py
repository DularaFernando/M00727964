import opc
from time import sleep
import random

leds = [(0, 0, 0)] * 360  # white
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

leds = [(255, 255, 255)] * 360
for led in range(353):

    leds[led] = (0, 0, 0)
    leds[led + 1] = (255, 0, 255)
    leds[led + 3] = (0, 0, 255)
    leds[led + 4] = (255, 0, 255)
    leds[led + 6] = (0, 0, 255)
    leds[led + 7] = (255, 0, 255)

    client.put_pixels(leds)
    sleep(.05)
    led = led + 1


