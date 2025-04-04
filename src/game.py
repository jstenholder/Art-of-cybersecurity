import pygame, sys
from button import Button
from settings import WIDTH, HEIGHT, BLUE, BLACK, WHITE, GREEN, RED, FONT_TEKO_BOLD, FONT_TEKO_LIGHT, FONT_TEKO_MEDIUM, FONT_TEKO_REGULAR, FONT_TEKO_SEMIBOLD, FONT, FONT_TEKO_BOLD_SMALL

pygame.init()

def start_painting_classification(screen):
    if 'minigames.painting_classification' not in sys.modules:
        from minigames.painting_classification import painting_classification

    painting_classification(screen)

def start_identity_verification(screen):
    if 'minigames.identity_verification' not in sys.modules:
        from minigames.identity_verification import identity_verification

    identity_verification(screen)

def start_key_change(screen):
    if 'minigames.key_change' not in sys.modules:
        from minigames.key_change import key_change

    key_change(screen)

def start_seek_and_find(screen):
    from minigames.seek_and_find import seek_and_find
    seek_and_find(screen)

background_image = pygame.image.load("assets/game_background_again.png")  # CHANGED

def game_menu(screen):
    while True:
        
        GAME_MENU_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(background_image, (0, 0))  # CHANGED

        #results_surface2 = FONT_TEKO_SEMIBOLD.render("MINIGAMES",False,'Black').convert_alpha()
        #results_rect2 = results_surface2.get_rect(center = (WIDTH // 2, 75))
        #screen.blit(results_surface2,results_rect2)

        # Create buttons for all minigames
    
        #painting_classification_display = pygame.Rect(0, 0, 300, 200)  # Adjust size and position as needed
        #painting_classification_display.center = (WIDTH / 2 - 200, HEIGHT / 6 + 300)
        #pygame.draw.rect(screen, BLUE, painting_classification_display)  # Background color
        #pygame.draw.rect(screen, BLACK, painting_classification_display, 3)  # Border

        pygame.draw.rect(screen, WHITE, (235, 310, 330, 275))  # White background box

        painting_classification_surface = pygame.image.load('assets/painting_classification_icon_again.png').convert_alpha()
        painting_classification_rect = painting_classification_surface.get_rect(center = (WIDTH / 2 - 200, HEIGHT / 6 + 300))
        screen.blit(painting_classification_surface,painting_classification_rect)

        painting_classification_topcenter_x,  painting_classification_topcenter_y =  painting_classification_rect.midtop
        painting_classification_bottomcenter_x,  painting_classification_bottomcenter_y =  painting_classification_rect.midbottom

        painting_button = Button(image=None, pos=(painting_classification_topcenter_x, painting_classification_topcenter_y - 25), 
                                 text_input="Confidential Collection", font=FONT_TEKO_MEDIUM, 
                                 base_color="Black", hovering_color="Blue")
        
        
        #identity_verification_display = pygame.Rect( 0,  0, 300, 200)  # Adjust size and position as needed
        #identity_verification_display.center = (WIDTH / 2 + 200, HEIGHT / 6 + 300)
        #pygame.draw.rect(screen, BLUE,  identity_verification_display)  # Background color
        #pygame.draw.rect(screen, BLACK,  identity_verification_display, 3)  # Border

        pygame.draw.rect(screen, WHITE, (635, 310, 330, 275))  # White background box

        identity_verification_surface = pygame.image.load('assets/identity_verification_icon.png').convert_alpha()
        identity_verification_rect = identity_verification_surface.get_rect(center = (WIDTH / 2 + 200, HEIGHT / 6 + 300))
        screen.blit(identity_verification_surface,identity_verification_rect)

        identity_verification_topcenter_x,  identity_verification_topcenter_y =  identity_verification_rect.midtop
        identity_verification_bottomcenter_x,  identity_verification_bottomcenter_y =  identity_verification_rect.midbottom

        identity_button = Button(image=None, pos=(identity_verification_topcenter_x, identity_verification_topcenter_y - 25), 
                                 text_input="Suspicious Shipments", font=FONT_TEKO_MEDIUM, 
                                 base_color="Black", hovering_color="Blue")
        
        #key_change_display = pygame.Rect(0, 0, 300, 200)  # Adjust size and position as needed
        #key_change_display.center = (painting_classification_bottomcenter_x,  painting_classification_bottomcenter_y + 200)
        #pygame.draw.rect(screen, BLUE, key_change_display)  # Background color
        #pygame.draw.rect(screen, BLACK, key_change_display, 3)  # Border

        pygame.draw.rect(screen, WHITE, (235, 610, 330, 275))  # White background box

        key_change_surface = pygame.image.load('assets/key_change_icon.png').convert_alpha()
        key_change_rect = key_change_surface.get_rect(center = (painting_classification_bottomcenter_x,  painting_classification_bottomcenter_y + 200))
        screen.blit(key_change_surface,key_change_rect)

        key_change_topcenter_x,  key_change_topcenter_y =  key_change_rect.midtop

        key_button = Button(image=None, pos=(key_change_topcenter_x, key_change_topcenter_y - 25), 
                            text_input="The Key to Security ", font=FONT_TEKO_MEDIUM, 
                            base_color="Black", hovering_color="Blue")

        
        #seek_and_find_display = pygame.Rect( 0,  0, 300, 200)  # Adjust size and position as needed
        #seek_and_find_display.center = (identity_verification_bottomcenter_x,  identity_verification_bottomcenter_y + 200)
        #pygame.draw.rect(screen, BLUE,  seek_and_find_display)  # Background color
        #pygame.draw.rect(screen, BLACK,  seek_and_find_display, 3)  # Border

        pygame.draw.rect(screen, WHITE, (635, 610, 330, 275))  # White background box

        seek_and_find_surface = pygame.image.load('assets/seek_and_find_icon.png').convert_alpha()
        seek_and_find_rect = seek_and_find_surface.get_rect(center = (identity_verification_bottomcenter_x,  identity_verification_bottomcenter_y + 200))
        screen.blit(seek_and_find_surface,seek_and_find_rect)

        seek_and_find_topcenter_x,  seek_and_find_topcenter_y =  seek_and_find_rect.midtop

        seek_button = Button(image=None, pos=(seek_and_find_topcenter_x, seek_and_find_topcenter_y - 25), 
                             text_input="Museum Mayhem", font=FONT_TEKO_MEDIUM, 
                             base_color="Black", hovering_color="Blue")

        back_button = Button(image=None, pos=(WIDTH - 150, HEIGHT - 75), 
                             text_input="BACK", font=FONT_TEKO_BOLD_SMALL, 
                             base_color="Black", hovering_color="Blue")

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