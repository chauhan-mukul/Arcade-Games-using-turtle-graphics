from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self, i):
        snake_body1 = Turtle('square')
        snake_body1.penup()
        snake_body1.color('white')
        snake_body1.goto(i)
        self.snake_body.append(snake_body1)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for seg_no in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_no - 1].xcor()
            new_y = self.snake_body[seg_no - 1].ycor()
            self.snake_body[seg_no].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
