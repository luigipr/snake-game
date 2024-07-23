from turtle import Turtle
import random

values = list(range(-263, 264, 20))


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()

        self.speed("fastest")
        self.goto(random.choice(values), random.choice(values))

    def refresh(self):
        self.goto(random.randint(-280,280), random.randint(-280,280))

