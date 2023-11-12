from turtle import Turtle
import os


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        if os.path.exists("score_log.txt") and os.path.getsize("score_log.txt") > 0:
            with open("score_log.txt", "r") as file:
                self.highest_score = int(file.read())
        else:
            self.highest_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, "normal"))

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 10, "normal"))

    def restart_game(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        with open(file="score_log.txt", mode="w") as file:
            file.write(str(self.highest_score))

    def display_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}    Highest score: {self.highest_score}",
                   align="center", font=("Arial", 10, "normal"))




