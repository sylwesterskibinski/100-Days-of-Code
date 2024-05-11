from turtle import Turtle,Screen
from make_square import make_square

timmy = Turtle()
timmy.shape("turtle")

make_square(timmy)

screen = Screen()
screen.exitonclick()