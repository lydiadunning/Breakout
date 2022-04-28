from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.score, align="center", font=("Courier", 80, "normal"))

    def increase_points(self, points):
        self.score += points
        self.update_scoreboard()

    def show_score(self):
        self.goto(0, -100)
        self.write(f"SCORE: {self.score}", align="center", font=("Courier", 80, "normal"))


