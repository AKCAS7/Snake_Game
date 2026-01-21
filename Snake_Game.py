from turtle import Turtle, Screen
import time

screen  = Screen()
screen.setup( width = 600, height = 600 )
screen.bgcolor("black")
screen.title(" The Snake Game ")
screen.tracer(0)

starting_positions = [ (0,0), (-20,0), (-40,0) ]

turtles = []
game_on = True

for position in starting_positions:
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.goto(position)
    turtles.append(new_turtle)

while game_on:
    screen.update()
    time.sleep(0.1)
    
    for t_num in range( len(turtles) - 1, 0, -1 ):
        new_x = turtles[t_num - 1].xcor()
        new_y = turtles[t_num - 1].ycor() 
        turtles[t_num].goto(new_x, new_y)
    turtles[0].forward(20)

  
screen.exitonclick()







