from turtle import Turtle
import random
STARTING_LOCATIONS_LEFT = [-240,-160,-80,0,80,160,240,320]
STARTING_LOCATIONS_RIGHT = [-280,-200,-120,-40,40,120,200,280]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1,2,2)
        self.color(random.randint(40,200),random.randint(40,200),random.randint(40,200))
        self.position_cars()

    def position_cars(self):
        side = random.choice([1,2])
        if side ==1:
            self.goto(-550,random.choice(STARTING_LOCATIONS_LEFT))
        else:
            self.goto(550,random.choice(STARTING_LOCATIONS_RIGHT))
        if self.xcor() == -550:
            self.seth(0)
        else:
            self.seth(180)
