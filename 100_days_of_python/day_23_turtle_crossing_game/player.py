from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0,-360)
        self.setheading(90)
    def up(self):
        self.setheading(90)
        self.forward(40)
    def down(self):
        if self.ycor() > -350:
            self.seth(270)
            self.forward(40)
        else:
            None
    def left(self):
        if self.xcor() > -460:
            self.setheading(180)
            self.forward(40)
        else:
            None
    def right(self):
        if self.xcor() < 460:
            self.seth(0)
            self.forward(40)
        else:
            None
    def win_level(self):
        self.goto(0,-360)
