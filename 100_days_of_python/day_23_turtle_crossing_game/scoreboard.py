from turtle import Turtle

font = ("Courier",50,'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-450,330)
        self.write(f"{self.score}",False,'center',font)
    
    def win_level(self):
        self.score +=1
        self.clear()
        self.write(f"{self.score}",False,'center',font)
    

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"Game Over\nFinal Score:{self.score}",align="center",font=font)