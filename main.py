import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.title('Crassing the Sreeet')
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")
screen.onkeypress(fun=player.move_down, key="Down")

loop_number = 0
game_is_on = True

while game_is_on:
    loop_number += 1
    time.sleep(0.1)
    screen.update()
    if (loop_number % 5) == 0:
        car_manager.create_car()
    car_manager.move_cars()
    tertle_pos = player.player_user.ycor()

    # Detect the collision with car
    for car in car_manager.all_cars:
        if car.distance(player.player_user) < 25:
            scoreboard.game_over()
            # print('game over')
            game_is_on = False

    # Detect seccussful crossing
    if player.player_user.ycor() >= 280:
        car_manager.increase_cars_sped()
        scoreboard.increase_point()
        player.go_to_start()




screen.exitonclick()
