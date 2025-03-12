import pygame
import globals
import utils

class Level:
    def __init__(self, platforms=None, entities=None, winFunc=None, loseFunc=None, powerupSpawnPoints=None):
        self.platforms = platforms
        self.entities = entities
        self.winFunc = winFunc
        self.loseFunc = loseFunc
        self.powerupSpawnPoints = powerupSpawnPoints
    def isWon(self):
        if self.winFunc is None:
            return False
        return self.winFunc(self)
    def isLost(self):
        if self.loseFunc is None:
            return False
        return self.loseFunc(self)

# lose if no players have lives remaining
def lostLevel(level):
    # level isn't lost if any player has a life left
    for entity in level.entities:
        if entity.type == 'player':
            if entity.battle is not None:
                if entity.battle.lives > 0:
                    return False
    # level is lost otherwise
    return True

# win if no collectable items left
def wonLevel(level):
    # level isn't won if any collectable exists
    for entity in level.entities:
        if entity.type == 'collectable':
            return False
    # level isn't won otherwise
    return True

def loadLevel(levelNumber):
    if levelNumber == 1:
        # load level 1
        globals.world = Level(
            platforms = [
                # middle
                pygame.Rect(100,300,400,50),
                # left
                pygame.Rect(100,250,50,50),
                # right
                pygame.Rect(450,250,50,50)
            ],
            entities = [
                utils.makeCoin(100,200),
                utils.makeCoin(200,250),
                utils.makeEnemy(150,274)
            ],
            winFunc = wonLevel,
            loseFunc = lostLevel,
            powerupSpawnPoints = [(400,260),(300,100)]
        )
    if levelNumber == 2:
        # load level 2
        globals.world = Level(
            platforms = [
                # middle
                pygame.Rect(100,300,400,50)
            ],
            entities = [
                utils.makeCoin(100,200)
            ],
            winFunc = wonLevel,
            loseFunc = lostLevel,
            powerupSpawnPoints = [(400,260),(300,100)]
        )

    elif levelNumber == 3:
        globals.world = Level(
        platforms=[
            pygame.Rect(50, 400, 300, 50),   # Starting platform
            pygame.Rect(400, 350, 200, 50),  # Mid-air platform
            pygame.Rect(650, 300, 200, 50),  # Another platform
            pygame.Rect(900, 250, 250, 50),  # Higher platform
            pygame.Rect(1200, 200, 200, 50), # Final stretch
        ],
        entities=[
            utils.makeCoin(100, 350),
            utils.makeCoin(450, 320),
            utils.makeCoin(700, 270),
            utils.makeCoin(950, 220),
            utils.makeEnemy(300, 374),
            utils.makeEnemy(600, 324),
            utils.makeEnemy(1100, 174),
        ],
        winFunc=wonLevel,
        loseFunc=lostLevel,
        powerupSpawnPoints=[(500, 320), (850, 220)]
    )

    
    # add players
    for player in globals.players:
        globals.world.entities.append(player)     

    # reset players
    for entity in globals.world.entities:
        entity.reset(entity)