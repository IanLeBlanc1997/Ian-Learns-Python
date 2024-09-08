from turtle import Turtle
font = ("Courier",25,"bold")
class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.up()
        self.goto(0,340)
        self.score = 0
        self.color(255,255,255)
        self.write(f"Score: {self.score}",False,"center",(font))
    def update(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}",False,"center",(font))
    def final_score(self):
        self.goto(0,0)
        self.write(f"Game Over!\nFinal Score: {self.score}",False,"center",(font))

