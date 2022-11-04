import random
from turtle import *


class Snake:
    def __init__(self):
        self.snake = []
        self.food = Turtle()
        self.food.color('green')
        self.food.shape('square')
        self.food.penup()
        randx = random.randint(-13, 13) * 20
        randy = random.randint(-13, 13) * 20
        self.food.goto(x=randx, y=randy)

    def create_snake(self, length):
        for _ in range(length):
            self.snake.append(Turtle())
            self.snake[_].color((255, 255, 255))
            self.snake[_].shape('square')
            self.snake[_].penup()
            self.snake[_].goto(x=-20 * _, y=0)
        return self.snake

    def add_snake(self):
        grow = Turtle()
        tail_xposition = self.snake[-1].xcor()
        tail_yposition = self.snake[-1].ycor()
        tail_hd = self.snake[-1].heading()
        grow.color((255, 255, 255))
        grow.shape('square')
        grow.penup()
        grow.seth(tail_hd)
        if tail_hd == 0:
            grow.goto((tail_xposition - 20, tail_yposition))
        if tail_hd == 90:
            grow.goto((tail_xposition, tail_yposition - 20))
        if tail_hd == 180:
            grow.goto((tail_xposition+ 20, tail_yposition))
        if tail_hd == 270:
            grow.goto((tail_xposition, tail_yposition + 20))
        self.snake.append(grow)

    def turn_left(self):
        self.snake[0].left(90)

    def turn_right(self):
        self.snake[0].right(90)

    def move(self):
        for _ in range(len(self.snake) - 1, -1, -1):
            self.snake[_].fd(20)
            if self.snake[_].heading() != self.snake[_ - 1].heading() and _ != 0:
                self.snake[_].seth(self.snake[_ - 1].heading())

    def dead(self):
        if self.snake[0].xcor() <= -300 or self.snake[0].xcor() >= 300:
            return False
        if self.snake[0].ycor() <= -300 or self.snake[0].ycor() >= 300:
            return False
        else:
            return True

    def eating(self):
        xs = round(self.snake[0].xcor())
        ys = round(self.snake[0].ycor())
        xf = self.food.xcor()
        yf = self.food.ycor()
        if (xs, ys) == (xf, yf):
            self.add_snake()
            randx = random.randint(-13, 13) * 20
            randy = random.randint(-13, 13) * 20
            self.food.goto(x=randx, y=randy)
            return 1
        else:
            return 0

    def hitting_yourself(self):
        snake_cordinates = []
        for _ in range(1, len(self.snake)):
            xss = round(self.snake[_].xcor())
            yss = round(self.snake[_].ycor())
            snake_cordinates.append((xss, yss))
        xs = round(self.snake[0].xcor())
        ys = round(self.snake[0].ycor())
        if (xs, ys) in snake_cordinates:
            return False
        else:
            return True

