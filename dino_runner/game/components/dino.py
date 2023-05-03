import pygame
import random
from game.utils.constants import RUNNING,DUCKING,JUMPING
class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.image = RUNNING[0]
        self.is_jumping = False
        self.jump_speed = 8.5
        self.jump_height = 20
        self.current_jump_height = 0
        
        
    #dino sabe dibujarse (pygame)
    def draw(self,screen,coord_x,coord_y):
        image_position = (coord_x,coord_y)
        screen.blit(self.image, image_position)
        

    #dino sabe correr 
    def run(self):
        #efect to run
        selected_image_index = random.randint(0,1)
        #selct image in selected_image_index
        print("selected image is",selected_image_index)
        self.image = RUNNING[selected_image_index]
    
    def duck(self):
        #efect ducking
        selected_image_index = random.randint(0,1)
        #selct image in selected_image_index
        print("selected image is",selected_image_index)
        self.image = DUCKING[selected_image_index]
        

    def jump (self):
        self.is_jumping = True
        if self.is_jumping:
                if self.current_jump_height >= self.jump_height:
                    self.current_jump_height = 0
                    self.is_jumping = False
                    self.image = RUNNING[0]
                else :
                    self.current_jump_height += self.jump_speed
                    self.image = JUMPING[0]

    
    def update(self,enter_user_date):
        
        self.run()

        if enter_user_date[pygame.K_DOWN]:
            
            self.duck()

        elif enter_user_date[pygame.K_UP]:
            
            self.jump()
            