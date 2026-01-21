from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [ (0,0), (-20,0), (-40,0) ]

class Snake:
    
    def __init__(self):
        self.turtles =[]
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(position)
            self.turtles.append(new_turtle)

    def move_snake(self):
        for t_num in range( len(self.turtles) - 1, 0, -1 ):
            new_x = self.turtles[t_num - 1].xcor()
            new_y = self.turtles[t_num - 1].ycor() 
            self.turtles[t_num].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_DISTANCE)
