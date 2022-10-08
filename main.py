from turtle import Screen
import time

import scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# build the screen as a black and 600X600 screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# build the starting snake with white color, square shape 20X20 size, position at (0,0), (-20,0) and (-40,0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# # move the snake by making the segments like a linked table,
# # the last segment take the position of the one before it and so on


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    # Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with the wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
            or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    # detect collision with the tail.
    # if head collides with any segments of the tail:
        # trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
