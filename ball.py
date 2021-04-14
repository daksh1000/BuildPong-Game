from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.penup()
        self.ball_speed = 0.1

    def move(self):
        xc = self.xcor() + self.x_move
        yc = self.ycor() + self.y_move
        self.goto(x=xc, y=yc)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.8

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.x_bounce()



