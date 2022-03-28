import os
import random
from constants import *

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point



class MazeBuilder:
    def __init__(self):
        pass

    def _build_maze(self):

        with open(DATA_PATH) as file:
            data = file.read()
            # messages = data.splitlines()



        with open("mazegame/maze/data/level1.txt") as level:
            for y, row in enumerate(level):
                for x, column in enumerate(row.strip()):
                    print(f"x,y={x},{y} char={column}")
                    # for n in range(DEFAULT_ARTIFACTS):
                    text = "X"
                    # message = messages[n]
                    position = Point(x, y)
                    position = position.scale(CELL_SIZE)

                    r = random.randint(0, 255)
                    g = random.randint(0, 255)
                    b = random.randint(0, 255)
                    color = Color(r, g, b)
                    
                    artifact = Artifact()
                    artifact.set_text(text)
                    artifact.set_font_size(FONT_SIZE)
                    artifact.set_color(color)
                    artifact.set_position(position)
                    artifact.set_message("HI")
                    cast.add_actor("artifacts", artifact)