class Shapes():
    def __init__(self,size,sides):
        self.size = size
        self.sides = sides
        
    def make_shape(self,turtle):
        for x in range(self.sides):
            turtle.forward(self.size)
            turtle.right(360/self.sides)