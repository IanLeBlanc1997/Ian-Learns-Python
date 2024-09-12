from turtle import Turtle
font = ("Courier",25,"bold")
with open("/Users/ianleblanc/Desktop/Repositories/Ian-Learns-Python/100_days_of_python/day_20_snake/snake_high_score.txt") as snake_high_score:
    high_score = int(snake_high_score.read())
class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.up()
        self.goto(-300,340)
        self.score = 0
        self.color(255,255,255)
        self.write(f"Score: {self.score} High Score: {high_score}",False,"center",(font))

    def update(self):
        self.clear()
        with open("/Users/ianleblanc/Desktop/Repositories/Ian-Learns-Python/100_days_of_python/day_20_snake/snake_high_score.txt") as snake_high_score:
            high_score = int(snake_high_score.read())
        self.score +=1
        self.write(f"Score: {self.score} High Score: {high_score}",False,"center",(font))
        if self.score > high_score:
            self.clear()
            with open("/Users/ianleblanc/Desktop/Repositories/Ian-Learns-Python/100_days_of_python/day_20_snake/snake_high_score.txt", mode="w") as snake_high_score:
                snake_high_score.write(f"{self.score}")
                high_score = int(snake_high_score.read())
                self.write(f"Score: {self.score} High Score: {high_score}",False,"center",(font))
    def reset(self):
        with open("/Users/ianleblanc/Desktop/Repositories/Ian-Learns-Python/100_days_of_python/day_20_snake/snake_high_score.txt") as snake_high_score:
            high_score = int(snake_high_score.read())
        self.clear()
        self.score = 0
        self.write(f"Score: {self.score} High Score: {high_score}",False,"center",(font))


