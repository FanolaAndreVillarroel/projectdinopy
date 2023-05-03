#responsable de crear catus de distintos tipos
from game.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from game.components.cactus import Cactus
import random

class CactusBuilder():

    def __init__(self):
        self.cactuses = []

    def update(self):
        #self.cactuses.extend(LARGE_CACTUS)

        random_number = random.randint(0,1)
        cactus_images = SMALL_CACTUS if random_number == 0 else LARGE_CACTUS

        for img_cactus in cactus_images:
            cactus = Cactus(img_cactus)
            self.cactuses.append(cactus)
        #self.cactuses.pop() #remuve un elemento en la cola

    def  draw(self,screen):
        x = 300
        y = 300
        for cactus in self.cactuses:
            y += 200
            x = 320
            cactus.draw(screen, x, y)

            #limpia la lista
            #self.cactuses = []
