import turtle as t
import random
turtle = t.Turtle()
t.colormode(255)
turtle.speed("fastest")

#turtle.shape("turtle")
turtle.hideturtle()


#make turtle draw a bunch of polygons
for i in range (3,11):
    angle = 360/i
    turtle.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    for y in range (0,i):
        turtle.right(angle)
        turtle.forward(100)


#make turtle make a random path
turtle.goto(0,0)
turtle.width(10)
for i in range (0,100):
    turtle.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    turtle.forward(100)
    turtle.right(360/random.choice([1+1/3,4]))
turtle.up()
#make the turtle make a spirograph
turtle.goto(0,0)
turtle.down()
turtle.width(1)
def spirograph(parameter):
    for i in range (int(360/parameter)):
        turtle.seth(turtle.heading() + parameter)
        turtle.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        turtle.circle(100)

parameter = 5
spirograph(parameter)
turtle.up()

#make a spot painting, 10x10, 20 radius, spaced out by 50
turtle.seth(0)
#set start coordinate
turtle.up()
turtle.goto(-325,-325)
counter = 65
for i in range(1,101):
    turtle.begin_fill()
    turtle.circle(20)
    turtle.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    turtle.end_fill()
    turtle.forward(65)
    if i % 10 == 0:
         turtle.goto(-325,-325 + counter)
         counter +=65















screen = t.Screen()
screen.exitonclick()