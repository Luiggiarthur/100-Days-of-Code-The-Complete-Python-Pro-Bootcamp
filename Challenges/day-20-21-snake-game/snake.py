from turtle import Turtle

SNAKE_BODY = []
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.SNAKE_BODY = []
        self.create_snake()
        self.head = self.SNAKE_BODY[0]

    def create_snake(self):
        x = 0
        for _ in range(3):
            x -= 20
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.setposition(x=x, y=0)
            self.SNAKE_BODY.append(snake)

    def extend(self):
        x = -len(self.SNAKE_BODY)*20
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.setposition(x=x, y=0)
        self.SNAKE_BODY.append(snake)
        
    def move(self):

        for seg_num in range(len(self.SNAKE_BODY) - 1, 0, -1):
            new_x = self.SNAKE_BODY[seg_num - 1].xcor()
            new_y = self.SNAKE_BODY[seg_num - 1].ycor()
            self.SNAKE_BODY[seg_num].goto(new_x, new_y)
        self.SNAKE_BODY[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.SNAKE_BODY[0].setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.SNAKE_BODY[0].setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.SNAKE_BODY[0].setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.SNAKE_BODY[0].setheading(0)
            