from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.reset()
       
    def reset(self):
        self.goto(0,0)
        self.up()
        self.x_move = random.randint(4,8)
        self.y_move = random.randint(4,8)
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1
    def recolor(self):
        r,g,b = random.randint(0,200),random.randint(0,200),random.randint(0,200)
        self.color(r,g,b)
        return r,g,b

    def hit(self):
        self.x_move *= -1
        if self.x_move > 0:
            self.x_move += random.randint(1,3)
        else:
            self.x_move -= random.randint(1,3)
        if self.y_move > 0:
            self.y_move += random.randint(1,3)
        else:
            self.y_move -= random.randint(1,3)


       

