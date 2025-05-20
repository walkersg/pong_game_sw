from turtle import Turtle

ALIGNMENT = "center"
FONTSPECS = ("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lScore = 0
        self.rScore = 0
        self.penup()
        self.color("white")
        self.goto(0,250)
        self.hideturtle()
        self.update_scoreboard()        
    
    def update_scoreboard(self):
        self.write(f"Player 1: {self.lScore} | Player 2: {self.rScore}", False, align=ALIGNMENT, font=FONTSPECS) 
        
    def increaseRight(self):
        self.rScore += 1
        self.clear()
        self.update_scoreboard()
    
    def increaseLeft(self):
        self.lScore += 1
        self.clear()
        self.update_scoreboard()
    
    
    def createMidline():
        midline = Turtle()
        midline.color("white")
        midline.penup()
        midline.hideturtle()
        midline.goto(0,-540)
        midline.setheading(90)
        midline.speed(0)

        for i in range(20):
            midline.pendown()
            midline.forward(20)
            midline.penup()
            midline.forward(20)
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONTSPECS)        
        
    def player_1_wins(self):
        self.goto(0,-30)
        self.write(f"Player 1 Wins!", False, align=ALIGNMENT, font=FONTSPECS)
    
    def player_2_wins(self):
        self.goto(0,-30)
        self.write(f"Player 2 Wins!", False, align=ALIGNMENT, font=FONTSPECS)

    