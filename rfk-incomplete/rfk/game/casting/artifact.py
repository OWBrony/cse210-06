import csv
from game.casting.actor import Actor
from game.shared.color import Color

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
# Right here is the columns and rows to use!!!
COLS = 60
ROWS = 40
# CAPTION = "Robot Finds Kitten"
# DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40
FIELD_TOP = 60
# FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
# FIELD_RIGHT = SCREEN_WIDTH

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    def __init__(self):
        super().__init__()
        self.message = ""

    def set_message(self, message):
        self.message = message

    def get_message(self):
        return self.message

    def set_position(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):
                    x = FIELD_LEFT + c * MAX_X
                    y = FIELD_TOP + r * MAX_Y

                    position = point(x,y)
                    cast.add_actor(MAZE_GROUP,block)
                    pass