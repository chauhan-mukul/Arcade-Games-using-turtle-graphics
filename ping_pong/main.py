from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
score = Scoreboard()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
ball = Ball()
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detecting collision at top and bottom of the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
    # detecting collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

screen.exitonclick()