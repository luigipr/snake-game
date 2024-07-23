from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake = []
        initial_positions = [(0, 0), (-20, 0), (-40, 0)]

        # Cria cada segmento inicial da cobra
        for position in initial_positions:
            block = Turtle(shape="square")
            block.color('white')
            block.penup()
            block.goto(position)
            block.setheading(0)
            self.snake.append(block)
        self.head = self.snake[0]
        #
        # # Cria o primeiro segmento da cobra
        # first_snake = Turtle(shape="square")
        # first_snake.color('white')
        # first_snake.penup()
        # first_snake.setheading(0)
        # self.snake.append(first_snake)
        #
        # # Adiciona mais segmentos à cobra
        # self.snake_machine()
        # self.snake_machine()

    def snake_machine(self):
        # Cria um novo segmento da cobra
        new_segment = Turtle(shape="square")
        new_segment.color('white')
        new_segment.penup()

        # Obtém a posição do último segmento da cobra
        last_segment = self.snake[-1]
        coord = last_segment.pos()

        # Define a posição do novo segmento com base na direção do último segmento
        if last_segment.heading() == 0:
            new_segment.goto(coord[0] - 20, coord[1])
        elif last_segment.heading() == 90:
            new_segment.goto(coord[0], coord[1] - 20)
        elif last_segment.heading() == 180:
            new_segment.goto(coord[0] + 20, coord[1])
        elif last_segment.heading() == 270:
            new_segment.goto(coord[0], coord[1] + 20)
        # Adiciona o novo segmento à lista de segmentos da cobra
        self.snake.append(new_segment)

    def move_up(self):
        head = self.snake[0]
        if head.heading() == 270:
            return
        head.setheading(90)

    def move_right(self):
        head = self.snake[0]
        if head.heading() == 180:
            return
        head.setheading(0)

    def move_down(self):
        head = self.snake[0]
        if head.heading() == 90:
            return
        head.setheading(270)

    def move_left(self):
        head = self.snake[0]
        if head.heading() == 0:
            return
        head.setheading(180)

    def move(self):
        for piece in range(len(self.snake) - 1, 0, -1):
            x = self.snake[piece - 1].xcor()
            y = self.snake[piece - 1].ycor()
            self.snake[piece].goto(x, y)
            # piece.forward(20)
            # piece.setheading(head.heading())
        self.snake[0].forward(20)
