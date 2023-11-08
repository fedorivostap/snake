from turtle import Screen, Turtle
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


my_snake = Snake()

screen.listen()
screen.onkeypress(my_snake.up, "Up")
screen.onkeypress(my_snake.down, "Down")
screen.onkeypress(my_snake.left, "Left")
screen.onkeypress(my_snake.right, "Right")

while True:
    time.sleep(0.1)
    screen.update()
    my_snake.move()




# segment_1 = Turtle(shape="square")
# segment_2 = Turtle(shape="square")
# segment_3 = Turtle(shape="square")
#
# segment_2.setposition((-20.00, 0.00))
# segment_3.setposition((-40.00, 0.00))
# segment_1.color("white")
# segment_2.color("white")
# segment_3.color("white")


# segment_1.degrees(fullcircle=360)
# segment_1.speed("slowest")
# segment_1.pendown()

# snake_tail = Turtle()
# snake_tail.shape("square")
# snake_tail.color("white")


# def move_right():
#     if segment_1.heading() != 180:
#         segment_1.setheading(to_angle=0)
#
#
# def move_up():
#     if segment_1.heading() != 270:
#         segment_1.setheading(to_angle=90)
#
#
# def move_left():
#     if segment_1.heading() != 0:
#         segment_1.setheading(to_angle=180)
#
#
# def move_down():
#     if segment_1.heading() != 90:
#         segment_1.setheading(to_angle=270)
#
#
# def snake_steering():
#     turtle_tail_id = segment_1.stamp()
#     #snake_tail.setposition(snake.pos())
#     segment_1.forward(10)
#     clearstamp(turtle_tail_id)
#     screen.listen()
#     screen.onkeypress(fun=move_left, key="a")
#     screen.onkeypress(fun=move_right, key="d")
#     screen.onkeypress(fun=move_up, key="w")
#     screen.onkeypress(fun=move_down, key="s")
#




# while True:
#     snake_steering()

#screen.exitonclick()
