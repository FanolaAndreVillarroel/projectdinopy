from game.utils.constants import LARGE_CACTUS

class Cactus:
    def __init__(self,image):
        self.image = image
    
    def draw(self, screen, x, y):
        cactus_rect = self.image.get_rect()
        cactus_rect.y = x
        cactus_rect.x = y
        screen.blit(self.image,cactus_rect)