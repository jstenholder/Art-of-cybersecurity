import pygame, sys
from button import Button
from settings import WIDTH, HEIGHT, WHITE

pygame.init()

def start_painting_classification(screen):
    from minigames.painting_classification import painting_classification
    painting_classification(screen)

def start_identity_verification(screen):
    from minigames.identity_verification import identity_verification
    identity_verification(screen)

def start_key_change(screen):
    from minigames.key_change import key_change
    key_change(screen)

def start_seek_and_find(screen):
    from minigames.seek_and_find import seek_and_find
    seek_and_find(screen)

def game_menu(screen):
    while True:
        screen.fill(WHITE)
        GAME_MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Create buttons for all minigames
        painting_button = Button(image=None, pos=(WIDTH // 2, HEIGHT // 5), 
                                 text_input="Painting Classification", font=pygame.font.Font(None, 36), 
                                 base_color="Black", hovering_color="Blue")

        identity_button = Button(image=None, pos=(WIDTH // 2, HEIGHT // 5 + 75), 
                                 text_input="Identity Verification", font=pygame.font.Font(None, 36), 
                                 base_color="Black", hovering_color="Blue")

        key_button = Button(image=None, pos=(WIDTH // 2, HEIGHT // 5 + 150), 
                            text_input="Key Change", font=pygame.font.Font(None, 36), 
                            base_color="Black", hovering_color="Blue")

        seek_button = Button(image=None, pos=(WIDTH // 2, HEIGHT // 5 + 225), 
                             text_input="Seek and Find", font=pygame.font.Font(None, 36), 
                             base_color="Black", hovering_color="Blue")

        back_button = Button(image=None, pos=(WIDTH - 150, HEIGHT - 75), 
                             text_input="BACK", font=pygame.font.Font(None, 50), 
                             base_color="Green", hovering_color="Red")

        # Update all buttons
        for button in [painting_button, identity_button, key_button, seek_button, back_button]:
            button.changeColor(GAME_MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(GAME_MENU_MOUSE_POS):
                    from menu import main_menu
                    main_menu(screen)
                elif painting_button.checkForInput(GAME_MENU_MOUSE_POS):
                    start_painting_classification(screen)
                elif identity_button.checkForInput(GAME_MENU_MOUSE_POS):
                    start_identity_verification(screen)
                elif key_button.checkForInput(GAME_MENU_MOUSE_POS):
                    start_key_change(screen)
                elif seek_button.checkForInput(GAME_MENU_MOUSE_POS):
                    start_seek_and_find(screen)

        pygame.display.update()