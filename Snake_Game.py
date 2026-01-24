from turtle import Turtle, Screen
from snake import Snake
from scoreboard import Scoreboard
import time

screen  = Screen()
screen.setup( width = 600, height = 600 )
screen.bgcolor("black")
screen.title(" The Snake Game ")
screen.tracer(0)

starting_positions = [ (0,0), (-20,0), (-40,0) ]

turtles = []
game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey( snake.up, "Up" )
screen.onkey( snake.down, "Down" )
screen.onkey( snake.left, "Left" )
screen.onkey( snake.right, "Right" )

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance() < 15:
        food.new_loc()
        snake.extend()
        scoreboard.increase_score()
    if(snake.head.xcor() > 280 or snake.head.xcor() < -280 or
       snake.head.ycor() > 280 or snake.head.ycor() < - 280):
           game_on = False
    for turtles in snake.turtles[1:]:
        if snake.head.distance(turtles) < 10:
            game_on = False

  
screen.exitonclick()












