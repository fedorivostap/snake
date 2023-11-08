from turtle import Turtle


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []

        self.create_snake()

    def create_snake(self):
        for position in self.starting_positions:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            self.segments.append(new_segment)
            new_segment.goto(position)

    def move(self):
        """Moving that snake"""
        for seg_number in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg_number - 1].xcor()
            y_cor = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(x_cor, y_cor)

        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(to_angle=90)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(to_angle=180)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(to_angle=270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(to_angle=0)

    def make_larger(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].pos())
        self.segments.append(new_segment)



