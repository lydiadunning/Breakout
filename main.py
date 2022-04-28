# A version of Breakout

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from wall import Wall
from lifebar import Lifebar
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(700, 600, None, 100)
screen.title("BREAKOUT")
screen.tracer(0)

screen.register_shape("brick", ((8, -20), (8, 20), (-8, 20), (-8, -20)))
screen.register_shape("paddle", ((10, -100), (10, 100), (-10, 100), (-10, -100)))
screen.register_shape("half_paddle", ((10, -50), (10, 50), (-10, 50), (-10, -50)))

wall = Wall()
paddle = Paddle((0, -250))
ball = Ball()
lifebar = Lifebar()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.move_r, "Right")
screen.onkeypress(paddle.move_l, "Left")

while not lifebar.out_of_lives():
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with side of window
    if ball.ycor() > 280:
        ball.bounce_y()
        paddle.shrink()

    if ball.xcor() < -330 or ball.xcor() > 320:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < paddle.collision_width and ball.ycor() < -220:
        if ball.ycor() < -230:
            ball.bounce_x()
        else:
            ball.bounce_y()


    # Detect collision with bricks in wall
    for brick in wall.bricks:
        x, y = brick.position()
        x1 = x - 10
        x2 = x + 10
        if ball.distance((x1, y)) < 20 or ball.distance((x2, y)) < 20:
            ball.bounce_y()
            brick_outcome = wall.hit(brick)
            scoreboard.increase_points(brick_outcome["points"])
            if brick_outcome["accelerate"]:
                ball.speed_up()

    # Detect paddle misses
    if ball.ycor() < -300:
        ball.reset_position(paddle.xcor())
        lifebar.lose_a_life()

lifebar.game_over()
scoreboard.show_score()

screen.exitonclick()