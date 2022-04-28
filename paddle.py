from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.shape("paddle")
        self.color("white")
        self.penup()
        self.goto(position)
        self.collision_width = 110

    def move_r(self):
        if self.xcor() < 320:
            self.forward(20)

    def move_l(self):
        if self.xcor() > -310:
            self.backward(20)

    def shrink(self):
        self.shape("half_paddle")
        self.collision_width = 50