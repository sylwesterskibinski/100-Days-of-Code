import colorgram
from turtle import Turtle, Screen
from random import choice
colors = colorgram.extract('C:/Users/skibi/Desktop/100 Days of Code/day 18 - Turtle and GUI/hirst_painting/dots.jpg', 10)

rgb_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_list.append(rgb)

filtered_rgb_list = [rgb for rgb in rgb_list if not (rgb[0] > 200 and rgb[1] > 200 and rgb[2] > 200)]

timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.penup()
timmy.setpos(-200,-100)

for _ in range(10):
    def make_dots_in_row():
        for _ in range(10):
            dot_color = choice(filtered_rgb_list)
            timmy.dot(15,dot_color)
            timmy.forward(30)
        
    make_dots_in_row()  
    position = timmy.position()
    timmy.setposition(((position[0])-300),(position[1])+30)

      

screen.exitonclick()

