from turtle import Turtle, Screen, colormode
from random import randint, choice

timmy = Turtle()
timmy.shape("turtle")
timmy.speed(10)
timmy.pensize(5)
colormode(255)

for _ in range(50):
    timmy.forward(10)
    degrees = choice([90])
    sides_to_choose = choice(["left", "right"])
    if sides_to_choose == "left":
        timmy.left(degrees)
        timmy.color(randint(0, 255), randint(0, 255), randint(0, 255)) 
    else:
        timmy.right(degrees)
        timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
    timmy.forward(10)

screen = Screen()
screen.exitonclick()
