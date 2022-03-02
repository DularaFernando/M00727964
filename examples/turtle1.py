#-----------------------------------------------------------------------------------------------------------------------------------------------
#import libraries
import turtle
from time import sleep
import colorsys
import random
import opc

leds = [(0 , 0 , 0)] * 360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

s = 1.0  # maximum colour
v = 1.0  # maximum brightness
#------------------------------------------------------------------------------------------------------------------------------------------------
#creating the turtle game
player_one = turtle.Turtle()                   #creating player 1    
player_one.color("green")                      #giving a color to player 1
player_one.shape("turtle")                     #giving a shape to player 1
player_one.penup()                             #giving a position
player_one.goto(-200, 100)

player_two = player_one.clone()                #creating player 2, as I am cloning no need to give a shape
player_two.color("blue")
player_two.penup()
player_two.goto(-200 , -100)


player_one.goto(200 , 60)                      #creating the finishing circle for player 1
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200 , 100)
player_two.goto(200 , -140)
player_two.pendown()                           #creating the finishing circle for player 2
player_two.circle(40)
player_two.penup()
player_two.goto(-200 , -100)

dice = random.randint(1 , 6)                   #using random library to get a random number from 1 to 6
dice_outcome = dice                            
print('Starting roll:'),print(dice)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#creating letters
def P():                                       #creating letter P
    for led in range(0 , 1):
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(1 , 3):                 
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(2 , 3):                 
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(1 , 2):                 
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)


def L(x):                                        #creating letter L
    for led in range(4+x , 5+x):                 
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(5+x , 7+x):                 
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)


def A(x):                                        #creating letter A
    for led in range(8+x , 9+x):                 
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(9+x , 12+x):                
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(10+x , 11+x):               
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(12+x , 13+x):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)


def Y():                                         #creating letter Y
    for led in range(14 , 15):               
        for rows in range(2 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(15 , 16):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(16 , 17):               
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(15 , 16):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)


def E(x):                                        #creating letter E
    for led in range(18+x , 21+x):               
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(18+x , 20+x):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(18+x , 21+x):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)


def R(x):                                        #creating letter R
    for led in range(22+x , 25+x):               
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(22+x , 24+x):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(22+x , 23+x):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(24+x , 25+x):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)


def ONE():                                       #creating number 1
    for led in range(28 , 31):               
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 200 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(29 , 30):               
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 200 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(28 , 31):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 200 , 0)
    client.put_pixels(leds)
    sleep(.01)


def W():                                         #creating letter W
    for led in range(33 , 34):              
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(34 , 35):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(38 , 39):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(36 , 37):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(35 , 36):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(37 , 38):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(39 , 40):               
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def S():                                         #creating letter S
    for led in range(51 , 54):               
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(52 , 53):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(51 , 54):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def TWO():                                       #creating number 2
    for led in range(28 , 32):               
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 255)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(29 , 31):               
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 255)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(28 , 32):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 255)
    client.put_pixels(leds)
    sleep(.01)
    
def N(x):                                       #creating letter N
    for led in range(10+x , 11+x):               
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(11+x , 12+x):               
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(12+x , 13+x):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(13+x , 14+x):               
        for rows in range(3 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(14+x , 15+x):               
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    
def I(x):                                        #creating letter I
    for led in range(16+x , 19+x):               
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(17+x , 18+x):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(16+x , 19+x):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    
def C():                                         #creating letter C
    for led in range(20 , 24):               
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(20 , 21):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(20 , 24):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def O(x):                                        #creating letter O
    for led in range(29+x , 31+x):               
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(28+x , 29+x):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(31+x , 32+x):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(29+x , 31+x):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def B():                                         #creating letter B
    for led in range(10 , 11):               
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(11 , 12):               
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(12 , 13):               
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def DForBad():                                   #creating letter D
    for led in range(20 , 23):               
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(21 , 22):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(20 , 23):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(23 , 24):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def E1(Y):                                       #creating letter E at last
    for led in range(1+Y , 5+Y):               
        for rows in range(1 , 2):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(1+Y , 2+Y):               
        for rows in range(1 , 6):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)    
    for led in range(1+Y , 3+Y):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(1+Y , 5+Y):               
        for rows in range(5 , 6):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)

def N1(Y):                                        #creating letter N at last
    for led in range(6+Y , 7+Y):               
        for rows in range(1 , 6):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(7+Y , 8+Y):               
        for rows in range(2 , 3):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(8+Y , 9+Y):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(9+Y , 10+Y):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(10+Y , 11+Y):               
        for rows in range(1 , 6):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)

def D1(Y):                                       #creating letter D at last
    for led in range(12+Y , 15+Y):               
        for rows in range(1 , 2):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(12+Y , 15+Y):               
        for rows in range(5 , 6):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(13+Y , 14+Y):               
        for rows in range(2 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(15+Y , 16+Y):               
        for rows in range(2 , 3):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(16+Y , 17+Y):               
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(15+Y , 16+Y):               
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)

def smileface(x):                               #creating the smile face
    for led in range(3+x , 5+x):                                  
        for rows in range(2 , 3):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(6+x , 8+x):                 
        for rows in range(2 , 3):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(5+x , 6+x):                 
         for rows in range(3 , 4):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(3+x , 4+x):                 
        for rows in range(3 , 4):
            leds[led + rows * 60] = (225 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(4+x , 7+x):                 
         for rows in range(4 , 5):
            leds[led + rows * 60] = (225 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(7+x , 8+x):                 
        for rows in range(3 , 4):
            leds[led + rows * 60] = (225 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def sadface(x):                                  #creating the sad face
    for led in range(3+x , 5+x):                                  
        for rows in range(2 , 3):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(6+x , 8+x):                 
        for rows in range(2 , 3):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(5+x , 6+x):                 
         for rows in range(3 , 4):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(3+x , 8+x):                 
         for rows in range(4 , 5):
            leds[led + rows * 60] = (225 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
#------------------------------------------------------------------------------------------------------------------------------------------------
#creating different animations 
def snake1():                                   #create the 1st snake animation
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

def snake2():                                   #create the 2nd snake animation
    for led in range (353):
        leds[led] = (random.randint(0 , 255) ,random.randint(0 , 255) ,random.randint(0 , 255) ) #start with purple but end with random colors
        leds[led + 1] = (125,25,255)
        leds[led + 3] = (125,25,255)
        leds[led + 4] = (125,25,255)
        leds[led + 6] = (125,25,255)
        leds[led + 7] = (125,25,255)

        client.put_pixels(leds)
        sleep(.01)
        led = led + 1
        
def rainbow_1_1():
    for hue in range(120):
        rgb_fractional = colorsys.hsv_to_rgb(random.randint(hue - 10 , hue + 10) / 360.0 , s , v)  # colorsys returns floats between 0 and 1
        r_float = rgb_fractional[0]  # extract said floating point numbers
        g_float = rgb_fractional[1]
        b_float = rgb_fractional[2]

        rgb = (r_float * 255 , g_float * 255 , b_float * 255)  # make new tuple with corrected values
        leds[hue] = rgb
        client.put_pixels(leds)  # send out

        sleep(0.01)  # 20ms

def rainbow_2_1():
    for hue in range(120):
        rgb_fractional = colorsys.hsv_to_rgb(hue / 360.0 , s , v)  # colorsys returns floats between 0 and 1
        r_float = rgb_fractional[0]  # extract said floating point numbers
        g_float = rgb_fractional[1]
        b_float = rgb_fractional[2]

        rgb = (r_float * 255 , g_float * 255 , b_float * 255)  # make new tuple with corrected values
        client.put_pixels([rgb] * 120)  # send out

        sleep(0.01)  # 20ms

def rainbow_2_2():
    for hue in range(300 , 360):
        rgb_fractional = colorsys.hsv_to_rgb(random.randint(hue - 10 , hue + 10) / 360.0 , s ,v)  # colorsys returns floats between 0 and 1
        r_float = rgb_fractional[0]  # extract said floating point numbers
        g_float = rgb_fractional[1]
        b_float = rgb_fractional[2]

        rgb = (r_float * 255 , g_float * 255 , b_float * 255)  # make new tuple with corrected values
        leds[hue] = rgb
        client.put_pixels(leds)  # send out

        sleep(0.01)  # 20ms

def row():
    led = 0
    while led < 30:  # scroll all rows at the same time
        for rows in range(0, 2):
            leds[59 - led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(0, 2):  # first three rows left to right
            leds[led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(2, 4):
            leds[29 - led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(2, 4):
            leds[29 + led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(2, 4):
            leds[59 - led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(2, 4):  # first three rows left to right
            leds[led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(4, 6):
            leds[59 - led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(4, 6):  # first three rows left to right
            leds[led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(2, 4):
            leds[29 - led + rows * 60] = (91, 24, 101)  # midnight
        
        client.put_pixels(leds)
        sleep(.05)
        led = led + 1

def row1():
    led = 0
    while led < 30:  # scroll all rows at the same time
        for rows in range(1, 2):
            leds[59 - led + rows * 60] = (0, 0, 0)  # midnight # first three rows left to right
            leds[led + rows * 60] = (0, 0, 0)  # midnight
        for rows in range(3, 4):
            leds[59 - led + rows * 60] = (0, 0, 0)  # midnight  # first three rows left to right
            leds[led + rows * 60] = (0, 0, 0)  # midnight
        for rows in range(5, 6):
            leds[59 - led + rows * 60] = (0, 0, 0)  # midnight # first three rows left to right
            leds[led + rows * 60] = (0, 0, 0)  # midnight
        
        for rows in range(0, 1):
            leds[30 + led + rows * 60] = (0, 0, 0)  # midnight# first three rows left to right
            leds[29 - led + rows * 60] = (0, 0, 0)  # midnight
        for rows in range(2, 3):
            leds[30 + led + rows * 60] = (0, 0, 0)  # midnight# first three rows left to right
            leds[29 - led + rows * 60] = (0, 0, 0)  # midnight
        for rows in range(4, 5):
            leds[30 + led + rows * 60] = (0, 0, 0)  # midnight # first three rows left to right
            leds[29 - led + rows * 60] = (0, 0, 0)  # midnight
        client.put_pixels(leds)
        sleep(.05)
        led = led + 2

def row2():
    led = 0
    while led < 30:
        for rows in range(6):
            leds[59 - led + rows * 60] = (0, 0, 0)
            leds[led + rows * 60] = (0, 0, 0)

        client.put_pixels(leds)
        sleep(.03)
        led = led + 2
    led = 1
    while led < 30:
        for rows in range(6):
            leds[59 - led + rows * 60] = (0, 0, 0)
            leds[led + rows * 60] = (0, 0, 0)

        client.put_pixels(leds)
        sleep(.03)
        led = led + 2

def row3():
    led = 0
    while led < 30:
        for rows in range(3,6):
            leds[59 - led + rows * 60] = (0, 0, 0)
            leds[led + rows * 60] = (0, 0, 0)

        client.put_pixels(leds)
        sleep(.03)
        led = led + 2
    led = 1
    while led < 30:
        for rows in range(3,6):
            leds[59 - led + rows * 60] = (0, 0, 0)
            leds[led + rows * 60] = (0, 0, 0)

        client.put_pixels(leds)
        sleep(.03)
        led = led + 2

def row4():
    led = 0
    while led < 30:  # scroll all rows at the same time
        for rows in range(5,6):
            leds[59 - led + rows * 60] = (0 ,random.randint(0 , 125) ,random.randint(0 , 255) )  # midnight # first three rows left to right
            leds[led + rows * 60] = (0 ,0 ,random.randint(0 , 155) )  # midnight
        client.put_pixels(leds)
        sleep(.01)
        led = led + 2

def row5():
    led = 0
    while led < 30:  # scroll all rows at the same time
        for rows in range(5,6):
            leds[29 - led + rows * 60] = (random.randint(0 , 255) ,random.randint(0 , 125) ,0 )  # midnight # first three rows left to right
            leds[29 + led + rows * 60] = (random.randint(0 , 155) ,0 ,random.randint(0 , 125) )  # midnight
        client.put_pixels(leds)
        sleep(.01)
        led = led + 1

for i in range(20):
    if player_one.pos() >= (200 , 100):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (200 , -100):
        print("Player Two Wins!")
        break
    elif dice_outcome >= 4:
        leds = [(0 , 0 , 0)]*360
        for led in range(60):  # pick out indeces: led = 0,1,2,3...
            leds[led] = (44, 87, 132) #bdazzled blue
            sleep(.001)
            client.put_pixels(leds)

            leds[119 - led] = (44, 87, 132) #bdazzled blue
            sleep(.001)
            client.put_pixels(leds)
        smileface(0), row4(), smileface(48)
        N(0)
        I(0)
        C()
        E(7)
        R(10)
        O(7)
        L(36)
        L(40)

        dice = random.randint(1 , 6)  # 6-sides dice random
        player_one_turn = input("Press 'Enter' to roll the die ")
        dice_outcome = dice
        print("The Player 1 result of the die roll is: ")
        print(dice_outcome)
        print("The number of Player 1 steps will be: ")
        print(20 * dice_outcome)
        player_one.fd(20 * dice_outcome)
        player_two_turn = input("Press 'Enter' to roll the die ")
        dice = random.randint(1 , 6)
        dice_outcome = dice
        print("The Player 2 result of the die roll is: ")             
        print(dice_outcome)
        print("The number Player 2 of steps will be: ")
        print(20 * dice_outcome)
        player_two.fd(20 * dice_outcome)


    else:        
        leds = [(0 , 0 , 0)]*360
        for led in range(60):  # pick out indeces: led = 0,1,2,3...
            leds[led] = (225, 0, 0) #bdazzled blue
            sleep(.001)
            client.put_pixels(leds)

            leds[119 - led] = (225, 0, 0) #bdazzled blue
            sleep(.001)
            client.put_pixels(leds)
        sadface(0), row5(), sadface(47)
        B()
        A(6)
        DForBad()
        R(10)
        O(7)
        L(36)
        L(40)
        
        dice = random.randint(1 , 6)  # 6-sides dice random
        player_one_turn = input("Press 'Enter' to roll the die ")
        dice_outcome = dice
        print("The Player 1 result of the die roll is: ")
        print(dice_outcome)
        print("The number of Player 1 steps will be: ")
        print(20 * dice_outcome)
        player_one.fd(20 * dice_outcome)
        player_two_turn = input("Press 'Enter' to roll the die ")
        dice = random.randint(1 , 6)
        dice_outcome = dice
        print("The Player 2 result of the die roll is: ")
        print(dice_outcome)
        print("The number of Player 2 steps will be: ")
        print(20 * dice_outcome)
        player_two.fd(20 * dice_outcome)
        sleep(.1)


# Animation ===========================================================================================================
if player_one.pos() >= (200 , 100):  
    leds = [(0 , 0 , 0)]*360
    rainbow_1_1()
    P(), L(0), A(0), Y(), E(0), R(0)
    ONE()
    W(), I(25), N(35), S()
    rainbow_2_2()
    leds = [(0 , 0 , 0)]*360
    row(), row1(), row2()
    snake1()
    snake2()
    E1(1), N1(3), D1(5)
    E1(31), N1(33), D1(35)

else:
    player_two.pos() >= (200 , -100)
    leds = [(0 , 0 , 0)]*360
    rainbow_2_1()
    P(), L(0), A(0), Y(), E(0), R(0)
    TWO()
    W(), I(25), N(35), S()
    rainbow_2_2()
    leds = [(0 , 0 , 0)]*360
    row(), row1(), row2()
    snake1()
    snake2()
    E1(1), N1(3), D1(5)
    E1(31), N1(33), D1(35)


# Animation Player  Win ================================================================================================

