import random
from turtle import Turtle
import random

class Food:
    def __init__(self):
        self.food=Turtle()
        self.food.shape("circle")
        self.food.color("indigo")
        self.food.penup()
        self.food.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        x_cordinat=random.randint(-280,280)
        y_cordinat=random.randint(-280,280)
        self.food.goto(x_cordinat,y_cordinat)