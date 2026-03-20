from turtle import Turtle
from car_manager import CarManager

car_manager = CarManager()

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1.2,1.2)
        self.seth(90)
        self.penup()
        self.goto(STARTING_POSITION)


    def move_turtle(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def check_win(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)