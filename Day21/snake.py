from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # initial 3 cubes of snake body
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        initial_segment = Turtle("square")
        initial_segment.color("white")
        initial_segment.penup()
        initial_segment.goto(position)
        self.segments.append(initial_segment)

    def move_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)