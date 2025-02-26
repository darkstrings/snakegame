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
            # The arguments are (start, stop and step)
            # Since the step is negative, the big number is on the left and the 0 is on the right instead of the usual 0 to whatever.
            # That's because it's getting the index of the previous index of segments and using that to assign THAT coordinate to the other one.
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

       #  clear the segment list, send the head snake elsewhere and make a new one
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.heading = 0


# THAT PAIN IN THE ASS FOR LOOP IN MOVE()
# The range(len(segments) - 1, 0, -1)

# len(segments) - 1: This is the index of the last segment in the list.
# If there are 3 segments, len(segments) is 3, so len(segments) - 1 is 2, meaning the loop starts at index 2 (the last segment).

# 0: The loop stops before reaching this value (so it runs until 1).

# -1: The step tells Python to count backward, decreasing by 1 each time.

# What is this loop doing?
# It moves each segment to the position of the segment in front of it, creating the effect of a slithering snake.
#
# Example with 3 segments:

# Index  Position
# 0      (0, 0)  (Head)
# 1      (-20, 0)
# 2      (-40, 0)  (Tail)
# Now, the loop runs:

# seg_num = 2 (last segment, at (-40, 0))
# It moves to the position of segment 1 ((-20, 0)).
# seg_num = 1 (middle segment, at (-20, 0))
# It moves to the position of segment 0 ((0, 0)).
# After the loop, the head (segments[0]) moves forward, creating the illusion of a smooth snake movement.

# Why not start from 0 and go forward?
# Because if we moved from front to back, we'd overwrite positions before using them, breaking the movement chain.
# Starting at the back ensures each segment moves after the one ahead of it has already shifted.