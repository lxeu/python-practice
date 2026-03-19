from turtle import Turtle

FONT = ("courrier", 60, "normal")
ALIGNMENT = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0,-300)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def draw_center_line(self):
        self.color("white")
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        self.hideturtle()

        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()