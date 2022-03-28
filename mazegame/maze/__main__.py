from game.constants import Constants

from game.casting.actor import Actor
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.services.level_service import LevelService

from game.shared.point import Point

def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(Constants.FONT_SIZE)
    banner.set_color(Constants.WHITE)
    banner.set_position(Point(Constants.CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(Constants.MAX_X / 2)
    y = int(Constants.MAX_Y / 2)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(Constants.FONT_SIZE)
    robot.set_color(Constants.WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    # start the game
    keyboard_service = KeyboardService(Constants.CELL_SIZE)
    video_service = VideoService(Constants.CAPTION, Constants.MAX_X, Constants.MAX_Y, 
        Constants.CELL_SIZE, Constants.FRAME_RATE)
    level_service = LevelService()
    director = Director(keyboard_service, video_service, level_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()
