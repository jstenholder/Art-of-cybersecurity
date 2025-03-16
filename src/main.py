import pygame
from menu import main_menu
from settings import WIDTH, HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Art of Cybersecurity")

main_menu(screen)

