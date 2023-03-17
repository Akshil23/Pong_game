from turtle import Turtle


class Scorecard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(self.l_score, align="center", font=("Arial", 60, "normal"))
        self.color
        self.goto(x=-120, y=200)
        self.write(self.r_score, align="center", font=("Arial", 60, "normal"))
        self.goto(x=120, y=200)

    def score_left(self):
        self.l_score += 1

    def score_right(self):
        self.r_score += 1

    def winner(self, s):
        self.penup()
        self.goto(0,0)
        self.write(f"{s} player is the winner ", align="center", font=("Arial", 50, "normal"))
