import soundmanager

world = None

maxLevel = 3
lastCompletedLevel = 3
curentLevel = 1

DARK_GREY = (50,50,50)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
MUSTARD = (209,206,25)

SCREEN_WIDTH = 3000
SCREEN_HEIGHT = 2800

player1 = None
player2 = None
player3 = None
player4 = None
players = []

LEVEL_BACKGROUNDS = {
    1: (135, 206, 235),   # light sky blue
    2: (255, 182, 193),   # light pink
    3: (144, 238, 144),   # light green
}

soundManager = soundmanager.SoundManager()