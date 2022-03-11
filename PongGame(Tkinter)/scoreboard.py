from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.left_points = 0
        self.right_points = 0
        self.sety(200)
        self.update_points()

    def update_points(self):
        self.write(f"{self.left_points}    {self.right_points}", align="center", font=("Arial", 60, "bold"))

    def increase_left_point(self):
        self.left_points += 1
        self.clear()
        self.update_points()

    def increase_right_point(self):
        self.right_points += 1
        self.clear()
        self.update_points()
