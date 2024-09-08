import random
from turtle import Turtle, Screen
screen = Screen()
screen.colormode(255)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.speed("fastest")
        self.goto(random.randint(-450,450),random.randint(-350,350))
        
    def food_color(self):
        r,g,b = random.randint(50,255),random.randint(50,255),random.randint(50,255)
        self.color(r,g,b)
        return r,g,b
    

    def eat(self):
        self.food_color()
        self.goto(random.randint(-450,450),random.randint(-350,350))