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

from game import game_menu # Imports the game menu function
from button import Button # Handles UI button interations

from settings import WIDTH, HEIGHT # Screen dimensions
from settings import BLUE, BLACK, WHITE, GREEN, RED # Color constants
from settings import FONT_TEKO_BOLD, FONT_TEKO_LIGHT, FONT_TEKO_MEDIUM, FONT_TEKO_REGULAR, FONT_TEKO_SEMIBOLD, FONT_TEKO_SEMIBOLD_SMALL, FONT_TEKO_BOLD_SMALL # Font constantsd





pygame.init()

# Load background image
BG = pygame.image.load("assets/game_background_again.png")

def main_menu(screen):
    while True:
        screen.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #MENU_TEXT = FONT_TEKO_BOLD.render("THE ART OF CYBERSECURITY", True, "#b68f40")
        #MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH // 2, 150))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(WIDTH // 2, 550), 
                            text_input="PLAY", font=FONT_TEKO_SEMIBOLD, base_color=WHITE, hovering_color=BLUE)
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(WIDTH // 2, 700), 
                             text_input="QUIT", font=FONT_TEKO_SEMIBOLD, base_color=WHITE, hovering_color=BLUE)

        #screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_menu(screen)  # Start the game
                    return  # Return after playing the game
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()