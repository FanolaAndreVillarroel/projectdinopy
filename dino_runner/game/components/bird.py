import random
from game.utils.constants import BIRD
class Bird:
    def __init__(self):
        
        self.image = BIRD[0]
        self.x_pos_bg = 900
        self.y_pos_bg = 100

    #bird sabe dibujarse (pygame)
    def draw(self,screen):
        image_width = self.image.get_width()
        screen.blit(self.image, (self.x_pos_bg, self.y_pos_bg))
        screen.blit(self.image, (image_width + self.x_pos_bg, self.y_pos_bg))
        screen.blit(self.image, (image_width + self.x_pos_bg +  1500, self.y_pos_bg+ 200))
        if self.x_pos_bg <= -image_width:
            screen.blit(self.image, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 800
        self.x_pos_bg -= 10

    #pajaro sabe volar 
    def fly(self):
        #efect to run
        selected_image_index = random.randint(0,1)
        
        print("selected image is",selected_image_index)
        self.image = BIRD[selected_image_index]
    
    def update(self):
        self.fly()
