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
def pause():
    time.sleep(infinity)

r,g,b = food.food_color()
for n in range (107):
    snake.eat(r,g,b)
while game_is_on:
    screen.update()
    time.sleep(.1)
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
        scoreboard.reset()
        snake.reset()
    if snake.segments[0].ycor() > 390 or snake.segments[0].ycor() < -390:
        scoreboard.reset()
        snake.reset()
        #snake colliding with self
    if snake.segments[0].distance(snake.segments[2]) < 10:
        snake.adjust()
        print("I adjusted")
    for segment in snake.segments[4:]:
        if snake.segments[0].distance(segment) < 20:
            scoreboard.reset()
            snake.reset()
    



screen.exitonclick()


