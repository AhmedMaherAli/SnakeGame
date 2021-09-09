from math import dist
import time
from snake import Snake
from turtle import Screen, distance
from food import Food
from scoreboard import Score

def setup_screen():
    screen.listen()
    screen.setup(width=600,height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")


def define_moves():

    screen.onkey(snake.turn_right,"d")
    screen.onkey(snake.turn_left,"a")
    screen.onkey(snake.turn_up,"w")
    screen.onkey(snake.turn_down,"s")


screen=Screen()
screen.tracer(0)
setup_screen()
snake=Snake()
food=Food()
scoreboard=Score()
define_moves()

game_on=True
while game_on:
    snake.make_move()
    if snake.snake_body[0].distance(food.food)<15:
        food.refresh()
        snake.add_square()
        scoreboard.update_score()
    elif snake.snake_body[0].xcor()>280 or snake.snake_body[0].xcor()<-280 or snake.snake_body[0].ycor()>280 or snake.snake_body[0].ycor()<-280:
        scoreboard.game_over()
        game_on=False    
    snake_len=len(snake.snake_body)
    for i in range(1,snake_len):
        if snake.snake_body[0].distance(snake.snake_body[i]) <10:
            scoreboard.game_over()
            game_on=False
            break
    screen.update()
    time.sleep(0.1)   

screen.exitonclick()
