from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


my_snake = Snake()
snake_food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkeypress(my_snake.up, "Up")
screen.onkeypress(my_snake.down, "Down")
screen.onkeypress(my_snake.left, "Left")
screen.onkeypress(my_snake.right, "Right")

run_game = True
while run_game:
    time.sleep(0.1)
    screen.update()
    my_snake.move()
    scoreboard.display_score()
    if my_snake.segments[0].distance(snake_food) < 15:
        snake_food.generate_food_piece()
        scoreboard.increase_score()
        my_snake.make_larger()

    if (my_snake.segments[0].xcor() > 280 or my_snake.segments[0].xcor() < -280
            or my_snake.segments[0].ycor() > 280 or my_snake.segments[0].ycor() < -280):
        scoreboard.restart_game()
        my_snake.restart_game()
        # run_game = False

    for segment in my_snake.segments[1:]:
        if my_snake.segments[0].distance(segment) < 10:
            scoreboard.restart_game()
            my_snake.restart_game()
            # run_game = False
            # break

screen.exitonclick()
