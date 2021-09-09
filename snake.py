import time
from turtle import Turtle

class Snake:
    snake_body=[]
    def __init__(self):
        snake_body=self.make_snake_body() 

    def turn_left(self):
        if self.snake_body[0].heading() != 0 and self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(180)

    def turn_right(self):
        if self.snake_body[0].heading() != 180 and self.snake_body[0].heading() != 0:    
            self.snake_body[0].setheading(0)

    def turn_up(self):
        if self.snake_body[0].heading() != 270 and self.snake_body[0].heading() != 90: 
            self.snake_body[0].setheading(90)    

    def turn_down(self):
        if self.snake_body[0].heading() != 90 and self.snake_body[0].heading() != 270: 
            self.snake_body[0].setheading(270)

    def make_move(self):

        for i in range(len(self.snake_body)-1,0,-1):
            self.snake_body[i].goto(self.snake_body[i-1].position())
        self.snake_body[0].forward(20)


    def make_square(self):
        square=Turtle()
        square.shape("square")
        square.color("white")
        square.penup()
        return square

    def make_snake_body(self):
        for i in range(0,3):
            square=self.make_square()
            square.goto(-i*20,0)
            self.snake_body.append(square)

    def add_square(self):
        new_square=self.make_square()
        self.snake_body.append(new_square)
        self.make_move()

            
