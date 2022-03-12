import pygame

#Initialize pygame
pygame.init()

#Setup game window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monster Wrangler")

#Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#Define Classes
class Game():
    """A class to control gameplay"""
    def __init__(self):
        """Initialize the game object"""
        pass

    def update(self):
        """Update our game object"""
        pass

    def draw(self):
        """Draw the HUD and other things to the display"""
        pass

    def check_collisions(self):
        """Check for collisions between players and monsters"""
        pass

    def start_new_round(self):
        """Populate board with new monsters"""
        pass

    def choose_new_target(self):
        """Choose a new target monster for the player"""
        pass

    def pause_game(self):
        """Pause the game"""
        pass

    def reset_game(self):
        """Reset the game"""
        pass

class Player(pygame.sprite.Sprite):
    """A player class that the user can control"""
    def __init__(self):
        """Initialize the player"""
        pass

    def update(self):
        """Update the player"""
        pass

    def warp(self):
        """Warps the player to safety at the bottom of the screen"""
        pass

    def reset_player(self):
        """Reset the player to the original starting position"""
        pass

class Monster(pygame.sprite.Sprite):
    """A class to create enemy monster objects"""
    def __init__(self):
        """Initialize the monster"""
        pass

    def update(self):
        """Update the monster"""
        pass


#The main game loop
running = True
while running:

    #Check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()

