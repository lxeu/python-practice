from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-220,250)
        self.print_level()
    
    def print_level(self):
        self.clear()
        self.write(f"Level {self.level}", font=FONT, align=ALIGNMENT)

    def increase_level(self):
        self.level += 1
        self.print_level()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)