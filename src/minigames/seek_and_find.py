"""
Author: Jennifer Tenholder
Course: CS/PUBP/ECE-6727 - Cyber Security Practicum
Institution: Georgia Institute of Technology
Date: 2025-04-04

Project Name: The Gameification of Cybersecurity Awareness
"""

"""
This code defines the Seek and Find minigame (referred to as 'Museum Mayhem' in-game)
More details on actual implementation and logic can be found below
"""

'''Import statement(s)'''
import pygame # Game development library
import sys # Used for exiting the game

from button import Button # Handles UI button interations

from settings import WIDTH, HEIGHT # Screen dimensions
from settings import BLUE, BLACK, WHITE, GREEN, RED # Color constants
from settings import FONT_TEKO_BOLD, FONT_TEKO_LIGHT, FONT_TEKO_MEDIUM, FONT_TEKO_REGULAR, FONT_TEKO_SEMIBOLD, FONT_TEKO_SEMIBOLD_SMALL, FONT_TEKO_BOLD_SMALL # Font constants

pygame.init() # Initializes pygame modules - Required for use

'''Game window definition'''
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Museum Mayhem")
background_image = pygame.image.load("assets/background_seek_and_find.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

'''
Defines items and their locations

These are the items that the user will be "searching for" in the game
'''
items = [
    ("phone", (215, 840, 76, 54)),
    ("ID", (113, 332, 88, 42)),
    ("mouse", (855, 573, 65, 37)),
    ("lucky purple paper clip", (751, 805, 27, 43)),
    ("sticky note with a deadline", (938, 288, 83, 88)),
]

'''
Defines hidden items and their locations

These are the extra items that a user could find in the game
'''
hidden_items = [
    ("computer", (422, 276, 426, 76), "I can't believe I left my computer unlocked. How un-safe of me! Thanks for letting me know"), # done
    ("document", (263, 352, 161, 198), "If my boss knew I left that document out, they'd have my job. Thanks for letting me know"), # done
    ("password", (467, 523, 86, 88), "I completely forgot to shred that. Thanks for letting me know"), # done
    ("flash_drive", (1110, 452, 70, 51), "I don't recognize this. I think I need to report this to IT. Thanks for letting me know"), # done
]

'''
Defines variables and buttons

show_message - Controls when the text bubble appears
found - Controls message state
message_timer - Controls success message duration
success_message - Track success message separately
hidden_message - Shows if a hidden message is found
current_item - What item is currently being searched for
items_found - Count of how many items have been found
hidden_items_found - Count of how many hidden items have been found

back_button - Defines the details of the back button
'''
show_message = True
found = False
message_timer = 0
success_message = ""
hidden_message = ""
current_item = 0
items_found = 0
hidden_items_found = 0

back_button = Button(image=None, pos=(WIDTH - 100, HEIGHT - 50), text_input="BACK", font=FONT_TEKO_SEMIBOLD_SMALL, base_color=BLACK, hovering_color=BLUE)

'''
Displays and instructions page

Explains the rules of the game and how to play
User can close out of it by clicking anywhere or hitting any key
'''
def show_instructions():
    """Display instructions and wait for user input to proceed."""
    instruction_text = [
        "Welcome to the Seek and Find Minigame!",
        "",
        "One of your fellow employees asks you to go to their desk to look for some things they've lost",
        "Search the scene to help them find their missing items",
        "As a security champion for the museum, report any unsafe security practices you find",
        "We've also been seeing some suspiciouis activities lately so keep your eye out for those",
        "",
        "Good luck",
        "",
        "Press any key to continue..."
    ]

    while True:
        '''Display the instructions on a white box outlined in black'''
        pygame.draw.rect(screen, WHITE, (200, 200, 800, 600))  # White background box
        pygame.draw.rect(screen, BLACK, (200, 200, 800, 600), 3)  # Black outline

        y = 350
        for line in instruction_text:
            text_surface = FONT_TEKO_LIGHT.render(line, True, BLACK)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
            screen.blit(text_surface, text_rect)
            y += 35 # Stars at y = 250, but adds 50 to the y value each time to draw text on a separate line

        pygame.display.flip()

        '''Waits for user to click their mouse or press a key to proceed'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return

'''
Resets the game values to the beginning

Prior to this, if the user selected the game again, they would been shown the final landing page
'''
def reset_seek_and_find():
    global show_message, found, message_timer, success_message, hidden_message, current_item, items_found, hidden_items_found
    show_message = True
    found = False
    message_timer = 0
    success_message = ""
            
def seek_and_find(screen):

    global show_message, found, message_timer, success_message, hidden_message, current_item, items_found, hidden_items_found
    screen.blit(background_image, (0, 0))
    reset_seek_and_find() # Resets game to its initial state
    show_instructions() # Shows the user the instruction page
      
    '''Game loop'''
    running = True
    while running:
        screen.blit(background_image, (0, 0))

        '''Defines what happens with the user interacts with the UI'''
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # If the user clicks the x button in the top right, close the game and exit
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if items_found == len(items) and back_button.checkForInput((mouse_x, mouse_y)): # If the back button is clicked and all items have been found, go back to the game menu
                    from game import game_menu
                    game_menu(screen)

                '''Check if a hidden item is clicked'''
                hidden_message_displayed = False
                for hidden_name, (hx, hy, hw, hh), message in hidden_items:
                    if hx <= mouse_x <= hx + hw and hy <= mouse_y <= hy + hh:
                        hidden_message = message
                        hidden_message_displayed = True
                        hidden_items_found += 1
                        break

                '''If no hidden item was clicked, clear the hidden message'''
                if not hidden_message_displayed:
                    hidden_message = ""

                '''Check if the correct main item is clicked'''
                if not found and not hidden_message_displayed:
                    item_name, (x, y, w, h) = items[current_item]
                    if x <= mouse_x <= x + w and y <= mouse_y <= y + h:
                        found = True
                        items_found += 1
                        show_message = True
                        success_message = f"Awesome! Thank you for finding my {items[current_item][0]}!"
                        message_timer = pygame.time.get_ticks()  # Start timer for success message

        '''Display the user prompt'''
        if show_message:
            if not found:
                text = f"Can you help me find my {items[current_item][0]}?"
            else:
                text = success_message  # Ensure the success message is stored and displayed correctly

            text_surface = FONT_TEKO_MEDIUM.render(text, True, BLACK)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, 50))
            screen.blit(text_surface, text_rect)
        
        '''Display the found item count in the top left corner'''
        score_surface = FONT_TEKO_LIGHT.render(f"Items found: {items_found}/{len(items)}",False,'Black').convert_alpha()
        score_rect = score_surface.get_rect(midleft = (25, 20))
        screen.blit(score_surface,score_rect)
        
        '''Display the hidden item count in the top right corner'''
        score_surface = FONT_TEKO_LIGHT.render(f"Hidden items found: {hidden_items_found}",False,'Black').convert_alpha()
        score_rect = score_surface.get_rect(midright = (1175, 20))
        screen.blit(score_surface,score_rect)

        ''' Display hidden item message if one is found'''
        if hidden_message:
            hidden_surface = FONT_TEKO_MEDIUM.render(hidden_message, True, BLUE)
            hidden_rect = hidden_surface.get_rect(center=(WIDTH // 2, 100))
            screen.blit(hidden_surface, hidden_rect)

        '''Display back button if all items are found'''
        if items_found == len(items):
            back_button.update(screen)

        '''Advance to next item when the message has been shown for some time'''
        if found and pygame.time.get_ticks() - message_timer > 1000:
            found = False  # Reset state
            show_message = True  # Ensure the next prompt appears
            current_item += 1  # Move to the next item
            if current_item >= len(items):
                current_item = len(items)  # Prevent index errors
                show_message = False  # Hide item search message
                success_message = "You found all the items! Great job!"

        pygame.display.flip()