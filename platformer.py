import pygame
import engine
import utils
import level
import scene
import globals
import inputstream
import soundmanager

# constant variables
SCREEN_SIZE = (830,830)
DARK_GREY = (50,50,50)
MUSTARD = (209,206,25)

# init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Platformer game')
clock = pygame.time.Clock()

sceneManager = scene.SceneManager()
mainMenu = scene.MainMenuScene()
sceneManager.push(mainMenu)

inputStream = inputstream.InputStream()

# create player
globals.player1 = utils.makePlayer(300,0)
#globals.player1.camera = engine.Camera(10,10,400,400)
#globals.player1.camera.setWorldPos(300,0)
#globals.player1.camera.trackEntity(globals.player1)
globals.player1.input = engine.Input(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_q, pygame.K_e)

# create player
globals.player2 = utils.makePlayer(350,0)
#globals.player2.camera = engine.Camera(420,10,400,400)
#globals.player2.camera.setWorldPos(350,0)
#globals.player2.camera.trackEntity(globals.player2)
globals.player2.input = engine.Input(pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l, pygame.K_u, pygame.K_o)

# create player
globals.player3 = utils.makePlayer(400,0)
#globals.player3.camera = engine.Camera(10,420,400,400)
#globals.player3.camera.setWorldPos(400,0)
#globals.player3.camera.trackEntity(globals.player3)
globals.player3.input = engine.Input(pygame.K_z, pygame.K_z, pygame.K_z, pygame.K_z, pygame.K_z, pygame.K_x)

# create player
globals.player4 = utils.makePlayer(450,0)
#globals.player4.camera = engine.Camera(420,420,400,400)
#globals.player4.camera.setWorldPos(450,0)
#globals.player4.camera.trackEntity(globals.player4)
globals.player4.input = engine.Input(pygame.K_z, pygame.K_z, pygame.K_z, pygame.K_z, pygame.K_z, pygame.K_x)

running = True
while running:
# game loop

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    inputStream.processInput()
    globals.soundManager.update()

    if sceneManager.isEmpty():
        running = False
    sceneManager.input(inputStream)
    sceneManager.update(inputStream)
    sceneManager.draw(screen) 

    clock.tick(60)

# quit
pygame.quit()