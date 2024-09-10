from turtle import Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard
import time
import random
screen = Screen()
screen.setup(1000,800)
screen.colormode(255)
screen.listen()
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.onkey(player.up,"w")
screen.onkey(player.down,"s")
screen.onkey(player.left,"a")
screen.onkey(player.right,"d")

game_is_on = True
def game_over():
    game_is_on = False
    return game_is_on
difficulty = 1
traffic = []

#make original set of cars
for n in range (1,25):
    cars = Car()
    traffic.append(cars) 
for car in traffic:
    car.forward(random.randint(50,500))  
screen.update()


#run game
while game_is_on:
    screen.update()
    time.sleep(.01)
    for car in traffic:
        car.forward(1 + difficulty/25)    
    create_car = random.randint(difficulty,25)
    if create_car == 25:
        cars = Car()
        traffic.append(cars)
        #collision
    for car in traffic:
        if player.distance(car) <= 28:
            car.color(255,0,0)
            player.color(255,0,0)
            screen.update()
            scoreboard.game_over()
            game_is_on = game_over()
        #remove cars from list
        if car.xcor() > 550 or car.xcor() < -550:
            traffic.remove(car)
    #winning and making harder
    if player.ycor() > 320:
        scoreboard.win_level()
        player.win_level()
        difficulty +=1
    if difficulty == 25:
        scoreboard.you_win()
        game_is_on=game_over


            
screen.exitonclick()