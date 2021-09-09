
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

    def __init__(self):
        self.player_user = Turtle(shape='turtle')
        self.player_user.penup()
        self.player_user.goto(STARTING_POSITION)
        self.player_user.setheading(90)


    def move_up(self):
        position_y = self.player_user.ycor() + MOVE_DISTANCE
        self.player_user.setposition(0, position_y )
        # self.setpos(self.xcor(), position_y)

    def move_down(self):
        position_y = self.player_user.ycor() - MOVE_DISTANCE
        self.player_user.setposition(0, position_y )



