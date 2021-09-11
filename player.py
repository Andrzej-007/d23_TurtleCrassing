
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

    def __init__(self):
        self.player_user = Turtle(shape='turtle')
        self.player_user.penup()
        self.go_to_start()
        self.player_user.setheading(90)


    def move_up(self):
        self.player_user.forward(MOVE_DISTANCE)
        # position_y = self.player_user.ycor() + MOVE_DISTANCE
        # self.player_user.setposition(0, position_y )
        # self.setpos(self.xcor(), position_y)

    def move_down(self):
        position_y = self.player_user.ycor() - MOVE_DISTANCE
        self.player_user.setposition(0, position_y )

    def go_to_start(self):
        self.player_user.goto(STARTING_POSITION)
        
        # test what to do 




