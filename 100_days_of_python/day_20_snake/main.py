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
screen.onkey(snake.up,"w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

r,g,b = food.food_color()
print(r,g,b)
while game_is_on:
    screen.update()
    time.sleep(.06)
    snake.move()
    #snake eating food
    if snake.segments[0].distance(food) < 15:
        snake.eat(r,g,b)
        for n in range (0,3):
            snake.segments[n].color(r,g,b)
        food.eat()
        r,g,b = food.food_color()
        scoreboard.update()
        #snake colliding with wall
    if snake.segments[0].xcor() > 490 or snake.segments[0].xcor() < -490:
        game_is_on = False
    if snake.segments[0].ycor() > 390 or snake.segments[0].ycor() < -390:
        game_is_on = False 
        #snake colliding with self
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False


scoreboard.final_score()

screen.exitonclick()
