from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

continue_snake = True
while continue_snake:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect eating food
    if snake.head.distance(food) < 15:
        food.respawn()
        scoreboard.increase_score()
        snake.add_segment()

    # detect hitting wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        continue_snake = False
        scoreboard.game_over()

    # detect hitting tail
    for segment in snake.seg_list[1:]:
        if snake.head.distance(segment) < 10:
            continue_snake = False
            scoreboard.game_over()


screen.exitonclick()
