STARTING_PLACES = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.heading = 0
        self.create_snake()
        self.head = self.segments[0]
        self.last_input = self.heading

    def up(self):
        if self.last_input != 270:
            self.heading = 90
    def down(self):
        if self.last_input != 90:
            self.heading = 270
    def left(self):
        if self.last_input != 0:
            self.heading = 180
    def right(self):
        if self.last_input != 180:
            self.heading = 0

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.setheading(self.heading)
        self.head.forward(MOVE_DISTANCE)
        self.last_input = self.head.heading()

    def create_snake(self):
        for position in STARTING_PLACES:
           self.add_segment(position)

    def add_segment(self, position):
        snake_piece = Turtle("square")
        snake_piece.color("green")
        snake_piece.penup()
        snake_piece.goto(position)
        self.segments.append(snake_piece)

    def extend(self):
        self.add_segment(self.segments[-1].position())
       #  clear the segment list, send the head snake to the shadow realm and make a new one
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.heading = 0
