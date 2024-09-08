from turtle import Turtle, Screen
import time
screen = Screen()
screen.colormode(255)


STARTING_POSITIONS = [(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
   def __init__(self):
      self.segments = []
      self.create_snake()

   def create_snake(self):
      for position in STARTING_POSITIONS:
         new_segment = Turtle("square")
         new_segment.up()
         new_segment.color(255,255,255)
         new_segment.goto(position)
         self.segments.append(new_segment)


   def move(self):
      for n in range(len(self.segments)-1,0,-1):
         new_pos = self.segments[n-1].pos()
         self.segments[n].goto(new_pos)
      self.segments[0].forward(MOVE_DISTANCE)
   
   def up(self):
      if self.segments[0].heading() != 270:
         self.segments[0].seth(90)
   def down(self):
      if self.segments[0].heading() != 90:
         self.segments[0].seth(270)
   def right(self):
      if self.segments[0].heading() != 180:
         self.segments[0].seth(0)
   def left(self):
      if self.segments[0].heading() != 0:
         self.segments[0].seth(180)

   def eat(self,r,g,b):
     
      self.new_segment = Turtle("square")
      self.new_segment.up()
      self.new_segment.color(r,g,b)
      self.new_segment.goto(1000,1000)
      self.segments.append(self.new_segment)
      self.new_segment.showturtle()
      
      

   
      