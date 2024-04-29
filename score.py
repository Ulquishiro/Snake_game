from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}, High Score: {self.high_score}", move=False, align="center", font=('Arial', 12, 'normal'))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", move=False, align="center", font=('Arial', 12, 'normal'))

    def increase_number(self):
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 12, 'normal'))
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()



