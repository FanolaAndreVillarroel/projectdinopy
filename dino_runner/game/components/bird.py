import random
from game.utils.constants import BIRD
class Bird:
    def __init__(self):
        
        self.image = BIRD[0]
    #bird sabe dibujarse (pygame)
    def draw(self,screen,coord_x,coord_y):
        image_position = (coord_x,coord_y)
        screen.blit(self.image, image_position)
        

    #pajaro sabe volar 
    def fly(self):
        #efect to run
        selected_image_index = random.randint(0,1)
        #selct image in selected_image_index
        print("selected image is",selected_image_index)
        self.image = BIRD[selected_image_index]
    
    def update(self):
        self.fly()
