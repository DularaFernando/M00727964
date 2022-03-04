from time import sleep
import opc

leds = [(0 , 0 , 0)] * 360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

leds = [(125, 225, 0)] *360                 #all leds to neon green
for led in range (173):                     #from left to right make the OPC screen black in first 3 lines
    leds[led] = (0,0,0)
    leds[led + 1] = (255,0,255)
    leds[led + 3] = (0,0,255)
    leds[led + 4] = (255,0,255)
    leds[led + 6] = (0,0,255)
    leds[led + 7] = (255,0,255)

    client.put_pixels(leds)
    sleep(.025)
    led = led + 1

for led in range (180):                     #from right to left make the OPC screen black in last 3 lines
    leds[352-led] = (0,0,255)
    leds[352-led + 1] = (255,0,255)
    leds[352-led + 3] = (0,0,255)
    leds[352-led + 4] = (255,0,255)
    leds[352-led + 6] = (0,0,255)
    leds[352-led + 7] = (0,0,0)

    client.put_pixels(leds)
    sleep(.025)
    led = led + 1