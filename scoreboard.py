from turtle import Turtle

ALIGNMENT = "center"
FONT = "Comic Sans MS"
FONT_SIZE = 20
FONT_STYLE = "normal"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt") as file:
            self.high_score_from_file = int(file.read())
        self.ht()
        self.penup()
        self.score = 0
        self.highscore = self.high_score_from_file
        self.shape("circle")
        self.color("red")
        self.update_scoreboard()

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=(FONT, FONT_SIZE, FONT_STYLE))
        self.setposition(0, -60)
        self.write("Press spacebar to play again", align="center", font=(FONT, FONT_SIZE, FONT_STYLE))


    def intro(self):
        self.setposition(0, 0)
        self.write("Press spacebar to start", align="center", font=("Comic Sans MS", 20, "normal"))

    def update_scoreboard(self):
        self.setposition(0, 260)
        self.write(f"Score: {self.score}     High Score: {self.highscore}", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_STYLE))

    def reset(self):
        self.clear()
        if self.score > self.highscore:
            with open("high_score.txt", mode="w") as checkfile:
                checkfile.write(str(self.score))
            self.highscore = self.score
        self.score = 0
        self.color("red")
        self.update_scoreboard()

    def score_up(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

