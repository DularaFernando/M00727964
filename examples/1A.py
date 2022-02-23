
import opc
from time import sleep
import colorsys

client = opc.Client('localhost:7890')
leds = [(255,255,0)]*360

for led in range(300, 360):  # pick out indeces: led = 0,1,2,3...
    leds[led] = (225, 0, 0) #bdazzled blue
    sleep(.001)
    client.put_pixels(leds)
        
     
