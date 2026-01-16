from turtle import Turtle, Screen

screen  = Screen()
screen.setup( width = 600, height = 600 )
screen.bgcolor("black")
screen.title(" The Snake Game ")

'''

t1.color("white")
t2.color("white")
t3.color("white")

t1.penup()
t2.penup()
t3.penup()
'''
positions = [ (0,0), (-20,0), (-40,0) ]

for position in positions:
    t = Turtle()
    t.shape("square")
    t.color("white")
    t.goto(position)
    














screen.exitonclick()


