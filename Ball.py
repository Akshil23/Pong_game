from turtle import Turtle


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)
        self.X = 10
        self.Y = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.X
        y = self.ycor() + self.Y
        self.goto(x, y)

    def bounce(self):
        self.Y *= -1

    def bounceBack(self):
        self.X *= -1
        self.move_speed *= 0.7

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.X *= -1
