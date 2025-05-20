from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(2,2,1)
        self.color('purple')
        self.penup()
        self.xmove = 10
        self.ymove = 10
    
    def move(self):
        newX = self.xcor()+ self.xmove
        newY = self.ycor()+ self.ymove
        self.goto(newX, newY)
        
    def bounce(self):
        self.ymove*=-1
    
    def hit(self):
        self.xmove*=-1

