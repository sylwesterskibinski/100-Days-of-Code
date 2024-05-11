class Square():
    def __init__(self,size):
        self.size = size
    
    def make_square(self,turtle):
        for x in range(4):
            turtle.forward(100)
            turtle.right(90)
