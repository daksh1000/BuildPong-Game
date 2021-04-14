from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scorecard
import time

screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)

screen.bgcolor("black")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scorecard = Scorecard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scorecard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scorecard.r_point()


screen.exitonclick()
