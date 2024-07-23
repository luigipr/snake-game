from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
game = True


snake = Snake()
food = Food()
score = Score()
screen.update()


screen.listen()
screen.onkey(fun=snake.move_up, key='Up')
screen.onkey(fun=snake.move_up, key='w')
screen.onkey(fun=snake.move_right, key='Right')
screen.onkey(fun=snake.move_right, key='d')
screen.onkey(fun=snake.move_down, key='Down')
screen.onkey(fun=snake.move_down, key='s')
screen.onkey(fun=snake.move_left, key='Left')
screen.onkey(fun=snake.move_left, key='a')

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.snake_machine()
        food.refresh()
        score.update_score()

    for piece in snake.snake[1:]:
        if snake.head.distance(piece) < 3:
            game = False
            score.game_over()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game = False
        score.game_over()


screen.exitonclick()
