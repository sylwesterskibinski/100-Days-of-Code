from turtle import Turtle,Screen,colormode
from shapes import Shapes
from random import randint


timmy = Turtle()
timmy.shape("turtle")
colormode(255)
shape_maker = Shapes(size=50,sides=3) 
timmy.speed(10)

for _ in range(7):
    shape_maker.make_shape(timmy)
    shape_maker.sides += 1
    timmy.color(randint(0, 255), 
          randint(0, 255), 
          randint(0, 255))


screen = Screen()
screen.exitonclick()