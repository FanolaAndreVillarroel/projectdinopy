#create a pygame program that show a boucing ball(pelota rebotando)
#Game is a class that hasmethods torun the logic for the bourcing ball

#main is responsible of creating an instance of class Game
#then it calls method run for the instance of class Game

#def -> define or create function , method class
from game import Game

if __name__ == "__main__":
    game = Game("hola",640,400) #create  instance(object)of class Game
    #call method tun using the "game"object(instance or variable)
    game.run()