import opc
import time
import random

leds = [(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#for led in leds:
for led in range(60):
    leds[led] = (255,0,0)
    time.sleep(.1)
    client.put_pixels(leds)

led = 0
while led<60:
    leds[led] = (0,255,0)
    time.sleep(.1)
    client.put_pixels(leds)
    led = led + 1

#leds[0] = (255, 0, 0)

#time.sleep(3)
##client.put_pixels(leds)
#client.put_pixels(leds)

#leds[10+60] = (255, 0, 0)

#time.sleep(3)
#client.put_pixels(leds)
#client.put_pixels(leds)
    
led = 0
while x<60:
    leds[led] = (0,0,255)
    leds[led+60] = (0,0,255)
    leds[led+120] = (0,0,255)
    leds[led+180] = (0,0,255)
    leds[led+240] = (0,0,255)
    leds[led+300] = (0,0,255)
    

    client.put_pixels(leds)
    time.sleep(.1)
    x = x + 1
