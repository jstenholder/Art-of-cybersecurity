"""
Author: Jennifer Tenholder
Course: CS/PUBP/ECE-6727 - Cyber Security Practicum
Institution: Georgia Institute of Technology
Date: 2025-04-04

Project Name: The Gameification of Cybersecurity Awareness
"""

"""
This code defines the game menu . The user can select one of the four minigames to play
"""

'''Import statement(s)'''
import pygame # Game development library
import sys # Used for exiting the game

from button import Button # Handles UI button interations]

from minigames.painting_classification import painting_classification
from minigames.identity_verification import identity_verification
from minigames.key_change import key_change
from minigames.seek_and_find import seek_and_find

from settings import WIDTH, HEIGHT # Screen dimensions
from settings import BLUE, BLACK, WHITE, GREEN, RED # Color constants
from settings import FONT_TEKO_BOLD, FONT_TEKO_LIGHT, FONT_TEKO_MEDIUM, FONT_TEKO_REGULAR, FONT_TEKO_SEMIBOLD, FONT_TEKO_SEMIBOLD_SMALL, FONT_TEKO_BOLD_SMALL # Font constants

pygame.init() # Initializes pygame modules - Required for use

'''Game window definition'''
background_image = pygame.image.load("assets/background_main_and_game_menu.png")

'''Game menu definition'''
def game_menu(screen):

    '''Game loop'''
    while True:
        
        GAME_MENU_MOUSE_POS = pygame.mouse.get_pos() # Returns the current position of the mouse

        screen.blit(background_image, (0, 0)) # Displays the background image defined perviously

        '''
        Painting classification

        This adds everything relating to the painting classification game to the screen
        It adds a white background (Added for contrast with the game name), an icon for the game, and a button to actually select the game
        It also includes location references that the other parts use for their locations
        '''
        pygame.draw.rect(screen, WHITE, (235, 310, 330, 275))

        painting_classification_surface = pygame.image.load('assets/icon_painting_classification.png').convert_alpha()
        painting_classification_rect = painting_classification_surface.get_rect(center = (WIDTH / 2 - 200, HEIGHT / 6 + 300))
        screen.blit(painting_classification_surface,painting_classification_rect)

        painting_classification_topcenter_x,  painting_classification_topcenter_y =  painting_classification_rect.midtop
        painting_classification_bottomcenter_x,  painting_classification_bottomcenter_y =  painting_classification_rect.midbottom

        painting_classification_button = Button(image=None, pos=(painting_classification_topcenter_x, painting_classification_topcenter_y - 25), 
                                 text_input="Confidential Collection", font=FONT_TEKO_MEDIUM, 
                                 base_color="Black", hovering_color="Blue")

        '''
        Identity verification

        This adds everything relating to the identity verification game to the screen
        It adds a white background (Added for contrast with the game name), an icon for the game, and a button to actually select the game
        It also includes location references that the other parts use for their locations
        '''
        pygame.draw.rect(screen, WHITE, (635, 310, 330, 275))

        identity_verification_surface = pygame.image.load('assets/icon_identity_verification.png').convert_alpha()
        identity_verification_rect = identity_verification_surface.get_rect(center = (WIDTH / 2 + 200, HEIGHT / 6 + 300))
        screen.blit(identity_verification_surface,identity_verification_rect)

        identity_verification_topcenter_x,  identity_verification_topcenter_y =  identity_verification_rect.midtop
        identity_verification_bottomcenter_x,  identity_verification_bottomcenter_y =  identity_verification_rect.midbottom

        identity_verification_button = Button(image=None, pos=(identity_verification_topcenter_x, identity_verification_topcenter_y - 25), 
                                 text_input="Suspicious Shipments", font=FONT_TEKO_MEDIUM, 
                                 base_color="Black", hovering_color="Blue")
        
        '''
        Key change

        This adds everything relating to the key change game to the screen
        It adds a white background (Added for contrast with the game name), an icon for the game, and a button to actually select the game
        '''
        pygame.draw.rect(screen, WHITE, (235, 610, 330, 275)) 

        key_change_surface = pygame.image.load('assets/icon_key_change').convert_alpha()
        key_change_rect = key_change_surface.get_rect(center = (painting_classification_bottomcenter_x,  painting_classification_bottomcenter_y + 200))
        screen.blit(key_change_surface,key_change_rect)

        key_change_topcenter_x,  key_change_topcenter_y =  key_change_rect.midtop

        key_change_button = Button(image=None, pos=(key_change_topcenter_x, key_change_topcenter_y - 25), 
                            text_input="The Key to Security ", font=FONT_TEKO_MEDIUM, 
                            base_color="Black", hovering_color="Blue")

        '''
        Seek and find

        This adds everything relating to the seek and find game to the screen
        It adds a white background (Added for contrast with the game name), an icon for the game, and a button to actually select the game
        '''
        pygame.draw.rect(screen, WHITE, (635, 610, 330, 275))

        seek_and_find_surface = pygame.image.load('assets/icon_seek_and_find.png').convert_alpha()
        seek_and_find_rect = seek_and_find_surface.get_rect(center = (identity_verification_bottomcenter_x,  identity_verification_bottomcenter_y + 200))
        screen.blit(seek_and_find_surface,seek_and_find_rect)

        seek_and_find_topcenter_x,  seek_and_find_topcenter_y =  seek_and_find_rect.midtop

        seek_and_find_button = Button(image=None, pos=(seek_and_find_topcenter_x, seek_and_find_topcenter_y - 25), 
                             text_input="Museum Mayhem", font=FONT_TEKO_MEDIUM, 
                             base_color="Black", hovering_color="Blue")

        '''Adds a back button which can be used to navigate back to the main menu'''
        back_button = Button(image=None, pos=(WIDTH - 100, HEIGHT - 50), 
                             text_input="BACK", font=FONT_TEKO_BOLD_SMALL, 
                             base_color="Black", hovering_color="Blue")

        '''Handles updates for all the buttons'''
        for button in [painting_classification_button, identity_verification_button, key_change_button, seek_and_find_button, back_button]:
            button.changeColor(GAME_MENU_MOUSE_POS)
            button.update(screen)

        '''Defines what happens with the user interacts with the UI'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the user clicks the x button in the top right, close the game and exit
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(GAME_MENU_MOUSE_POS): # If the user clicks the back button, go to the main menu
                    from menu import main_menu
                    main_menu(screen)
                elif painting_classification_button.checkForInput(GAME_MENU_MOUSE_POS): # If the user clicks the painting classification button, go to that game
                    painting_classification(screen)
                elif identity_verification_button.checkForInput(GAME_MENU_MOUSE_POS): # If the user clicks the identity verification button, go to that game
                    identity_verification(screen)
                elif key_change_button.checkForInput(GAME_MENU_MOUSE_POS): # If the user clicks the key_change button, go to that game
                    key_change(screen)
                elif seek_and_find_button.checkForInput(GAME_MENU_MOUSE_POS): # If the user clicks the seek and find button, go to that game
                    seek_and_find(screen)

        pygame.display.update()