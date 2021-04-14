from turtle import Turtle

STEP = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        xc = self.xcor()
        yc = self.ycor() + STEP
        self.goto(x=xc, y=yc)

    def go_down(self):
        xc = self.xcor()
        yc = self.ycor() - STEP
        self.goto(x=xc, y=yc)


