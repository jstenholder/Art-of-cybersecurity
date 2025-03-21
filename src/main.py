import pygame
from menu import main_menu
from settings import WIDTH, HEIGHT, FONT_TEKO_BOLD, FONT_TEKO_LIGHT, FONT_TEKO_MEDIUM, FONT_TEKO_REGULAR, FONT_TEKO_SEMIBOLD

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Art of Cybersecurity")

main_menu(screen)

