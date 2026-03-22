from turtle import Turtle

ALIGNMENT = "center"
FONT = ("times new roman", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()
    
    # scoreboard text
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.highscore < self.score:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()