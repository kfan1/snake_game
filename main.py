import time
from turtle import *
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.colormode(255)
screen.tracer(n=0)

nagini = Snake()
nagini.create_snake(3)


screen.onkey(nagini.turn_left, key='Left')
screen.onkey(nagini.turn_right, key='Right')
screen.listen()

writing_turtle = Turtle()
writing_turtle.pencolor('red')
writing_turtle.hideturtle()
score_turtle = Turtle()
score_turtle.pencolor('white')
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(x=0, y=280)

still_alive = True
score = 0
num = 0

while still_alive:
    if num != score:
        score_turtle.clear()
    score_turtle.write(arg=f'score: {score}', align='center', move=False, font=('Comic Sans MS', 12, 'normal'))
    screen.update()
    time.sleep(.075)
    nagini.move()
    num = score
    score += nagini.eating()
    still_alive = nagini.dead()
    if still_alive:
        still_alive = nagini.hitting_yourself()
    if not still_alive:
        writing_turtle.write(arg='You lose', align='center', move=False, font=('Comic Sans MS', 36, 'normal'))


screen.exitonclick()
