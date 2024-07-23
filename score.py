from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.pencolor('white')
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align='center', font=('Arial', 20, 'normal'))
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align='center', font=('Arial', 20, 'normal'))

