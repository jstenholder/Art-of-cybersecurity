"""
Author: Jennifer Tenholder
Course: CS/PUBP/ECE-6727 - Cyber Security Practicum
Institution: Georgia Institute of Technology
Date: 2025-04-04

Project Name: The Gameification of Cybersecurity Awareness
"""

"""
This code defines constants that will be used throughout the game
"""

'''Import statement(s)'''
import pygame # Game development library

'''Defines the screen dimensions'''
WIDTH, HEIGHT = 1200, 1000

'''Defines colors'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)
GREEN = (50, 205, 50)
RED = (220, 20, 60)

'''Defines fonts'''
pygame.init() # Not sure why, but needs to be initialized here specifically
FONT = pygame.font.Font("fonts/font.ttf", 36)
FONT_TEKO_BOLD = pygame.font.Font("fonts/Teko-Bold.ttf", 100)
FONT_TEKO_BOLD_SMALL = pygame.font.Font("fonts/Teko-Bold.ttf", 40)
FONT_TEKO_LIGHT = pygame.font.Font("fonts/Teko-Light.ttf", 30)
FONT_TEKO_MEDIUM = pygame.font.Font("fonts/Teko-Medium.ttf", 36)
FONT_TEKO_REGULAR = pygame.font.Font("fonts/Teko-Regular.ttf", 36)
FONT_TEKO_SEMIBOLD = pygame.font.Font("fonts/Teko-SemiBold.ttf", 60)
FONT_TEKO_SEMIBOLD_SMALL = pygame.font.Font("fonts/Teko-SemiBold.ttf", 40)