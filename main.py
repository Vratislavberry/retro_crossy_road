from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from traffic_lanes import Traffic_lanes
from line import Line


# setting up screen
screen = Screen()
screen.bgcolor("grey")
screen.setup(width=600, height=600)
screen.colormode(255)
screen.tracer(0)

# setting up an image
screen.addshape("finnish_line.gif")
img = Turtle()
img.penup()
img.sety(190)
img.shape("finnish_line.gif")




# creating objects
player = Player()
scoreboard = Scoreboard()
traffic_lanes = Traffic_lanes()
line = Line()

# controls
screen.listen()
screen.onkey(player.do_a_step, "space")


# The game itself
game_continues = True
while game_continues:
    traffic_lanes.start_traffic()

    # player reached the end of level
    if player.is_winner():
        traffic_lanes.new_level(scoreboard.level)
        player.reset_position()
        scoreboard.update_score()

    # player lost
    if traffic_lanes.is_crashed(player):
        if scoreboard.new_highscore():
            scoreboard.update_highscore()
            scoreboard.print_highscore()
        scoreboard.game_over()
        game_continues = False
    screen.update()

screen.update()






screen.exitonclick()
