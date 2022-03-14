import random
import pygame
from game import *
from settings import *
from player import *
from monster import *

#Initialize pygame
pygame.init()

#Create a player group and player object
player_group = pygame.sprite.Group()
player = Player()
player_group.add(player)

#Create a monster group. Monsters will be added by start_new_round method.
monster_group = pygame.sprite.Group()

#Create a game object
game = Game(player, monster_group)
game.pause_game("Monster Wrangler", "Press 'Enter' to begin")
game.start_new_round()
#The main game loop
running = True
while running:

    #Check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Player wants to warp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.warp()

    #Fill the display
    display_surface.fill((0,0,0))

    #Update and draw sprite groups
    player_group.update()
    player_group.draw(display_surface)

    monster_group.update()
    monster_group.draw(display_surface)

    #Update and draw the game
    game.update()
    game.draw()

    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()

