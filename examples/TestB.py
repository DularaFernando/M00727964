import turtle
from time import sleep
import random
import opc

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)

player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)

die = [1,2,3,4,5,6]

for i in range(10):
    if player_one.pos() >= (300,100):
            print("Player One Wins!")
            break
    elif player_two.pos() >= (300,-100):
            print("Player Two Wins!")
            break
    else:
            player_one_turn = input("Press 'Enter' to roll the die ")
            die_outcome = random.choice(die)
            print("The result of the die roll is: ")
            print(die_outcome)
            print("The number of steps will be: ")
            print(20*die_outcome)
            player_one.fd(20*die_outcome)
            player_two_turn = input("Press 'Enter' to roll the die ")
            die_outcome = random.choice(die)
            print("The result of the die roll is: ")
            print(die_outcome)
            print("The number of steps will be: ")
            print(20*die_outcome)
            player_two.fd(20*die_outcome)

for led in range(0,2): 
    for rows in range(6):
        if die_outcome >= 3:
            leds[led+rows*60] = (0,255,0)
            break
client.put_pixels(leds)
sleep(.1)
   
    #------------------- player 1 ---------------------

for led in range(0,1): #p
    for rows in range(3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(1,3):
    for rows in range(0,1):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(2,3):  #p
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(1,2):  #p
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(4,5):  #L
    for rows in range(3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(5,7):  #L
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(8,9):  #A 
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(9,12):  #A 
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(10,11):  #A 
    for rows in range(0,1):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(12,13):  #A 
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(14,15): #Y
    for rows in range(0,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(15,16): #Y
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(16,17): #Y
    for rows in range(0,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(15,16): #Y
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(18,21): #E
    for rows in range(0,1):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(18,20): #E
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(18,21): #E
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(22,25): #R
    for rows in range(0,1):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(22,24): #R
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(22,23): #R
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(24,25): #R
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(28,30): #1
    for rows in range(0,1):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(29,30): #1
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(28,31): #1
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(33,34): #W
    for rows in range(0,1):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(34,35): #W
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(38,39): #W
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(36,37): #W
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)


for led in range(35,36): #W
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(37,38): #W
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(39,40): #W
    for rows in range(0,1):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(41,44): #I
    for rows in range(0,1):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(42,43): #I
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(41,44): #I
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(45,46): #N
    for rows in range(3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(46,47): #N
    for rows in range(0,1):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(47,48): #N
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(48,49): #N
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(49,50): #N
    for rows in range(3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(51,54): #S
    for rows in range(0,1):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(52,53): #S
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(51,54): #S
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

 #------------------- player 2 ---------------------

for led in range(0,1): #p
    for rows in range(3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(1,3):
    for rows in range(0,1):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(2,3):  #p
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(1,2):  #p
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(4,5):  #L
    for rows in range(3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(5,7):  #L
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(8,9):  #A 
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(9,12):  #A 
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(10,11):  #A 
    for rows in range(0,1):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(12,13):  #A 
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(14,15): #Y
    for rows in range(0,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(15,16): #Y
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(16,17): #Y
    for rows in range(0,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(15,16): #Y
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(18,21): #E
    for rows in range(0,1):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(18,20): #E
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(18,21): #E
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(22,25): #R
    for rows in range(0,1):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(22,24): #R
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(22,23): #R
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(24,25): #R
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(28,30): #1
    for rows in range(0,1):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(29,30): #1
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(28,31): #1
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(33,34): #W
    for rows in range(0,1):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(34,35): #W
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(38,39): #W
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(36,37): #W
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)


for led in range(35,36): #W
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(37,38): #W
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(39,40): #W
    for rows in range(0,1):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(41,44): #I
    for rows in range(0,1):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(42,43): #I
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(41,44): #I
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(45,46): #N
    for rows in range(3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(46,47): #N
    for rows in range(0,1):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(47,48): #N
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(48,49): #N
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(49,50): #N
    for rows in range(3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(51,54): #S
    for rows in range(0,1):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(52,53): #S
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

for led in range(51,54): #S
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,255)
client.put_pixels(leds)
sleep(.1)

