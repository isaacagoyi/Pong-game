import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

PADDLE_POSITIONS = [(-370, 0), (370,0)]
game_on = True

screen = Screen()
screen.tracer(0)
paddle_left = Paddle(PADDLE_POSITIONS[0])
paddle_right = Paddle(PADDLE_POSITIONS[1])
ball = Ball()
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")


# Paddle controls
screen.listen()
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

while game_on:
    time.sleep(ball.difficulty)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_right)<50  and ball.xcor() > 340 or ball.distance(paddle_left)<50 and ball.xcor() < -340 :
        ball.bounce_x()


#     Detect if paddle misses the ball
#     Right paddle miss
    if ball.xcor()>380:
        ball.reset_ball()
        scoreboard.increment_left_score()

    #     Left paddle misses
    if ball.xcor()<-380:
        ball.reset_ball()
        scoreboard.increment_right_score()
screen.exitonclick()