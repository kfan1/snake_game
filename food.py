import random
from turtle import *

class Food:
    def __init__(self):
        self.food = Turtle()
        self.food.color('green')
        self.food.shape('square')
        self.food.penup()
        randx = random.randint(-13, 13) * 20
        randy = random.randint(-13, 13) * 20
        self.food.goto(x=randx, y=randy)

    def eating(self, snaker):
        xs = round(snaker.snake[0].xcor())
        ys = round(snaker.snake[0].ycor())
        xf = self.food.xcor()
        yf = self.food.ycor()
        if (xs, ys) == (xf, yf):
            snaker.add_snake()
            randx = random.randint(-13, 13) * 20
            randy = random.randint(-13, 13) * 20
            self.food.goto(x=randx, y=randy)
            return 1
        else:
            return 0