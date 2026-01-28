from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "w"):
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto( 0, 260 )

    def increase_score(self):
        self.score +=1
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align = "center", font = ("Arial", 16, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()
    
