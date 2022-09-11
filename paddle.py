from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        x_cor = self.xcor()
        y_cor = self.ycor()+20
        if y_cor < 260:
            self.goto(x=x_cor, y=y_cor)

    def go_down(self):
        x_cor = self.xcor()
        y_cor = self.ycor()-20
        if y_cor > -245:
            self.goto(x=x_cor, y=y_cor)
