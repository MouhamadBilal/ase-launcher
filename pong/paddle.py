from turtle import Turtle

UP = 90
DOWN = 270

# Définition des paddle (couleur, forme etc)

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(position)
        self.color("white")
        self.resizemode(stretch_width=5, stretch_len=1)
        
        
# Création des mouvements des Paddle
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
