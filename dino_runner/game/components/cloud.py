from game.utils.constants import CLOUD
class Cloud():
    def __init__(self):
        self.image = CLOUD
    
    def draw(self,screen,coord_x,coord_y):
        image_position = (coord_x,coord_y)
        screen.blit(self.image, image_position)

    def show(self):
        #selct image in selected
        print("selected image is",self.image)
        self.image = CLOUD

    def update(self):
        self.show()