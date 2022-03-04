from time import sleep
import opc

leds = [(0 , 0 , 0)] * 360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


 # random iteration
led = 0
while led < 30:  # giving a range
    for rows in range(0 , 2):
        leds[59 - led + rows * 60] = (91 , 24 , 101)  # 1st 2 rows from right to left      # DarkOrchid
    for rows in range(0 , 2):
        leds[led + rows * 60] = (91 , 24 , 101)  # 1st 2 rows from left to right
    for rows in range(2 , 4):
        leds[29 - led + rows * 60] = (91 , 24 , 101)  # 3rd and 4th row from 29th led to left side
    for rows in range(2 , 4):
        leds[30 + led + rows * 60] = (91 , 24 , 101)  # 3rd and 4th row from 30th led to right side
    for rows in range(2 , 4):
        leds[59 - led + rows * 60] = (91 , 24 , 101)  # 3rd and 4th row from right to left
    for rows in range(2 , 4):
        leds[led + rows * 60] = (91 , 24 , 101)  # 3rd and 4th row from left to right
    for rows in range(4 , 6):
        leds[59 - led + rows * 60] = (91 , 24 , 101)  # last 2 rows from right to left
    for rows in range(4 , 6):
        leds[led + rows * 60] = (91 , 24 , 101)  # last 2 rows from left to right

    client.put_pixels(leds)
    sleep(.05)
    led = led + 1



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
    led = led + 2



led = 0
while led < 30:
    for rows in range(6):
        leds[59 - led + rows * 60] = (0 , 0 , 0)  # all 6 rows from right to left led by led
        leds[led + rows * 60] = (0 , 0 , 0)  # all 6 rows from left to right led by led

    client.put_pixels(leds)
    sleep(.05)
    led = led + 2

led = 1  # starting the animation by skipping a led
while led < 30:
    for rows in range(6):
        leds[59 - led + rows * 60] = (0 , 0 , 0)  # all 6 rows from right to left led by led
        leds[led + rows * 60] = (0 , 0 , 0)  # all 6 rows from left to right led by led

    client.put_pixels(leds)
    sleep(.05)
    led = led + 2


        
