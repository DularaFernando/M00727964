import opc
from time import sleep
import math
import random

leds = [(255, 255, 255)] * 360
client = opc.Client('localhost:7890')

client.put_pixels(leds)
client.put_pixels(leds)


def blackout_line(x):
    for column in range(0, 60):
        for rows in range(0, x):
            leds[column + rows * 60] = (0, 0, 0)  # Black
    client.put_pixels(leds)
    sleep(0.1)


def snake():
    snake_run = True
    x1 = 60
    x2 = 1

    leds = [(255, 255, 255)] * 360  # background color

    for led in range(353):
        print(x1, led, x2)
        if led >= x1:
            for column in range(0, 60):
                for rows in range(0, x2):
                    leds[column + rows * 60] = (0, 0, 0)  # Black
            client.put_pixels(leds)
            sleep(0.1)
            x1 = x1 + 60
            x2 = x2 + 1

        elif led >= 350:
            led = 0

        else:
            leds[led-1] = (255, 255, 255) # -1 fix the color error on the 1st led
            leds[led + 1] = (255, 0, 255)
            leds[led + 3] = (0, 0, 255)
            leds[led + 4] = (255, 0, 255)
            leds[led + 6] = (0, 0, 255)
            leds[led + 7] = (255, 0, 255)

            client.put_pixels(leds)
            sleep(0.1)
            led + 1



snake()
