#responsable de crear catus de distintos tipos
from game.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from game.components.cactus import Cactus
import random

class CactusBuilder():

    def __init__(self):
        self.cactuses = []
        self.cactus_images = LARGE_CACTUS
        

    def update(self):
        if len(self.cactuses) == 0:
            for img_cactus in self.cactus_images:
                cactus = Cactus(img_cactus)
                self.cactuses.append(cactus)

        #self.cactuses.extend(LARGE_CACTUS)

        # random_number = random.randint(0,1)
        # for img_cactus in self.cactus_images:
        #     cactus = Cactus(img_cactus)
        #     self.cactuses.append(cactus)
        
        # for c in self.cactuses:
        #     c.rect.x -= 50
        #     if c.rect.x < -c.rect.width:
        #         self.cactuses.pop()

    def  draw(self,screen):
        self.cactuses[-1].x_pos_bg -= 15

        for obstacle in self.cactuses:
            obstacle.draw(screen)

        # x = 300
        # y = 300
        # for cactus in self.cactuses:
        #     y += 200
        #     x = 320
        #     cactus.draw(screen, x, y)

            #limpia la lista
            #self.cactuses = []

