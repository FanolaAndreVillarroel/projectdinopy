import pygame
import random
from game.utils.constants import RUNNING,DUCKING,JUMPING

class Dinosaur:
    #Valores
    X_POSITION = 80
    Y_POSITION = 310
    Y_POSITION_DUCK =340
    jUMP_VEL = 8.5
    def __init__(self,name):
        self.name = name
        
        #imagenes que utilizaremos 
        self.run_image = RUNNING
        self.duck_image = DUCKING
        self.jump_image = JUMPING

        #Inicia corriendo
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_selected_image_index = 0
        self.jump_vel = self.jUMP_VEL
        self.image =self.run_image[0]
        #Definos dino_rect
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POSITION
        self.dino_rect.y = self.Y_POSITION


        

        
    #dino sabe dibujarse (pygame)
    def draw(self,screen):
        image_position = (self.dino_rect.x,self.dino_rect.y)
        screen.blit(self.image,image_position)
        

    #dino sabe correr 
    def run(self):
        #efect to run
        #selected_image_index = random.randint(0,1)
        #selct image in selected_image_index
        #print("selected image is",selected_image_index)
        self.image = self.run_image[self.step_selected_image_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POSITION
        self.dino_rect.y = self.Y_POSITION
        self.step_selected_image_index += 1
    
    def duck(self):
        #efect ducking
        #selected_image_index = random.randint(0,1)
        #selct image in selected_image_index
        #print("selected image is",selected_image_index)

        self.image = self.duck_image[self.step_selected_image_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POSITION
        self.dino_rect.y = self.Y_POSITION_DUCK
        self.step_selected_image_index += 1

    #Sabe saltar
    def jump(self):
        self.image = self.jump_image
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < - self.jUMP_VEL:
            self.dino_rect.y = self.Y_POSITION
            self.dino_jump = False
            self.jump_vel = self.jUMP_VEL
        
        

    def update(self,enter_user_date):
        if self.dino_run:
            self.run()
            self.dino_status = "Run"

        if self.dino_duck:
            self.duck()
            self.dino_status = "Duck"

        if self.dino_jump:
            self.jump()
            self.dino_status = "jump"

        if self.step_selected_image_index >= 10:
            self.step_selected_image_index = 0

        if enter_user_date[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif enter_user_date[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or enter_user_date[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False    
