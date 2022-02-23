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

player_one = turtle.Turtle()  # C
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200 , 100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200 , -100)

player_one.goto(200 , 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200 , 100)
player_two.goto(200 , -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200 , -100)

dice = random.randint(1 , 6)
dice_outcome = dice
print('Starting roll:'),print(dice)


# =========================================Def of Letters and Numbers==============================================================
def P():
    for led in range(0 , 1):
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(1 , 3):  # p
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(2 , 3):  # p
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(1 , 2):  # p
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)


def L():
    for led in range(4 , 5):  # L
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(5 , 7):  # L
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)


def A():
    for led in range(8 , 9):  # A
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(9 , 12):  # A
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(10 , 11):  # A
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(12 , 13):  # A
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)


def Y():
    for led in range(14 , 15):  # Y
        for rows in range(2 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(15 , 16):  # Y
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(16 , 17):  # Y
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(15 , 16):  # Y
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)


def E():
    for led in range(18 , 21):  # E
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(18 , 20):  # E
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(18 , 21):  # E
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)


def R():
    for led in range(22 , 25):  # R
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(22 , 24):  # R
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(22 , 23):  # R
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(24 , 25):  # R
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)


def ONE():
    for led in range(28 , 31):  # 1
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 200 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(29 , 30):  # 1
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 200 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(28 , 31):  # 1
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 200 , 0)
    client.put_pixels(leds)
    sleep(.01)


def W():
    for led in range(33 , 34):  # W
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(34 , 35):  # W
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(38 , 39):  # W
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(36 , 37):  # W
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(35 , 36):  # W
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(37 , 38):  # W
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(39 , 40):  # W
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)


def I():
    for led in range(41 , 44):  # I
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(42 , 43):  # I
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(41 , 44):  # I
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)


def N():
    for led in range(45 , 46):  # N
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(46 , 47):  # N
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(47 , 48):  # N
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(48 , 49):  # N
        for rows in range(3 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(49 , 50):  # N
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def S():
    for led in range(51 , 54):  # S
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(52 , 53):  # S
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(51 , 54):  # S
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def TWO():
    for led in range(28 , 32):  # 2
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 255)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(29 , 31):  # 2
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 255)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(28 , 32):  # 2
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 255)
    client.put_pixels(leds)
    sleep(.01)
    
def N1():
    for led in range(10 , 11):  # N
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(11 , 12):  # N
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(12 , 13):  # N
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(13 , 14):  # N
        for rows in range(3 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(14 , 15):  # N
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    
def I1():
    for led in range(16 , 19):  # I
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(17 , 18):  # I
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(16 , 19):  # I
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    
def C1():
    for led in range(20 , 24):  # I
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(20 , 21):  # I
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(20 , 24):  # I
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def E3():
    for led in range(25 , 28):  # I
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(25 , 27):  # I
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(25 , 28):  # I
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def O1():
    for led in range(29 , 31):  # E
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(28 , 29):  # E
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(32 , 33):  # E
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(29 , 31):  # E
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    
def R1():
    for led in range(32 , 33):  # E
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(33 , 35):  # E
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(33 , 34):  # E
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(34 , 35):  # E
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def O():                                                  
    for led in range(36 , 37):                                  
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(37 , 38):  # E
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(38 , 39):  # E
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(37 , 38):  # E
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def L1():                                                    
    for led in range(40 , 41):                                  
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(41 , 43):  # E
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def L2():                                                     
    for led in range(44 , 45):                                  
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(45 , 47):  # E
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def B():
    for led in range(10 , 11):  # N
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(11 , 12):  # N
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(12 , 13):  # N
        for rows in range(2 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def AForBad():
    for led in range(14 , 15):  # A
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(15 , 18):  # A
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(16 , 17):  # A
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(18 , 19):  # A
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def DForBad():
    for led in range(20 , 23):  # A
        for rows in range(2 , 3):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(21 , 22):  # A
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(20 , 23):  # A
        for rows in range(4 , 5):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(23 , 24):  # A
        for rows in range(3 , 4):
            leds[led + rows * 60] = (255 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def AForBad1():
    for led in range(14 , 15):  # A
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(15 , 18):  # A
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(16 , 17):  # A
        for rows in range(2 , 3):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(18 , 19):  # A
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)

def B1():
    for led in range(10 , 11):  # N
        for rows in range(2 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(11 , 12):  # N
        for rows in range(2 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(12 , 13):  # N
        for rows in range(2 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)

def DForBad1():
    for led in range(20 , 23):  # A
        for rows in range(2 , 3):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(21 , 22):  # A
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(20 , 23):  # A
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(23 , 24):  # A
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)

def n():
    for led in range(10 , 11):  # Nblack
        for rows in range(2 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(11 , 12):  # Nblack
        for rows in range(2 , 3):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(12 , 13):  # Nblack
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(13 , 14):  # Nblack
        for rows in range(3 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(14 , 15):  # Nblack
        for rows in range(2 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    
def i1():
    for led in range(16 , 19):  # Iblack
        for rows in range(2 , 3):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(17 , 18):  # Iblack
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(16 , 19):  # Iblack
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    
def c1():
    for led in range(20 , 24):  # Cblack
        for rows in range(2 , 3):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(20 , 21):  # Cblack
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(20 , 24):  # Cblack
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)

def e3():
    for led in range(25 , 28):  # Eblack
        for rows in range(2 , 3):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(25 , 27):  # Eblack
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(25 , 28):  # Eblack
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)

def o1():
    for led in range(29 , 31):  # oblack
        for rows in range(2 , 3):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(28 , 29):  # oblack
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(32 , 33):  # oblack
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(29 , 31):  # oblack
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    
def r():
    for led in range(32 , 33):  # rblack
        for rows in range(2 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(33 , 35):  # rblack
        for rows in range(2 , 3):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(33 , 34):  # rblack
        for rows in range(3 , 4):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(34 , 35):  # rblack
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)

def o():
    for led in range(36 , 37):                                  
        for rows in range(2 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(37 , 38):  # oblack
        for rows in range(2 , 3):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(38 , 39):  # oblack
        for rows in range(2 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(37 , 38):  # oblack
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)

def l1():
    for led in range(40 , 41):                                  
        for rows in range(2 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(41 , 43):  # lblack
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)

def l2():
    for led in range(44 , 45):                                  
        for rows in range(2 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(45 , 47):  # lblack
        for rows in range(4 , 5):
            leds[led + rows * 60] = (0 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)

def smileface1():
    for led in range(3 , 5):                                  
        for rows in range(2 , 3):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(6 , 8):  # oblack
        for rows in range(2 , 3):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(5 , 6):  # oblack
         for rows in range(3 , 4):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(3 , 4):  # oblack
        for rows in range(3 , 4):
            leds[led + rows * 60] = (225 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(4 , 7):  # oblack
         for rows in range(4 , 5):
            leds[led + rows * 60] = (225 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(7 , 8):  # oblack
        for rows in range(3 , 4):
            leds[led + rows * 60] = (225 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

def smileface2():
    for led in range(51 , 53):                                  
        for rows in range(2 , 3):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(54 , 56):  # oblack
        for rows in range(2 , 3):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(53 , 54):  # oblack
         for rows in range(3 , 4):
            leds[led + rows * 60] = (225 , 0 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(51 , 52):  # oblack
        for rows in range(3 , 4):
            leds[led + rows * 60] = (225 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(52 , 55):  # oblack
         for rows in range(4 , 5):
            leds[led + rows * 60] = (225 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)
    for led in range(55 , 56):  # oblack
        for rows in range(3 , 4):
            leds[led + rows * 60] = (225 , 255 , 0)
    client.put_pixels(leds)
    sleep(.01)

# ====================================Def of rainbows==================================================================
def rainbow_1_1():
    for hue in range(120):
        rgb_fractional = colorsys.hsv_to_rgb(random.randint(hue - 10 , hue + 10) / 360.0 , s , v)  # colorsys returns floats between 0 and 1
        r_float = rgb_fractional[0]  # extract said floating point numbers
        g_float = rgb_fractional[1]
        b_float = rgb_fractional[2]

        rgb = (r_float * 255 , g_float * 255 , b_float * 255)  # make new tuple with corrected values
        leds[hue] = rgb
        client.put_pixels(leds)  # send out

        sleep(0.03)  # 20ms

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
        for rows in range(1, 2):
            leds[59 - led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(1, 2):  # first three rows left to right
            leds[led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(3, 4):
            leds[29 - led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(3, 4):
            leds[29 + led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(3, 4):
            leds[59 - led + rows * 60] = (91, 24, 101)  # midnight
        for rows in range(3, 4):  # first three rows left to right
            leds[led + rows * 60] = (91, 24, 101)  # midnight
        
        client.put_pixels(leds)
        sleep(.1)
        led = led + 1

def row1():
    led = 0
    while led < 30:  # scroll all rows at the same time
        for rows in range(1, 2):
            leds[59 - led + rows * 60] = (0, 0, 0)  # midnight
        for rows in range(1, 2):  # first three rows left to right
            leds[led + rows * 60] = (0, 0, 0)  # midnight
        client.put_pixels(leds)
        sleep(.1)
        led = led + 2

for i in range(20):
    if player_one.pos() >= (200 , 100):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (200 , -100):
        print("Player Two Wins!")
        break
    elif dice_outcome >= 4:
        leds = [(0 , 0 , 0)]*360
        for led in range(120):  # pick out indeces: led = 0,1,2,3...
            leds[led] = (44, 87, 132) #bdazzled blue
            sleep(.001)
            client.put_pixels(leds)

            leds[119 - led] = (44, 87, 132) #bdazzled blue
            sleep(.001)
            client.put_pixels(leds)
        smileface1()
        N1()
        I1()
        C1()
        E3()
        R1()
        O()
        L1()
        L2()
        smileface2()
        for i in range(10):
            client.put_pixels(leds)

            sleep(0.02)
        dice = random.randint(1 , 6)  # 6-sides dice random
        player_one_turn = input("Press 'Enter' to roll the die ")
        dice_outcome = dice
        print("The result of the die roll is: ")
        print(dice_outcome)
        print("The number of steps will be: ")
        print(20 * dice_outcome)
        player_one.fd(20 * dice_outcome)
        player_two_turn = input("Press 'Enter' to roll the die ")
        dice = random.randint(1 , 6)
        dice_outcome = dice
        print("The result of the die roll is: ")
        print(dice_outcome)
        print("The number of steps will be: ")
        print(20 * dice_outcome)
        player_two.fd(20 * dice_outcome)


    else:        
        n()
        i1()
        c1()
        e3()
        B1()
        AForBad1()
        DForBad1()
        r()
        o()
        l1()
        l2()
        for led in range(120):  # pick out indeces: led = 0,1,2,3...
            leds[led] = (225, 0, 0) #bdazzled blue
            sleep(.001)
            client.put_pixels(leds)

            leds[119 - led] = (225, 0, 0) #bdazzled blue
            sleep(.001)
            client.put_pixels(leds)
        leds = [(0 , 0 , 0)]*360
        B()
        AForBad()
        DForBad()
        R1()
        O()
        L1()
        L2()
        for i in range(10):
            client.put_pixels(leds)

            sleep(0.02)
        dice = random.randint(1 , 6)  # 6-sides dice random
        player_one_turn = input("Press 'Enter' to roll the die ")
        dice_outcome = dice
        print("The result of the die roll is: ")
        print(dice_outcome)
        print("The number of steps will be: ")
        print(20 * dice_outcome)
        player_one.fd(20 * dice_outcome)
        player_two_turn = input("Press 'Enter' to roll the die ")
        dice = random.randint(1 , 6)
        dice_outcome = dice
        print("The result of the die roll is: ")
        print(dice_outcome)
        print("The number of steps will be: ")
        print(20 * dice_outcome)
        player_two.fd(20 * dice_outcome)
        sleep(.1)


# Animation ===========================================================================================================
if player_one.pos() >= (200 , 100):  
    leds = [(0 , 0 , 0)]*360
    rainbow_1_1()
    P()
    L()
    A()
    Y()
    L()
    E()
    R()
    ONE()
    W()
    I()
    N()
    S()
    sleep(0.4)
    leds = [(0 , 0 , 0)]*360
    row()
    row1()

 #   for led in range(60):  # pick out indeces: led = 0,1,2,3...
 #       leds[led] = (44, 87, 132) #bdazzled blue

 #       leds[59 - led] = (44, 87, 132) #bdazzled blue
 #       time.sleep(.09)
 #       client.put_pixels(leds)


else:
    player_two.pos() >= (200 , -100)
    leds = [(0 , 0 , 0)]*360
    rainbow_2_1()
    P()
    L()
    A()
    Y()
    L()
    E()
    R()
    TWO()
    W()
    I()
    N()
    S()
    rainbow_2_2()
    sleep(0.4)
    leds = [(0 , 0 , 0)]*360
    row()
    row1()

# Animation Player  Win ================================================================================================

