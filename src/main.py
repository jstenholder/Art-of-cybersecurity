"""
Author: Jennifer Tenholder
Course: CS/PUBP/ECE-6727 - Cyber Security Practicum
Institution: Georgia Institute of Technology
Date: 2025-04-04

Project Name: The Gameification of Cybersecurity Awareness
"""

"""
This code defines main
If you wanted to run the whole code, run this file
"""

'''
Import statement(s)
'''

import pygame # Game development library

from menu import main_menu # Imports the main menu function

from settings import WIDTH, HEIGHT # Screen dimensions






screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Art of Cybersecurity")

main_menu(screen)

