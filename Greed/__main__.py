import os
import random

from Game.casting.actor import Actor
from Game.casting.artifact import Artifact
from Game.casting.cast import Cast

from Game.directing.director import Director

from Game.services.keyboard_service import KeyboardService
from Game.services.video_service import VideoService

from Game.shared.color import Color
from Game.shared.point import Point


FRAME_RATE = 20
MAX_X = 1000
MAX_Y = 600 
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 100
ROWS = 80
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
COLOR = Color(70, 102, 30)
DEFAULT_ROCKS = 50
DEFAULT_GEMS = 50


def main():
    
    
    cast = Cast(COLS, ROWS, CELL_SIZE)
    
    
    score = Actor()
    score.set_text("Score: 0")
    score.set_font_size(FONT_SIZE)
    score.set_color(COLOR)
    score.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("scores", score)
    
    
    x = int(MAX_X / 2)
    y = int(MAX_Y - FONT_SIZE * 2)
    position = Point(x, y)    

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(COLOR)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    '''The Rocks'''
    for n in range(DEFAULT_ROCKS):        
        text = str('O')
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
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
        y_speed = random.randint(3, 5)                
        artifact.set_velocity(Point(0,y_speed))       
                
        cast.add_actor("artifacts", artifact)
    
    '''The gems'''
    for n in range(DEFAULT_GEMS):        
        text = str('*')
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
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
        y_speed = random.randint(2, 5)
        artifact.set_velocity(Point(0,y_speed))
                
        cast.add_actor("artifacts", artifact)
    
    
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
