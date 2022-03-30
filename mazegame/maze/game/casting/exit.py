from game.constants import Constants
from game.shared.color import Color
from game.casting.actor import Actor

class Exit(Actor):
    def __init__(self, level, x, y):
        self.set_text("O")
        self.set_font_size(Constants.FONT_SIZE)
        self.set_color(Color(127,127,0))
        self.level = level
        self.x = x
        self.y = y
