from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle("right")
left_paddle = Paddle("left")
screen.listen()

ball = Ball()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.001)
    ball.move()

    screen.onkeypress(key="Up", fun=right_paddle.move_up)
    screen.onkey(key="Up", fun=right_paddle.move_up)
    screen.onkeypress(key="Down", fun=right_paddle.move_down)
    screen.onkey(key="Down", fun=right_paddle.move_down)
    screen.onkeypress(key="w", fun=left_paddle.move_up)
    screen.onkey(key="w", fun=left_paddle.move_up)
    screen.onkeypress(key="s", fun=left_paddle.move_down)
    screen.onkey(key="s", fun=left_paddle.move_down)

    # Detect collision with walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.wall_bounce()

    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.paddle_bounce()

    # Increase player points
    if ball.xcor() > 400:
        scoreboard.increase_left_point()
        ball.refresh()
    elif ball.xcor() < -400:
        scoreboard.increase_right_point()
        ball.refresh()

    if scoreboard.right_points == 10 or scoreboard.left_points == 10:
        game_is_on = False








screen.exitonclick()