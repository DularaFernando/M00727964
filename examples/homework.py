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

#while led<60:
 #   leds[59-led] = (0,255,0)
  #  time.sleep(.1)
  #  client.put_pixels(leds)
  #  led = led + 1 #or reverse if you want

led=59
while led>=0:
    leds[led] = (0,255,0)
    time.sleep(.1)
    client.put_pixels(leds)
    led = led-1
    

#led=0
#while led<60: #scroll all rows at the same time
  #  for rows in range(3): # 1st 3 lines to left from right
 #       leds[led+rows*60] = (0,0,255)
  #  for rows in range(3,6): #last3 lines to right from left
  #      leds[59-led+rows*60] = (100,100,255)
  #  client.put_pixels(leds)
  #  time.sleep(.1)
  #  led = led + 1

head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score :0 High Score : 0", align = "center",
          font =("candara", 24, "bold"))
