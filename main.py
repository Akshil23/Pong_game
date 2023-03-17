from turtle import Screen
from Paddle import Paddle
from Ball import Ball
import time
from Scorecard import Scorecard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle((380, 0))
r_paddle.color("red")

l_paddle = Paddle((-380, 0))
l_paddle.color("yellow")
ball = Ball((0, 0))
score = Scorecard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    score.update_scoreboard()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if (ball.distance(r_paddle) < 80 and ball.xcor() > 340) or (ball.distance(l_paddle) < 80 and ball.xcor() < -340):
        ball.bounceBack()

    if ball.xcor() < -400:
        ball.reset()
        score.score_left()
        score.update_scoreboard()
    if ball.xcor() > 400:
        ball.reset()
        score.score_right()
        score.update_scoreboard()
    if score.l_score == 10:
        score.winner("Left")
        game_is_on = False
    elif score.r_score == 10:
        score.winner("Right")
        game_is_on = False
screen.exitonclick()
