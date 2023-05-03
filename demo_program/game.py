#define "Class Game"
#__inint__ --> initializer method (initializes "atributes")
#Merhods are special functions defined in a class: METHODS REQUIRE self argument

#Game has a pygame context
import pygame

class Game:
    def __init__(self, caption="my first game", screen_width = 640 , screen_height = 400):
        print("initializing game atributes")


        pygame.init()
        #create tge game Window(screen)
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode(screen_width, screen_height)
        self.keep_screen_open = True

    #this method has the "game loop = while true"
    def run(self):
        print("This is the game run method")
        while self.keep_screen_open:
            print("The game is runing")
        else:
            print("quit game because",self.keep_screen_open)