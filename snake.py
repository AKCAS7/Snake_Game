from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.turtles.append(segment)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto( 1000, 1000 )
        self.segment.clear()
        self.create()
        self.head = self.turtles[0]

    def move_snake(self):
        for t_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[t_num - 1].xcor()
            new_y = self.turtles[t_num - 1].ycor()
            self.turtles[t_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


