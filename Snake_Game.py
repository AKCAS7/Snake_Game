from turtle import Turtle, Screen, time

screen  = Screen()
screen.setup( width = 600, height = 600 )
screen.bgcolor("black")
screen.title(" The Snake Game ")
screen.tracer(0)

positions = [ (0,0), (-20,0), (-40,0) ]

turtles = []
game_on = True

for position in positions:
    t = Turtle()
    t.penup()
    t.shape("square")
    t.color("white")
    t.goto(position)
    turtles.append(t)

while game_on:
    for t in turtles:
        t.forward(20)
        screen.update()
        time.sleep(1)

screen.exitonclick()













screen.exitonclick()





