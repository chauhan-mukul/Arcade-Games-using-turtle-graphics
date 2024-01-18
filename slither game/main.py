from turtle import Screen
import snake
import time
from food import Food
from scoreboard1 import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)
# we have 7 obstacles
""" Create a snake body
move the snake n
create snake food
detect collision with food
create a scoreboard
detect collision with wall
detect collision with tail
"""

# time.sleep(2)
# t1 = threading.Thread(target=snake_body[0].forward, args=[200])
# t2 = threading.Thread(target=snake_body[1].forward, args=[200])
# t3 = threading.Thread(target=snake_body[2].forward, args=[200])
# t1.start()
# t2.start()
# t3.start()
snake = snake.Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detecting food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        snake.extend()
    # detect collision with tail
    for segment in snake.snake_body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
