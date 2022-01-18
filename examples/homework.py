import opc
import time
import random

leds = [(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

for led in range(60): #pick out indeces: led = 0,1,2,3...
    leds[led] = (255,0,0)
    time.sleep(.1)
    client.put_pixels(leds)

led=0

while led<60:
    leds[59-led] = (0,255,0)
    time.sleep(.1)
    client.put_pixels(leds)
    led = led + 1 #or reverse if you want

led=0
while led<60: #scroll all rows at the same time
    for rows in range(3): # 1st 3 lines to left from right
        leds[led+rows*60] = (0,0,255)
    for rows in range(3,6): #last3 lines to right from left
        leds[59-led+rows*60] = (100,100,255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1
