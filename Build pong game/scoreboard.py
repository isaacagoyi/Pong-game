from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 250)
        self.update_scoreboard()

    def update_scoreboard (self):
        self.clear()
        self.write(f"Player L score: {self.l_score} & Player R score: {self.r_score}", align="center",
                   font=("Arial", 24, "bold"))


    def increment_left_score(self):
        self.l_score +=1
        self.update_scoreboard()

    def increment_right_score(self):
        self.r_score +=1
        self.update_scoreboard()