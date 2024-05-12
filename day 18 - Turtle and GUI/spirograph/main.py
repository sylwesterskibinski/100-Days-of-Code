from turtle import Turtle, Screen, colormode
from random import randint, choice

timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
timmy.pensize(1)
colormode(255)

for _ in range(72):
    actual_direction = timmy.heading()
    actual_direction += 5
    timmy.circle(100)
    timmy.setheading(actual_direction)
    timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))


screen = Screen()
screen.exitonclick()
