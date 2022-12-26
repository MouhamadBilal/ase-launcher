import turtle

class Paddle(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)
    
    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)
    
    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)

class Ball(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.dx = 0.1
        self.dy = 0.1
    
    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

