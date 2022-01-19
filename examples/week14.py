import opc
import random
import time

leds = [(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

while True:
    for led in range(0,360,60):
        leds = [(255,255,255)]*360
        leds[led] = (0,0,255)
        leds[led+1] = (0,0,255)
        leds[led+2] = (0,0,255)
        leds[led+3] = (0,0,255)
        leds[led+4] = (0,0,255)
        if led == 255:
            led = 0
        client.put_pixels(leds)
        time.sleep(0.02)
