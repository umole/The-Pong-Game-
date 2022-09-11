from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title("The Pong Game.")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.delay(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if r_paddle.distance(ball) < 30 or l_paddle.distance(ball) < 30:
        ball.rebounce_x()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.rebounce_y()

    #Detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
