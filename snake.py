from turtle import Turtle

MOVE_DIST = 20

X_START = 0
Y_START = 0
ANGLE_START = 0

class Snake:

    def __init__(self):
        self.seg_list = []
        self.length = 0
        for _ in range(3):
            self.add_segment()
        self.head = self.seg_list[0]

    def add_segment(self):
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        if not self.seg_list:
            segment.seth(ANGLE_START)
            segment.goto(X_START, Y_START)
        else:
            segment.goto(self.seg_list[-1].xcor(), self.seg_list[-1].ycor())

        self.length += 1
        self.seg_list.append(segment)

    def move(self):
        for seg_num in range(self.length - 1, 0, -1):
            new_x = self.seg_list[seg_num - 1].xcor()
            new_y = self.seg_list[seg_num - 1].ycor()
            self.seg_list[seg_num].goto(new_x, new_y)
        self.seg_list[0].forward(MOVE_DIST)

    def up(self):
        if self.seg_list[0].heading() != 270:
            self.seg_list[0].seth(90)

    def down(self):
        if self.seg_list[0].heading() != 90:
            self.seg_list[0].seth(270)

    def left(self):
        if self.seg_list[0].heading() != 0:
            self.seg_list[0].seth(180)

    def right(self):
        if self.seg_list[0].heading() != 180:
            self.seg_list[0].seth(0)
