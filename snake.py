from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.body = []
        self.x = 20
        self.y = 0
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for segment in range(3):
            self.segment = Turtle("square")
            self.segment.color("white")
            self.segment.penup()
            self.x -= 20
            self.segment.setposition(x=self.x, y=self.y)
            self.body.append(self.segment)

    def move(self):
        for segment_number in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment_number - 1].xcor()
            new_y = self.body[segment_number - 1].ycor()
            self.body[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def extend(self):
        self.segment = Turtle("square")
        self.segment.color("white")
        self.segment.penup()
        self.segment.setposition(x=self.body[-1].xcor(), y=self.body[-1].ycor())
        self.body.append(self.segment)

    def rest(self):
        for seg in self.body:
            seg.goto(1000, 1000)
        self.x = 20
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

