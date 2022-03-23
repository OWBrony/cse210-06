# This will hold the code to read the maze.txt files
# it should print them out in an arrangment like in the file
# use Batter file scene_manager.py: starting at line 164.
import csv
from services.keyboard_service import KeyboardService
from services.video_service import VideoService
from casting.artifact import Artifact

class SceneManager():

    KEYBOARD_SERVICE = RaylibKeyboardService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    def __init__():
        pass

    def _add_maze_bricks(self, cast):
        cast.clear_actors()

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):

                    x = FIELD_LEFT + c * BRICK_WIDTH
                    y = FIELD_TOP + r * BRICK_HEIGHT
                    color = column[0]
                    frames = int(column[1])
                    points = BRICK_POINTS 
                    
                    if frames == 1:
                        points *= 2
                    
                    position = Point(x, y)
                    size = Point(BRICK_WIDTH, BRICK_HEIGHT)
                    velocity = Point(0, 0)
                    # images = BRICK_IMAGES[color][0:frames]

                    body = Body(position, size, velocity)
                    # animation = Animation(images, BRICK_RATE, BRICK_DELAY)

                    brick = Brick(body, animation, points)
                    cast.add_actor(BRICK_GROUP, brick)
        pass

