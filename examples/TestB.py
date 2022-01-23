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

for led in range(0,1): #p
    for rows in range(0,6):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(1,4):
    for rows in range(0,1):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(3,4):  #p
    for rows in range(0,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(1,4):  #p
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(4,5):  #L
    for rows in range(6):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(5,9):  #L
    for rows in range(5,6):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(13,14):  #A 12,13
    for rows in range(0,1):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(12,13): #A 11,12
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(10,11): #A 9,10
    for rows in range(3,4):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(9,10): #A 8,9
    for rows in range(4,5):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(8,9): #A 7,8
    for rows in range(5,6):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(11,16): #A 10,15
    for rows in range(2,3):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(14,15): #A 13,14
    for rows in range(1,2):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(16,17): #A 15,16
    for rows in range(3,4):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(17,18): #A 16,17
    for rows in range(4,5):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(18,19): #A 17,18
    for rows in range(5,6):
        if player_one.pos() >= (300,100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)


#player 2

for led in range(0,1): #p
    for rows in range(0,6):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(1,4):
    for rows in range(0,1):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(3,4):  #p
    for rows in range(0,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(1,4):  #p
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(4,5):  #L
    for rows in range(6):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(5,9):  #L
    for rows in range(5,6):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(13,14):  #A 12,13
    for rows in range(0,1):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(12,13): #A 11,12
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(10,11): #A 9,10
    for rows in range(3,4):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(9,10): #A 8,9
    for rows in range(4,5):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(8,9): #A 7,8
    for rows in range(5,6):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(11,16): #A 10,15
    for rows in range(2,3):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(14,15): #A 13,14
    for rows in range(1,2):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(16,17): #A 15,16
    for rows in range(3,4):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(17,18): #A 16,17
    for rows in range(4,5):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)

for led in range(18,19): #A 17,18
    for rows in range(5,6):
        if player_two.pos() >= (300,-100):
            leds[led+rows*60] = (255,255,0)
client.put_pixels(leds)
sleep(.1)
