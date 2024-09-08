#the game of snake
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()
screen.colormode(255)
screen.bgcolor(0,0,0)
screen.setup(1000,800)
screen.title("Snake")
screen.tracer(0)
game_is_on = True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

r,g,b = food.food_color()
print(r,g,b)
while game_is_on:
    screen.update()
    time.sleep(.06)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        snake.eat(r,g,b)
        for n in range (0,3):
            snake.segments[n].color(r,g,b)
        food.eat()
        r,g,b = food.food_color()
        scoreboard.update()
    if snake.segments[0].xcor() > 490 or snake.segments[0].xcor() < -490:
        game_is_on = False
    if snake.segments[0].ycor() > 390 or snake.segments[0].ycor() < -390:
        game_is_on = False 
    for n in range(3,len(snake.segments)-1):
        if snake.segments[0].distance(snake.segments[n]) < 20:
            game_is_on = False


scoreboard.final_score()

screen.exitonclick()
