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

while True:
    for i in range(10):
        if player_one.pos() >= (300,100):
                print("Player One Wins!")
                break
        else:
            player_two.pos() >= (300,-100):
                print("Player Two Wins!")
                break
        else:

           while led in range(0,1):
                for rows in range(3):
                    if player_one_turn >= input("Press 'Enter' to roll the die ")
                    leds[led+rows*60] = (255,255,0)
                    die_outcome = random.choice(die)
            client.put_pixels(leds)
            sleep(0.1)





        
        
        
