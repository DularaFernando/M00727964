import opc
import time
import random

leds = [(0, 0, 0)] * 360  # white
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

led = 0
while led < 30:  # scroll all rows at the same time
    for rows in range(1, 2):
        leds[59 - led + rows * 60] = (91, 24, 101)  # midnight
    for rows in range(1, 2):  # first three rows left to right
        leds[led + rows * 60] = (91, 24, 101)  # midnight

    for rows in range(3, 4):
        leds[29 - led + rows * 60] = (91, 24, 101)  # midnight
    for rows in range(3, 4):
        leds[29 + led + rows * 60] = (91, 24, 101)  # midnight
    for rows in range(3, 4):
        leds[59 - led + rows * 60] = (91, 24, 101)  # midnight
    for rows in range(3, 4):  # first three rows left to right
        leds[led + rows * 60] = (91, 24, 101)  # midnight    

    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1
