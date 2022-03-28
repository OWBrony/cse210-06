from game.constants import Constants

from game.shared.color import Color

from game.casting.actor import Actor

class Wall(Actor):
    def __init__(self):
        self.set_text("X")
        self.set_font_size(Constants.FONT_SIZE)
        self.set_color(Color(127,127,127))