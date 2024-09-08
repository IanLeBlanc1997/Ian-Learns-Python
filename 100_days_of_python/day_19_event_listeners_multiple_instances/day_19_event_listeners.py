from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def rotate_clockwise():
   tim.right(10)
def rotate_counterclockwise():
    tim.left(10)
def clear():
    tim.goto(0,0)
    tim.clear()
    


screen.listen()
screen.onkey(key= "w", fun=move_forward)
screen.onkey(key= "s", fun=move_backward)
screen.onkey(key= "a", fun=rotate_counterclockwise)
screen.onkey(key= "d", fun=rotate_clockwise)
screen.onkey(key= "space", fun=clear)
screen.exitonclick()