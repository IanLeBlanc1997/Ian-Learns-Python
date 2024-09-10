from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5,1,None)
        

    def up(self):
        x,y=self.pos()
        if y >350:
            None
        else:
            self.goto(x,y + 40)
        
    def down(self):
        x,y = self.pos()
        if y < -350:
            None
        else:
            self.goto(x,y - 40)

    def recolor(self,r,g,b):
        self.color(r,g,b)