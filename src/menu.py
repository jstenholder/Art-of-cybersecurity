"""
Author: Jennifer Tenholder
Course: CS/PUBP/ECE-6727 - Cyber Security Practicum
Institution: Georgia Institute of Technology
Date: 2025-04-04

Project Name: The Gameification of Cybersecurity Awareness
"""

"""
This code defines the main menu of the game. The user can select 'play' or close the game
"""

'''Import statement(s)'''
import pygame # Game development library
import sys # Used for exiting the game
import os # Used for getting the resource path

from game import game_menu # Imports the game menu function
from button import Button # Handles UI button interations

from settings import WIDTH, HEIGHT # Screen dimensions
from settings import BLUE, BLACK, WHITE, GREEN, RED # Color constants
from settings import FONT_TEKO_BOLD, FONT_TEKO_LIGHT, FONT_TEKO_MEDIUM, FONT_TEKO_REGULAR, FONT_TEKO_SEMIBOLD, FONT_TEKO_SEMIBOLD_SMALL, FONT_TEKO_BOLD_SMALL # Font constants

'''Get resource path'''
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller's temp dir
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init() # Initializes pygame modules - Required for use

'''Game window definition'''
background_image = pygame.image.load(resource_path("assets/background_main_and_game_menu.png")) 

'''Main menu definition'''
def main_menu(screen):

    '''Game loop'''
    while True:
        screen.blit(background_image, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        '''Defines buttons to play and quit the game'''

        button_image = pygame.image.load(resource_path("assets/button_background.png"))
        
        play_button_pos = (WIDTH // 2, 550)
        PLAY_BUTTON = Button(image=button_image,
                     pos=play_button_pos,
                     text_input="PLAY",
                     font=FONT_TEKO_SEMIBOLD,
                     base_color=WHITE,
                     hovering_color=BLUE)
        
        quit_button_pos = (WIDTH // 2, 700)
        QUIT_BUTTON = Button(image=button_image,
                     pos=quit_button_pos,
                     text_input="QUIT",
                     font=FONT_TEKO_SEMIBOLD,
                     base_color=WHITE,
                     hovering_color=BLUE)

        
        '''PLAY_BUTTON = Button(image=pygame.image.load(resource_path("assets/button_background.png"), pos=(WIDTH // 2, 550)), 
                            text_input="PLAY", font=FONT_TEKO_SEMIBOLD, base_color=WHITE, hovering_color=BLUE)
        QUIT_BUTTON = Button(image=pygame.image.load(resource_path("assets/button_background.png"), pos=(WIDTH // 2, 700)), 
                             text_input="QUIT", font=FONT_TEKO_SEMIBOLD, base_color=WHITE, hovering_color=BLUE)
'''
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        '''Defines what happens with the user interacts with the UI'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the user clicks the x button in the top right, close the game and exit
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS): # If the user clicks the play button, the game_menu screen is displayed
                    game_menu(screen)
                    return
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): # If the user clicks the quit button, close the game and exit
                    pygame.quit()
                    sys.exit()

        pygame.display.update()