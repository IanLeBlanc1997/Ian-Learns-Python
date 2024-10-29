from playing_field import Net, Scoreboard
from ball import Ball
from paddles import Paddle
from turtle import Turtle, Screen
import time
screen = Screen()
screen.listen()
screen.setup(1000,800)
screen.tracer(0)
screen.title("Pong")
screen.colormode(255)
net = Net()
scoreboard = Scoreboard()
ball = Ball()
left_paddle = Paddle()
left_paddle.goto(-400,0)
right_paddle = Paddle()
right_paddle.goto(400,0)
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.05)
    ball.move()
    #scoring
    if ball.xcor() > 500:
        scoreboard.score_left()
        ball.reset()
    if ball.xcor() < -500:
        scoreboard.score_right()
        ball.reset()
    #collision
    if ball.ycor() > 370 or ball.ycor() < -370:
        ball.bounce()
    if ball.xcor() < -385 and ball.xcor() > -400 and ball.distance(left_paddle.pos()) <= 50:
        ball.hit()
        r,g,b = ball.recolor()
        left_paddle.recolor(r,g,b)
    if ball.xcor() > 385 and ball.xcor() < 400 and ball.distance(right_paddle.pos()) <= 50:
        ball.hit()
        r,g,b = ball.recolor()
        right_paddle.recolor(r,g,b)

     







screen.exitonclick()