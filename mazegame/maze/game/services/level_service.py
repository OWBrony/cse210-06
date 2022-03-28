import numpy as np
import random

from game.constants import Constants

from game.casting.wall import Wall

from game.shared.color import Color
from game.shared.point import Point

class LevelService:
    EMPTY = 0
    WALL = 1

    def __init__(self):
        self._matrix = None

    def at(self, x, y):
        return self._matrix[x, y]

    def _char_to_int(self, c):
        if c == "X": return LevelService.WALL
        return LevelService.EMPTY

    def _construct_actor(self, n):
        if n == LevelService.WALL: return (Wall(), "walls")
        return (None, None)

    def _clear_level_actors(self, cast):
        cast.remove_actor_group("walls")

    def load_level(self, cast, path):
        # Load the level from the file
        self._matrix = np.array([[0],[0]])
        self._matrix.resize(Constants.COLS, Constants.ROWS)
        with open(path) as level:
            for y, row in enumerate(level):
                for x, column in enumerate(row.strip()):
                    print(f"{x} {y}")
                    self._matrix[x, y] = self._char_to_int(column)
        # Construct actors from level data
        self._clear_level_actors(cast)
        for x in range(0, Constants.COLS):
            for y in range(0, Constants.ROWS):
                print(f"x,y={x},{y} char={column}")
                (actor, group) = self._construct_actor(self._matrix[x, y])
                if not actor == None:
                    position = Point(x, y)
                    position = position.scale(Constants.CELL_SIZE)
                    actor.set_position(position)
                    cast.add_actor(group, actor)
