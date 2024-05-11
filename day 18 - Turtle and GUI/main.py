from turtle import Turtle,Screen
from make_square import Square


timmy = Turtle()
timmy.shape("turtle")

square_maker = Square(size=100) 
square_maker.make_square(timmy)

screen = Screen()
screen.exitonclick()