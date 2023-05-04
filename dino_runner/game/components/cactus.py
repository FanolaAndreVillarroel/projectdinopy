from game.utils.constants import LARGE_CACTUS,SMALL_CACTUS

class Cactus:
    def __init__(self,image):
        self.image = image
        self.x_pos_bg = 600
        self.y_pos_bg = 300

    
    def draw(self, screen):

        image_width = self.image.get_width()

        screen.blit(self.image, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            screen.blit(self.image, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg =2000
        self.x_pos_bg -= 15