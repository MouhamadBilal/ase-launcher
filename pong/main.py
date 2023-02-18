from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

p1_paddle = Paddle((350, 0))
p2_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(fun=p1_paddle.up, key="Up")
screen.onkey(fun=p1_paddle.down, key="Down")
screen.onkey(fun=p2_paddle.up, key="z")
screen.onkey(fun=p2_paddle.down, key="s")

ball = Ball()
score = Score()

game_on = True

while game_on:
    time.sleep(ball.time_speed)
    screen.update()
    ball.move()
    
# Collision Ball/Mur
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
# Collision avec les paddles
    if ball.distance(p1_paddle) < 50 and ball.xcor() > 320 or ball.distance(p2_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 420:
        score.p1_point()
        ball.restart()
    elif ball.xcor() < -420:
        score.p2_point()
        ball.restart()
    
screen.exitonclick()
