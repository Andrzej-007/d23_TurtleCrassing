from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.game_lever = 1
        self.penup()
        self.color('black')
        self.hideturtle()
        self.updatescore()


    def updatescore(self):
        self.goto(-230, 260)
        self.write(f'LEVEL :{self.game_lever}' , align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER !", align=ALIGMENT, font=FONT)

    def increase_point(self):
        self.game_lever += 1
        self.clear()
        self.updatescore()
