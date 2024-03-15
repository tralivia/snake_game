
from turtle import Turtle
score = 0
class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.score = 0
            self.penup()
            self.goto(x=0, y=265)
            self.color("white")
            self.hideturtle()
            self.update_scoreboard()

        def update_scoreboard(self):
            self.write(f"score:{self.score} ", align="center", font=("Courier", 24, "normal"))

        def game_over(self):
            self.goto(0,0)
            self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
        def increase_score(self):
            self.score +=1
            self.write(f"score:{self.score} ", align="center", font=("Courier", 24, "normal"))
            self.clear()
            self.update_scoreboard()