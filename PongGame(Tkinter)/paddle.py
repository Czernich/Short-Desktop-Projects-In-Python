from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        if side == "right":
            self.goto(350, 0)
        elif side == "left":
            self.goto(-350, 0)

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)