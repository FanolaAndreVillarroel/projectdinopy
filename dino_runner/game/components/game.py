import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from game.components.dino import Dinosaur
from game.components.cloud import Cloud
from game.components.bird import Bird
#from game.components.cactus import Cactus
from game.components.cactus_builder import CactusBuilder

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        
        

        #Game has dinosaur:
        self.dinosaur = Dinosaur("T_Rex")

        show_name = pygame.font.SysFont('Z003', 50)

        self.attribute = show_name.render("Dino: "+self.dinosaur.name +" is running", False, (0, 0, 0))
        #Game has cloud:
        self.cloud = Cloud(self.game_speed)
        #Game has cloud:
        self.bird = Bird()
        #game has cactus
        #self.cactus = Cactus()
        #has builder cactus
        self.cactus_builder = CactusBuilder()

    def run(self):
        # This is Game Loop: events - update - draw
        print("starting the game loop")
        self.playing = True
        while self.playing:
            self.capture_events()
            self.update()
            self.draw()
        else:
            print("quit the game")
            pygame.quit()


    def capture_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("received event.type", event.type, "that indicates `quit` game")
                self.playing = False

    #actualiza el estado de los objetos en pantalla
    def update(self):
        self.dinosaur.update(pygame.key.get_pressed())
            
        self.cloud.update()
        self.bird.update()
        self.cactus_builder.update(0)
        

    #actualiza el display del juego
    def draw(self):
        print("entering draw")
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        #DRAW Dinosaurs
        self.dinosaur.draw(self.screen)
        self.screen.blit(self.attribute, (500, 500))

        #DRAW Claud:
        self.cloud.draw(self.screen)
        self.cloud.draw(self.screen)

        #DRAW Birds
        self.bird.draw(self.screen)

        #DRAW Cactus
        #self.cactus.draw(self.screen)

        #Se pide al  cactus_builder que dibije cactus
        self.cactus_builder.draw(self.screen)

        #Cambios en la pantalla
        pygame.display.update()
        pygame.display.flip()
        #
        print("exiting draw")

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
