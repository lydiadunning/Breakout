from math import floor
from turtle import Turtle

BRICK_X = 40
BRICK_Y = 20
SPACING_X = 10 + BRICK_X
SPACING_Y = 5 + BRICK_Y
STARTING_X = -330
STARTING_Y = 200

class Wall():
    def __init__(self):
        super(Wall, self).__init__()
        self.brick_colors = ["firebrick", "darkorange", "springgreen4", "gold"]
        self.bricks = []
        self.place_bricks()
        self.speed_walls = []
        self.hit_count = 0
        self.accel_colors = ["firebrick", "darkorange"]

    def place_bricks(self):
        y = STARTING_Y
        for brick_row in range(8):
            x = STARTING_X
            color = self.brick_colors[floor(brick_row / 2)]
            for i in range(14):
                brick = self.make_brick(color)
                brick.setposition(x, y)
                self.bricks.append(brick)
                x +=  SPACING_X
            y -= SPACING_Y

    def make_brick(self, color):
        brick = Turtle()
        brick.penup()
        brick.shape("brick")
        brick.color(color)
        return brick

    def hit(self, brick):
        color = brick.fillcolor()
        points = self.hit_points(color)
        accelerate = self.hit_accelerate(color)
        brick.reset()
        self.bricks.remove(brick)
        self.hit_count += 1
        return {"points": points, "accelerate": accelerate}


    def hit_points(self, brick_color):
        points_list = [7, 5, 3, 1]
        points = points_list[self.brick_colors.index(brick_color)]
        return points

    # hitting a certain number of bricks or rows for the first time speeds up the game.
    def hit_accelerate(self, brick_color):
        if brick_color in self.accel_colors:
            self.accel_colors.remove(brick_color)
            return True
        return self.hit_count == 4 or self.hit_count == 12