import time
from turtle import *
from snake import Snake
from food import Food
from scores import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.colormode(255)
screen.tracer(n=0)

nagini = Snake()
nagini.create_snake(3)
food = Food()

screen.onkey(nagini.turn_left, key='Left')
screen.onkey(nagini.turn_right, key='Right')
screen.listen()

penturtle = Score()

still_alive = True
score = 0
num = 0

while still_alive:
    screen.update()
    time.sleep(.075)
    nagini.move()
    num = score
    score += food.eating(nagini)
    penturtle.keeping_score(num, score)
    still_alive = nagini.dead()
    if still_alive:
        still_alive = nagini.hitting_yourself()
    penturtle.you_lose(still_alive)



screen.exitonclick()
