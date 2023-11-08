from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")

    def generate_food_piece(self):
        """Generate new food piece when snake eats it food"""
        x_cor_food = random.randint(-280, 280)
        y_cor_food = random.randint(-280, 280)
        self.goto(x_cor_food, y_cor_food)


