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

'''
Load background images

There are multiple background images used throughout the game to make it seem like the user is going around and changing the keys for different exhibits
'''
background_images = [
    pygame.image.load("assets/diamond_and_asteroid.png"),
    pygame.image.load("assets/asteroid_and_shell_fossil.png"),
    pygame.image.load("assets/shell_fossil_and_sword.png"),
    pygame.image.load("assets/diamond_and_map.png"),
    pygame.image.load("assets/map_and_vase.png"),
    pygame.image.load("assets/vase_and_fish_fossil.png")
]

'''
Load keys

These images serve as the "keys" that the user is presented in-game
'''
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

'''
Loading prompt information

Each key is loaded into a dictionary as well as if its secure or not
This information is used in the game loop to generate game content
'''

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


'''
Declare global variables and buttons

rounds_played - Tracks how many rounds have been played
max_rounds - How many rounds the user is subjected to
score - Tracks score
selected_answer - Stores what the user selects
show_result - Shows the answer (Only after the user makes a choice)
show_next_button - Allows the user to move on to the next round (Only after they make a choice)
message - Shows the explanation (Only after the user makes a choice)
key_positions - Stores the location where the user clicks

KEY_CHANGE_MOUSE_POS - Tracks mouse position
back_button - Defines the details of the back button
next_button - Defines the details of the next button
'''
global rounds_played, max_rounds, score, selected_answer, show_result, show_next_button, message, current_keys, key_positions
rounds_played = 0
max_rounds = 10
score = 0
selected_answer = -1
show_result = False
show_next_button = False
message = ""
key_positions = []

global KEY_CHANGE_MOUSE_POS
KEY_CHANGE_MOUSE_POS = pygame.mouse.get_pos()

global back_button, next_button
back_button = Button(image=None, pos=(WIDTH - 100, HEIGHT - 50), text_input="BACK", font=FONT_TEKO_BOLD_SMALL, base_color=BLACK, hovering_color=BLUE)
back_button.changeColor(KEY_CHANGE_MOUSE_POS)

next_button = Button(image=None, pos=(WIDTH - 100, HEIGHT - 50), text_input="NEXT", font=FONT_TEKO_BOLD_SMALL, base_color=BLACK, hovering_color=BLUE)
next_button.changeColor(KEY_CHANGE_MOUSE_POS)

'''
Displays and instructions page

Explains the rules of the game and how to play
User can close out of it by clicking anywhere or hitting any key
'''
def show_instructions():
    """Display instructions and wait for user input to proceed."""
    instruction_text = [
        "Welcome to Key Change Minigame!",
        "",
        "As part of the security procedures, we need to change some keys on exhibits",
        "The most secure keys have the most notches, making them harder to guess and replicate",
        "With a copy of the keys, a criminal could take control of the exhibit and steal things",
        "So length is very important",
        "Keys also must have all three groove types and cannot have more than two of the same in a row",
        "Doing so would make them less complex, which isn't good",
        "So make sure all keys have at least fourteen notches and their patterns are complex",
        "",
        "Good luck",
        "",
        "Press any key to continue..."
    ]

    while True:
        screen.fill(WHITE)  # Clear the screen

        # Draw instructions box
        pygame.draw.rect(screen, WHITE, (200, 200, 800, 600))  # White background box
        pygame.draw.rect(screen, BLACK, (200, 200, 800, 600), 3)  # Black outline

        # Render instructions text
        y = 300
        for line in instruction_text:
            text_surface = FONT_TEKO_LIGHT.render(line, True, BLACK)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
            screen.blit(text_surface, text_rect)
            y += 35

        pygame.display.flip()

        # Wait for user input to proceed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # Exit function when a key or mouse click is detected
            
'''
Key selection

Selects four key options to be shown to the user
Guarantees that at least one of the four will be secure
'''
def select_new_keys():
    global current_keys
    current_keys = random.sample(key_information, 4)

    if not any(k["answer"] == 0 for k in current_keys):  
        secure_key = random.choice([k for k in key_information if k["answer"] == 0]) # Ensure at least one key is secure
        current_keys[random.randint(0, 3)] = secure_key

'''
Determines if the users selection is correct

First, inputs the users selection and then compares it against the answer
'''
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
                rounds_played += 1 
                
            else:
                message = key["explanation"]
                rounds_played += 1     

'''
Resets the game values to the beginning

Prior to this, if the user selected the game again, they would been shown the final landing page
'''
def reset_key_change():
    global current_question, selected_answer, show_result, show_next_button, score, rounds_played, key_positions
    current_question = random.randint(0, len(key_information) - 1)
    selected_answer = -1
    show_result = False
    show_next_button = False
    score = 0  # Reset score
    rounds_played = 0  # Reset round counter

'''
Main function

Sole purpose of this is to hold the game loop and make it callable by other places in the code
'''              
def key_change(screen):
    
    global current_question, selected_answer, show_result, show_next_button, score, max_rounds, rounds_played, key_positions
    screen.blit(background_images[0], (0, 0))
    reset_key_change() # Resets game to its initial state
    select_new_keys() # Selects new keys   
    show_instructions() # Shows the user the instruction page       

    '''Game loop'''
    running = True
    while running:
        
        KEY_CHANGE_MOUSE_POS = pygame.mouse.get_pos()
        key_positions.clear()
        
        '''Choose background image based on rounds played (changes every 2 rounds)'''
        background_index = (rounds_played // 2) % len(background_images)
        screen.blit(background_images[background_index], (0, 0))

        '''If the rounds played is equal to the max number of rounds, display the final landing page. If not, continue with the game'''
        if rounds_played >= max_rounds:
            '''Displays the final landing pages with the users score'''
            if score < 5: # If the user got a perfect score, show them this message
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

                back_button.update(screen) # Shows the back button

            else: # If the user did not get a perfect score, show them this message  
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
                
                back_button.update(screen) # Shows the back button

        else:

            
            '''Display the user prompt'''
            prompt_surface = FONT_TEKO_MEDIUM.render("Select a secure key for these two exhibits",False,'Black').convert_alpha()
            prompt_rect = prompt_surface.get_rect(center = (WIDTH // 2, 100))
            screen.blit(prompt_surface,prompt_rect)

            '''Display the key options'''
            positions = [(200, 800), (450, 800), (700, 800), (950, 800)]

            for i, key in enumerate(current_keys):
                key_rect = key["image"].get_rect(center=positions[i])
                screen.blit(key["image"], key_rect)
                key_positions.append((key_rect, key))
            
            '''Display the score in the top left corner'''
            score_surface = FONT_TEKO_LIGHT.render(f"Score: {score}", False, BLACK).convert_alpha()
            score_rect = score_surface.get_rect(center = (50, 50))
            screen.blit(score_surface,score_rect)

            if show_result:
                if selected_answer == 0:
                    correct_surface = FONT_TEKO_REGULAR.render(message,False, GREEN).convert_alpha()
                    correct_rect = correct_surface.get_rect(center = (WIDTH // 2, HEIGHT - 100))
                    screen.blit(correct_surface,correct_rect)
                else:
                    correct_surface = FONT_TEKO_REGULAR.render(message,False, RED).convert_alpha()
                    correct_rect = correct_surface.get_rect(center = (WIDTH // 2, HEIGHT - 100))
                    screen.blit(correct_surface,correct_rect)

                next_surface = FONT_TEKO_REGULAR.render("Click 'Next' to continue",False,'Black').convert_alpha()
                next_rect = next_surface.get_rect(center = (WIDTH // 2, HEIGHT - 50))
                screen.blit(next_surface,next_rect)

        pygame.display.flip()

        '''Defines what happens with the user interacts with the UI'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the user clicks the x button in the top right, close the game and exit
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if show_next_button and rounds_played < max_rounds: # If show next button is true (True when the user selects an answer) and all rounds have not been played
                    rounds_played += 1
                    show_result = False
                    show_next_button = False
                    select_new_keys() # Select new question from character_information and do another round
                if back_button.checkForInput(KEY_CHANGE_MOUSE_POS):
                    from game import game_menu
                    game_menu(screen)

                else:
                    check_key_click(event.pos) # Check to see if an answer has been selected
