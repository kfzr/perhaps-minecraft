import turtle
import random

screen = turtle.Screen()
screen.bgcolor('lightgreen')

player_one = turtle.Turtle()
player_one.color('blue')
player_one.penup()
player_one.goto(-300, 200)

player_two = turtle.Turtle()
player_two.color('red')
player_two.penup()
player_two.goto(-300, -200)

player_one.goto(300, -250)
player_one.left(90)
player_one.pencolor('black')
player_one.pendown()
player_one.forward(500)
player_one.write('finish', font=24)
player_one.penup()
player_one.goto(-300, 200)
player_one.pencolor('blue')
player_one.right(90)

die = [1, 2, 3, 4, 5, 6]

for i in range(30):
    if player_one.pos() >= (300, 250):
        print("player one wins")
        player_one.hideturtle()
        player_one.goto(0,0)
        player_one.write('player one won')
        break
    elif player_two.pos() >= (300, -250):
        print("player two wins")
        player_two.hideturtle()
        player_two.goto(0,0)
        player_two.write('player two finished')
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(60*die_roll/2.5)
        die_roll2 = random.choice(die)
        player_two.forward(60*die_roll/2.5)

turtle.done()

