from turtle import Turtle


class Lifebar(Turtle):
    def __init__(self):
        super(Lifebar, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = ["0", "0", "0"]
        self.update_lifebar()

    def update_lifebar(self):
        self.clear()
        self.goto(-200, 200)
        lifebar = f"{self.lives[0]}{self.lives[1]}{self.lives[2]}"
        self.write(lifebar, align="center", font=("Courier", 80, "normal"))

    def lose_a_life(self):
        self.lives.append("X")
        self.lives.pop(0)
        self.update_lifebar()


    def out_of_lives(self):
        return self.lives == ["X", "X", "X"]

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 80, "normal"))
