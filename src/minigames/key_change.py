"""
Author: Jennifer Tenholder
Course: CS/PUBP/ECE-6727 - Cyber Security Practicum
Institution: Georgia Institute of Technology
Date: 2025-04-04

Project Name: The Gameification of Cybersecurity Awareness
"""

"""
This code defines the Key Change minigame (referred to as 'The Key to Security' in-game)
More details on actual implementation and logic can be found below
"""

'''Import statement(s)'''
import pygame # Game development library
import random # Used for selecting items/questions
import sys # Used for exiting the game

from button import Button # Handles UI button interations

from settings import WIDTH, HEIGHT # Screen dimensions
from settings import BLUE, BLACK, WHITE, GREEN, RED # Color constants
from settings import FONT_TEKO_BOLD, FONT_TEKO_LIGHT, FONT_TEKO_MEDIUM, FONT_TEKO_REGULAR, FONT_TEKO_SEMIBOLD, FONT_TEKO_SEMIBOLD_SMALL, FONT_TEKO_BOLD_SMALL # Font constants

pygame.init() # Initializes pygame modules - Required for use

'''Game window definition'''
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Key to Security")
background_images = [ # uses multiple background images throughout the game
    pygame.image.load("assets/diamond_and_asteroid.png"),
    pygame.image.load("assets/asteroid_and_shell_fossil.png"),
    pygame.image.load("assets/shell_fossil_and_sword.png"),
    pygame.image.load("assets/diamond_and_map.png"),
    pygame.image.load("assets/map_and_vase.png"),
    pygame.image.load("assets/vase_and_fish_fossil.png")
]



# Load images
key_images = [
    pygame.image.load("assets/key1.png"),
    pygame.image.load("assets/key2.png"),
    pygame.image.load("assets/key3.png"),
    pygame.image.load("assets/key4.png"),
    pygame.image.load("assets/key5.png"),
    pygame.image.load("assets/key6.png"),
    pygame.image.load("assets/key7.png"),
    pygame.image.load("assets/key8.png"),
    pygame.image.load("assets/key9.png"),
    pygame.image.load("assets/key10.png"),
    pygame.image.load("assets/key11.png"),
    pygame.image.load("assets/key12.png"),
    pygame.image.load("assets/key13.png"),
    pygame.image.load("assets/key14.png"),
    pygame.image.load("assets/key15.png"),
    pygame.image.load("assets/key16.png"),
    pygame.image.load("assets/key17.png"),
    pygame.image.load("assets/key18.png"),
    pygame.image.load("assets/key19.png"),
    pygame.image.load("assets/key20.png")
]

key_information = [
    {"image": key_images[0], "choices": ["Secure", "Insecure"], "answer": 1, "explanation": "I'm not so sure about this one. I doesn't look complex enough"},
    {"image": key_images[1], "choices": ["Secure", "Insecure"], "answer": 0, "explanation": "Looks good to me! Good job!"},
    {"image": key_images[2], "choices": ["Secure", "Insecure"], "answer": 0, "explanation": "Looks good to me! Good job!"},
    {"image": key_images[3], "choices": ["Secure", "Insecure"], "answer": 1, "explanation": "I'm not so sure about this one. I doesn't look complex enough"},
    {"image": key_images[4], "choices": ["Secure", "Insecure"], "answer": 1, "explanation": "I'm not so sure about this one. I doesn't look complex enough"},
    {"image": key_images[5], "choices": ["Secure", "Insecure"], "answer": 0, "explanation": "Looks good to me! Good job!"},
    {"image": key_images[6], "choices": ["Secure", "Insecure"], "answer": 1, "explanation": "I'm not so sure about this one. I doesn't look complex enough"},
    {"image": key_images[7], "choices": ["Secure", "Insecure"], "answer": 1, "explanation": "I'm not so sure about this one. I doesn't look complex enough"},
    {"image": key_images[8], "choices": ["Secure", "Insecure"], "answer": 1, "explanation": "I'm not so sure about this one. I doesn't look complex enough"},
    {"image": key_images[9], "choices": ["Secure", "Insecure"], "answer": 1, "explanation": "I'm not so sure about this one. I doesn't look complex enough"},
    {"image": key_images[10], "choices": ["Secure", "Insecure"], "answer": 0, "explanation": "Looks good to me! Good job!"},
    {"image": key_images[11], "choices": ["Secure", "Insecure"], "answer": 1, "explanation": "I'm not so sure about this one. I doesn't look complex enough"},
    {"image": key_images[12], "choices": ["Secure", "Insecure"], "answer": 0, "explanation": "Looks good to me! Good job!"},
    {"image": key_images[13], "choices": ["Secure", "Insecure"], "answer": 1, "explanation": "I'm not so sure about this one. I doesn't look complex enough"},
    {"image": key_images[14], "choices": ["Secure", "Insecure"], "answer": 0, "explanation": "Looks good to me! Good job!"},
    {"image": key_images[15], "choices": ["Secure", "Insecure"], "answer": 0, "explanation": "Looks good to me! Good job!"},
    {"image": key_images[16], "choices": ["Secure", "Insecure"], "answer": 0, "explanation": "Looks good to me! Good job!"},
    {"image": key_images[17], "choices": ["Secure", "Insecure"], "answer": 1, "explanation": "I'm not so sure about this one. I doesn't look complex enough"},
    {"image": key_images[18], "choices": ["Secure", "Insecure"], "answer": 0, "explanation": "Looks good to me! Good job!"},
    {"image": key_images[19], "choices": ["Secure", "Insecure"], "answer": 0, "explanation": "Looks good to me! Good job!"}
]


# Game state
global KEY_CHANGE_MOUSE_POS
KEY_CHANGE_MOUSE_POS = pygame.mouse.get_pos()
global rounds_played
rounds_played = 0
max_rounds = 10
global score
score = 0
selected_answer = -1
global show_result
show_result = False
global show_next_button
show_next_button = False
global message
message = ""
global current_keys
global key_positions
key_positions = []

global back_button
back_button = Button(image=None, pos=(WIDTH - 150, HEIGHT - 75), text_input="BACK", font=FONT_TEKO_SEMIBOLD_SMALL, base_color="Green", hovering_color="Red")
back_button.changeColor(KEY_CHANGE_MOUSE_POS)

def select_new_keys():
    global current_keys
    current_keys = random.sample(key_information, 4)
    # Ensure at least one key is secure
    if not any(k["answer"] == 0 for k in current_keys):  
        secure_key = random.choice([k for k in key_information if k["answer"] == 0])
        current_keys[random.randint(0, 3)] = secure_key

# Initial selection
select_new_keys()

# Function to check if a key is clicked


def check_key_click(pos):
    global selected_answer, show_result, show_next_button, rounds_played, message, score, key_positions  # Used to access the global variables

    for key_rect, key in key_positions:
        if key_rect.collidepoint(pos): 
            selected_answer = key["answer"]
            show_result = True
            show_next_button = True

            if selected_answer == 0:
                message = key["explanation"]
                score += 1
                
            else:
                message = key["explanation"]
                rounds_played += 1 

            rounds_played += 1     

# Initialize game state
game_state = "instructions"  # Start with the instructions screen

def show_instructions():
    """Display instructions and wait for user input to proceed."""
    instruction_text = [
        "Welcome to Key Change Minigame!",
        "As part of the security procedures, we need to go around and change some keys on exhibits",
        "Instructions:",
        "- For each of the exhibits, select a new secure key",
        "- Secure keys must meet the following criteria",
        "  - The key must have all three groove types",
        "  - The key cannot have more than two of the same grooves in a row",
        "  - The key must have at least fourteen notches",
        "Press any key to continue..."
    ]

    while True:
        screen.fill(WHITE)  # Clear the screen

        # Draw instructions box
        pygame.draw.rect(screen, WHITE, (200, 200, 800, 600))  # White background box
        pygame.draw.rect(screen, BLACK, (200, 200, 800, 600), 3)  # Black outline

        # Render instructions text
        y = 250
        for line in instruction_text:
            text_surface = FONT_TEKO_REGULAR.render(line, True, BLACK)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
            screen.blit(text_surface, text_rect)
            y += 50

        pygame.display.flip()

        # Wait for user input to proceed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # Exit function when a key or mouse click is detected


def reset_key_change():
    global current_question, selected_answer, show_result, show_next_button, score, rounds_played, key_positions
    current_question = random.randint(0, len(key_information) - 1)
    selected_answer = -1
    show_result = False
    show_next_button = False
    score = 0  # Reset score
    rounds_played = 0  # Reset round counter
            
def key_change(screen):
    global current_question, selected_answer, show_result, show_next_button, score, max_rounds, rounds_played, key_positions
    reset_key_change()

    # Show instructions before starting the game loop
    show_instructions()       

    '''Game loop'''
    running = True
    while running:
        
        KEY_CHANGE_MOUSE_POS = pygame.mouse.get_pos()
        key_positions.clear()
        
        # CHANGED: Choose background image based on rounds played (changes every 2 rounds)
        background_index = (rounds_played // 2) % len(background_images)
        screen.blit(background_images[background_index], (0, 0))

        if rounds_played >= max_rounds:

            if score < 5:
                pygame.draw.rect(screen, WHITE, (250, 400, 700, 200))
                results_surface2 = FONT_TEKO_MEDIUM.render("Definitely not as secure as we typically want to be...",False,'Black').convert_alpha()
                results_rect2 = results_surface2.get_rect(center = (WIDTH // 2, HEIGHT // 2))
                screen.blit(results_surface2,results_rect2)

                results_surface1 = FONT_TEKO_MEDIUM.render("You've changed all the keys", False, 'Black').convert_alpha()
                results_rect1 = results_surface1.get_rect(center=(WIDTH // 2, results_rect2.centery - 50))
                screen.blit(results_surface1, results_rect1)

                results_surface3 = FONT_TEKO_BOLD_SMALL.render(f"Final Score: {score} / {int(max_rounds / 2)}", False, 'Black').convert_alpha()
                results_rect3 = results_surface3.get_rect(center=(WIDTH // 2, results_rect2.centery + 50))
                screen.blit(results_surface3, results_rect3)

                back_button.update(screen)

            else:
                pygame.draw.rect(screen, WHITE, (250, 400, 700, 200))
                results_surface2 = FONT_TEKO_MEDIUM.render("Great job keeping the museum safe!",False,'Black').convert_alpha()
                results_rect2 = results_surface2.get_rect(center = (WIDTH // 2, HEIGHT // 2))
                screen.blit(results_surface2,results_rect2)

                results_surface1 = FONT_TEKO_MEDIUM.render("You've changed all the keys", False, 'Black').convert_alpha()
                results_rect1 = results_surface1.get_rect(center=(WIDTH // 2, results_rect2.centery - 50))
                screen.blit(results_surface1, results_rect1)

                results_surface3 = FONT_TEKO_BOLD_SMALL.render(f"Final Score: {score} / {int(max_rounds / 2)}", False, 'Black').convert_alpha()
                results_rect3 = results_surface3.get_rect(center=(WIDTH // 2, results_rect2.centery + 50))
                screen.blit(results_surface3, results_rect3)
                
                back_button.update(screen)

        else:
            score_surface = FONT_TEKO_REGULAR.render(f"Score: {score}",False,'Black').convert_alpha()
            score_rect = score_surface.get_rect(center = (50, 50))
            screen.blit(score_surface,score_rect)
            
            prompt_surface = FONT_TEKO_MEDIUM.render("Select a secure key for these two exhibits",False,'Black').convert_alpha()
            prompt_rect = prompt_surface.get_rect(center = (WIDTH // 2, 100))
            screen.blit(prompt_surface,prompt_rect)


            positions = [(200, 800), (450, 800), (700, 800), (950, 800)]

            for i, key in enumerate(current_keys):
                key_rect = key["image"].get_rect(center=positions[i])
                screen.blit(key["image"], key_rect)
                key_positions.append((key_rect, key))

            if show_result:

                if selected_answer == 0:
                    correct_surface = FONT_TEKO_SEMIBOLD_SMALL.render(message,False,'Green').convert_alpha()
                    correct_rect = correct_surface.get_rect(center = (WIDTH // 2, HEIGHT - 100))
                    screen.blit(correct_surface,correct_rect)
                else:
                    correct_surface = FONT_TEKO_SEMIBOLD_SMALL.render(message,False,'Red').convert_alpha()
                    correct_rect = correct_surface.get_rect(center = (WIDTH // 2, HEIGHT - 100))
                    screen.blit(correct_surface,correct_rect)

                next_surface = FONT_TEKO_SEMIBOLD_SMALL.render("Click 'Next' to continue",False,'Black').convert_alpha()
                next_rect = next_surface.get_rect(center = (WIDTH // 2, HEIGHT - 50))
                screen.blit(next_surface,next_rect)

        pygame.display.flip()

        '''Defines what happens with the user interacts with the UI'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the user clicks the x button in the top right, close the game and exit
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if show_next_button and rounds_played < max_rounds:
                    rounds_played += 1
                    show_result = False
                    show_next_button = False
                    select_new_keys()

                if back_button.checkForInput(KEY_CHANGE_MOUSE_POS):
                    from game import game_menu
                    game_menu(screen)

                else:
                    check_key_click(event.pos)

    pygame.quit()
    sys.exit()