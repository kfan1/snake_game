from turtle import Turtle

class Score():
    def __init__(self):
        self.writing_turtle = Turtle()
        self.writing_turtle.pencolor('red')
        self.writing_turtle.hideturtle()
        self.score_turtle = Turtle()
        self.score_turtle.pencolor('white')
        self.score_turtle.hideturtle()
        self.score_turtle.penup()
        self.score_turtle.goto(x=0, y=280)

    def keeping_score(self, previous, current):
        if previous != current:
            self.score_turtle.clear()
        self.score_turtle.write(arg=f'score: {current}', align='center', move=False, font=('Comic Sans MS', 12, 'normal'))

    def you_lose(self, bool):
        if not bool:
            self.writing_turtle.write(arg='You lose', align='center', move=False, font=('Comic Sans MS', 36, 'normal'))