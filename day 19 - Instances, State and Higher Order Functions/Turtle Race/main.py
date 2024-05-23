from turtle import Turtle,Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]

turtles = []

y_positions = [-100, -60, -20, 20, 60, 100]

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won, {winning_color} color won")
            else:
                print(f"You've lost, {winning_color} color won")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()