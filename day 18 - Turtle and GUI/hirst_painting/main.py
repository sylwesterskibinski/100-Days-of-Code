import colorgram

colors = colorgram.extract('C:/Users/skibi/Desktop/100 Days of Code/day 18 - Turtle and GUI/hirst_painting/dots.jpg', 10)

rgb_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_list.append(rgb)

print("Original RGB List:", rgb_list)

filtered_rgb_list = [rgb for rgb in rgb_list if not (rgb[0] > 200 and rgb[1] > 200 and rgb[2] > 200)]

