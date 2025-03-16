import pygame, random, sys
from settings import WIDTH, HEIGHT, BLUE, BLACK, WHITE, GREEN, RED
from button import Button
from settings import FONT

# Initialize Pygame
pygame.init()


# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seek and Find Game")

# Load background image
background = pygame.image.load("assets/seek_and_find1.png")  # Replace with your image file
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Font setup
font = pygame.font.Font(None, 36)

# Define items to find (name, correct click area as (x, y, width, height))
items = [
    ("phone", (215, 790, 78, 54)),
    ("ID", (117, 268, 87, 57)),
]

current_item = 0
items_found = 0

# Define hidden items with special messages
hidden_items = [
    ("computer", (424, 226, 424, 75), "Oh my gosh. I can't believe I left my computer unlocked. How un-safe of me! Good catch!"),
]
hidden_message = ""

# Game loop variables
running = True
show_message = True  # Controls when the text bubble appears
found = False  # Controls message state
message_timer = 0  # Timer to control success message duration
success_message = ""  # Track success message separately

# Back button setup
back_button = Button(image=None, pos=(WIDTH - 150, HEIGHT - 75), text_input="BACK", font=FONT, base_color="Green", hovering_color="Red")

while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if back button is clicked
            if items_found == len(items) and back_button.checkForInput((mouse_x, mouse_y)):
                from game import game_menu  # Adjust this import as per your project structure
                game_menu(screen)  # Replace with the appropriate function to go back to menu

            # Check if a hidden item is clicked
            hidden_message_displayed = False
            for hidden_name, (hx, hy, hw, hh), message in hidden_items:
                if hx <= mouse_x <= hx + hw and hy <= mouse_y <= hy + hh:
                    hidden_message = message
                    hidden_message_displayed = True
                    break

            # If no hidden item was clicked, clear the hidden message
            if not hidden_message_displayed:
                hidden_message = ""

            # Check if the correct main item is clicked
            if not found and not hidden_message_displayed:
                item_name, (x, y, w, h) = items[current_item]
                if x <= mouse_x <= x + w and y <= mouse_y <= y + h:
                    found = True  # Correct item found
                    items_found += 1
                    show_message = True  # Show success message
                    success_message = f"Awesome! Thank you for finding my {items[current_item][0]}!"
                    message_timer = pygame.time.get_ticks()  # Start timer for success message

    # Display text bubble
    if show_message:
        if not found:
            text = f"Can you help me find my {items[current_item][0]}?"
        else:
            text = success_message  # Ensure the success message is stored and displayed correctly

        text_surface = font.render(text, True, (255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), (50, 50, text_surface.get_width() + 20, 40))
        screen.blit(text_surface, (60, 60))

    # Display hidden item message if found
    if hidden_message:
        hidden_surface = font.render(hidden_message, True, (255, 255, 255))
        pygame.draw.rect(screen, (50, 50, 50), (50, 100, hidden_surface.get_width() + 20, 40))
        screen.blit(hidden_surface, (60, 110))

    # Display back button if all items are found
    if items_found == len(items):
        back_button.update(screen)

    # Advance to next item when the message has been shown for some time
    if found and pygame.time.get_ticks() - message_timer > 1000:
        found = False  # Reset state
        show_message = True  # Ensure the next prompt appears
        current_item += 1  # Move to the next item
        if current_item >= len(items):
            current_item = len(items)  # Prevent index errors
            show_message = False  # Hide item search message
            success_message = "You found all the items! Great job!"

    pygame.display.flip()

pygame.quit()