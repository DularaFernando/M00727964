import opc
from time import sleep
import random

leds = [(0 , 0 , 0)] * 360  # white
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


def E1( Y ):  # creating letter E for end
    for led in range(1 + Y , 5 + Y):
        for rows in range(1 , 2):
            leds[led + rows * 60] = (0 , 0 , 0)  # black
    client.put_pixels(leds)
    sleep(.01)
    for led in range(1 + Y , 2 + Y):
        for rows in range(1 , 6):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(1 + Y , 3 + Y):
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(1 + Y , 5 + Y):
        for rows in range(5 , 6):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)


def N1( Y ):  # creating letter N for end
    for led in range(6 + Y , 7 + Y):
        for rows in range(1 , 6):
            leds[led + rows * 60] = (0 , 0 , 0)  # black
    client.put_pixels(leds)
    sleep(.01)
    for led in range(7 + Y , 8 + Y):
        for rows in range(2 , 3):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(8 + Y , 9 + Y):
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(9 + Y , 10 + Y):
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(10 + Y , 11 + Y):
        for rows in range(1 , 6):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)


def D1( Y ):  # creating letter D for end
    for led in range(12 + Y , 15 + Y):
        for rows in range(1 , 2):
            leds[led + rows * 60] = (0 , 0 , 0)  # black
    client.put_pixels(leds)
    sleep(.01)
    for led in range(12 + Y , 15 + Y):
        for rows in range(5 , 6):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(13 + Y , 14 + Y):
        for rows in range(2 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(15 + Y , 16 + Y):
        for rows in range(2 , 3):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(16 + Y , 17 + Y):
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(15 + Y , 16 + Y):
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)


def row3():
    led = 0
    while led < 30:
        for rows in range(1 , 2):
            leds[59 - led + rows * 60] = (0 , 0 , 0)  # 2nd row from right to left led by led  #Black
            leds[led + rows * 60] = (0 , 0 , 0)  # 2nd row from left to right led by led
        for rows in range(3 , 4):
            leds[59 - led + rows * 60] = (0 , 0 , 0)  # 4th row from right to left led by led
            leds[led + rows * 60] = (0 , 0 , 0)  # 4th row from left to right led by led
        for rows in range(5 , 6):
            leds[59 - led + rows * 60] = (0 , 0 , 0)  # 6th row from right to left led by led
            leds[led + rows * 60] = (0 , 0 , 0)  # 6th row from left to right led by led

        for rows in range(0 , 1):
            leds[30 + led + rows * 60] = (0 , 0 , 0)  # 1st row from 30th led to right led by led
            leds[29 - led + rows * 60] = (0 , 0 , 0)  # 1st row from 29th led to left led by led
        for rows in range(2 , 3):
            leds[30 + led + rows * 60] = (0 , 0 , 0)  # 3rd row from 30th led to right led by led
            leds[29 - led + rows * 60] = (0 , 0 , 0)  # 3rd row from 29th led to left led by led
        for rows in range(4 , 5):
            leds[30 + led + rows * 60] = (0 , 0 , 0)  # 5th row from 30th led to right led by led
            leds[29 - led + rows * 60] = (0 , 0 , 0)  # 5th row from 29th led to left led by led
        client.put_pixels(leds)
        sleep(.05)
        led = led + 1

for led in range(353):
    leds[led] = (random.randint(0 , 255) , random.randint(0 , 255) ,
                 random.randint(0 , 255))  # start with purple but end with random colors
    leds[led + 1] = (125 , 25 , 255)
    leds[led + 3] = (125 , 25 , 255)
    leds[led + 4] = (125 , 25 , 255)
    leds[led + 6] = (125 , 25 , 255)
    leds[led + 7] = (125 , 25 , 255)

    client.put_pixels(leds)
    sleep(.01)
    led = led + 1

E1(4) , N1(6) , D1(8)
E1(31) , N1(33) , D1(35)
row3()
