import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from random import choice

BG_COLORS = [
    "black", "midnight blue", "navy", "dark green", "maroon", "purple",
    "dark slate gray", "firebrick", "saddle brown", "dark olive green"
]

COLORS = [
    "white", "lime", "pink", "cyan", "yellow", "orange", "magenta", "gold",
    "deepskyblue", "turquoise", "orchid", "chartreuse", "dodgerblue",
    "springgreen", "violet", "tomato", "peru", "darkorange", "hotpink", "khaki"
]

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

# Flashing control
flashing = False  # Global flag to control flashing

def flash_colors():
    if not flashing:
        return  # Stop execution if flashing is disabled

    random_bg = choice(BG_COLORS)
    random_primary = choice(COLORS)

    # Change background color
    screen.bgcolor(random_bg)

    # Change food and snake segment colors
    food.color(random_primary)
    for seg in snake.segments:
        seg.color(random_primary)
    scoreboard.color(random_primary)
    scoreboard.clear()
    scoreboard.game_over()
    scoreboard.update_scoreboard()
    screen.update()  # Force update

    screen.ontimer(flash_colors, 8000)  # Schedule next flash

def start_flashing():
    global flashing
    flashing = True
    screen.ontimer(flash_colors, 6000)

def stop_flashing():
    global flashing
    food.color("red")
    food.refresh()
    flashing = False
    screen.bgcolor("black")

def start():
    stop_flashing()  # Stop flashing when restarting
    scoreboard.clear()
    scoreboard.reset()
    screen.update()
    snake.reset()
    game_loop()  # Restart the game loop

def game_loop():
    global game_on
    game_on = True

    while game_on:
        screen.update()
        time.sleep(0.08)
        snake.move()

        # Detect touching food
        if snake.head.distance(food) < 15:
            scoreboard.score_up()
            snake.extend()
            food.refresh()

        # Detect hitting wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_on = False

        # Detect hitting tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False

    scoreboard.game_over()  # Show game over screen
    start_flashing()  # Restart flashing on game over

scoreboard.intro()
screen.onkey(start, "space")  # Allow restarting the game with the spacebar


screen.mainloop()
