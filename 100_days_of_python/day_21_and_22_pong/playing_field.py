from turtle import Turtle, Screen
screen = Screen()
scoreboard_font = ("Courier",50,"bold")
class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.create_net()

    def create_net(self):
        self.hideturtle()
        self.up()
        self.goto(0,-400)
        self.write("|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n",False,"center",("Arial", 20, "bold"))

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.create_scoreboard()
    
    def create_scoreboard(self):
        self.hideturtle()
        self.up()
        self.goto(0,335)
        self.write(f"{self.left_score}  {self.right_score}",False,"center",scoreboard_font)

    def score_left(self):
        self.left_score+=1
        self.clear()
        self.write(f"{self.left_score}  {self.right_score}",False,"center",scoreboard_font)
        
    def score_right(self):
        self.right_score+=1
        self.clear()
        self.write(f"{self.left_score}  {self.right_score}",False,"center",scoreboard_font)

