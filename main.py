from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

ball = Ball()

board = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

midline  = Scoreboard.createMidline()

game_is_on = True

while game_is_on == True:
    time.sleep(0.1)
    ball.move()
    screen.update()
    
    #detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit()
        
    if ball.xcor() > 350:
        time.sleep(.25)
        board.increaseLeft()
        board.update_scoreboard()
        ball.goto(0,0)
        time.sleep(1)


    
    if ball.xcor() < -350:
        time.sleep(.25)
        board.increaseRight()
        board.update_scoreboard()
        ball.goto(0,0)
        time.sleep(1)
    
    if board.lScore == 5:
        board.game_over()
        board.player_1_wins()
        game_is_on = False
    
    if board.rScore == 5:
        board.game_over()
        board.player_2_wins()
        game_is_on = False  
        

    
screen.exitonclick()