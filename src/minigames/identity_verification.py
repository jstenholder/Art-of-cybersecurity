"""
Author: Jennifer Tenholder
Course: CS/PUBP/ECE-6727 - Cyber Security Practicum
Institution: Georgia Institute of Technology
Date: 2025-04-04

Project Name: The Gameification of Cybersecurity Awareness
"""

"""
This code defines the Identity Verification minigame (referred to as 'Suspicious Shipments' in-game)
More details on actual implementation and logic can be found below
"""

'''Import statement(s)'''
import pygame # Game development library
import random # Used for selecting items/questions
import sys # Used for exiting the game
import os # Used for getting the resource path

from button import Button # Handles UI button interations

from settings import WIDTH, HEIGHT # Screen dimensions
from settings import BLUE, BLACK, WHITE, GREEN, RED # Color constants
from settings import FONT_TEKO_BOLD, FONT_TEKO_LIGHT, FONT_TEKO_MEDIUM, FONT_TEKO_REGULAR, FONT_TEKO_SEMIBOLD, FONT_TEKO_SEMIBOLD_SMALL, FONT_TEKO_BOLD_SMALL # Font constants

'''Get resource path'''
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller's temp dir
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init() # Initializes pygame modules - Required for use

'''Game window definition'''
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Suspicious Shipments")
background_image = pygame.image.load(resource_path("assets/background_identity_verification.png"))

'''
Load characters

These images serve as the "characters" that are displayed to the user in-game
'''
character_images = [
    pygame.image.load(resource_path("assets/blue_imposter_1.png")).convert_alpha(), #0
    pygame.image.load(resource_path("assets/blue_imposter_2.png")).convert_alpha(), #1
    pygame.image.load(resource_path("assets/blue_imposter_3.png")).convert_alpha(), #2
    pygame.image.load(resource_path("assets/blue_imposter_4.png")).convert_alpha(), #3
    pygame.image.load(resource_path("assets/blue_imposter_5.png")).convert_alpha(), #4
    pygame.image.load(resource_path("assets/blue_real.png")).convert_alpha(), #5
    pygame.image.load(resource_path("assets/blue_wrong_id.png")).convert_alpha(), #6

    pygame.image.load(resource_path("assets/green_imposter_1.png")).convert_alpha(), #7
    pygame.image.load(resource_path("assets/green_imposter_2.png")).convert_alpha(), #8
    pygame.image.load(resource_path("assets/green_imposter_3.png")).convert_alpha(), #9
    pygame.image.load(resource_path("assets/green_imposter_4.png")).convert_alpha(), #10
    pygame.image.load(resource_path("assets/green_imposter_5.png")).convert_alpha(), #11
    pygame.image.load(resource_path("assets/green_real.png")).convert_alpha(), #12
    pygame.image.load(resource_path("assets/green_wrong_id.png")).convert_alpha(), #13

    pygame.image.load(resource_path("assets/pink_imposter_1.png")).convert_alpha(), #14
    pygame.image.load(resource_path("assets/pink_imposter_2.png")).convert_alpha(), #15
    pygame.image.load(resource_path("assets/pink_imposter_3.png")).convert_alpha(), #16
    pygame.image.load(resource_path("assets/pink_imposter_4.png")).convert_alpha(), #17
    pygame.image.load(resource_path("assets/pink_imposter_5.png")).convert_alpha(), #18
    pygame.image.load(resource_path("assets/pink_real.png")).convert_alpha(), #19
    pygame.image.load(resource_path("assets/pink_wrong_id.png")).convert_alpha(), #20

    pygame.image.load(resource_path("assets/purple_imposter_1.png")).convert_alpha(), #21
    pygame.image.load(resource_path("assets/purple_imposter_2.png")).convert_alpha(), #22
    pygame.image.load(resource_path("assets/purple_imposter_3.png")).convert_alpha(), #23
    pygame.image.load(resource_path("assets/purple_imposter_4.png")).convert_alpha(), #24
    pygame.image.load(resource_path("assets/purple_imposter_5.png")).convert_alpha(), #25
    pygame.image.load(resource_path("assets/purple_real.png")).convert_alpha(), #26
    pygame.image.load(resource_path("assets/purple_wrong_id.png")).convert_alpha(), #27

    pygame.image.load(resource_path("assets/teal_imposter_1.png")).convert_alpha(), #28
    pygame.image.load(resource_path("assets/teal_imposter_2.png")).convert_alpha(), #29
    pygame.image.load(resource_path("assets/teal_imposter_3.png")).convert_alpha(), #30
    pygame.image.load(resource_path("assets/teal_imposter_4.png")).convert_alpha(), #31
    pygame.image.load(resource_path("assets/teal_imposter_5.png")).convert_alpha(), #32
    pygame.image.load(resource_path("assets/teal_real.png")).convert_alpha(), #33
    pygame.image.load(resource_path("assets/teal_wrong_id.png")).convert_alpha() #34
]

'''
Loading IDs

These images serve as the bases of the IDs used in the game
'''
character_id_images = [
    pygame.image.load(resource_path("assets/blue_id.png")),
    pygame.image.load(resource_path("assets/green_id.png")),
    pygame.image.load(resource_path("assets/pink_id.png")),
    pygame.image.load(resource_path("assets/purple_id.png")),
    pygame.image.load(resource_path("assets/teal_id.png"))
]

'''
Loading profile pictures

These images serve as the "ID photos" on the IDs used in the game
'''
character_profile_pics = [
    pygame.image.load(resource_path("assets/id_photo_blue.png")),
    pygame.image.load(resource_path("assets/id_photo_green.png")),
    pygame.image.load(resource_path("assets/id_photo_pink.png")),
    pygame.image.load(resource_path("assets/id_photo_purple.png")),
    pygame.image.load(resource_path("assets/id_photo_teal.png"))
]

'''
Loading prompt information

Each character image, character ID, and character profile picture is loaded into a dictionary as well as the answer for if this "Delivery person" is legitimate
This information is used in the game loop to generate game content
'''
character_information = [
    # Real blue
    {"character": character_images[5], "fake_ID": "266470", "real_ID": "266470", "ID": character_id_images[0], "picture": character_profile_pics[0], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[5], "fake_ID": "266470", "real_ID": "266470", "ID": character_id_images[0], "picture": character_profile_pics[0], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[5], "fake_ID": "266470", "real_ID": "266470", "ID": character_id_images[0], "picture": character_profile_pics[0], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[5], "fake_ID": "266470", "real_ID": "266470", "ID": character_id_images[0], "picture": character_profile_pics[0], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    # Fake blue
    {"character": character_images[0], "fake_ID": "266470", "real_ID": "266470", "ID": character_id_images[0], "picture": character_profile_pics[0], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[1], "fake_ID": "266470", "real_ID": "266470", "ID": character_id_images[0], "picture": character_profile_pics[0], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[2], "fake_ID": "266470", "real_ID": "266470", "ID": character_id_images[0], "picture": character_profile_pics[0], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[3], "fake_ID": "266470", "real_ID": "266470", "ID": character_id_images[0], "picture": character_profile_pics[0], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[4], "fake_ID": "266470", "real_ID": "266470", "ID": character_id_images[0], "picture": character_profile_pics[0], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[6], "fake_ID": "266470", "real_ID": "266479", "ID": character_id_images[0], "picture": character_profile_pics[0], "choices": ["Yes", "No"], "answer": 1, "explanation": "I don't think they are who they claim to be..."},

    # Real green
    {"character": character_images[12], "fake_ID": "206079", "real_ID": "206079", "ID": character_id_images[1], "picture": character_profile_pics[1], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[12], "fake_ID": "206079", "real_ID": "206079", "ID": character_id_images[1], "picture": character_profile_pics[1], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[12], "fake_ID": "206079", "real_ID": "206079", "ID": character_id_images[1], "picture": character_profile_pics[1], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[12], "fake_ID": "206079", "real_ID": "206079", "ID": character_id_images[1], "picture": character_profile_pics[1], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    # Fake green
    {"character": character_images[7], "fake_ID": "206079", "real_ID": "206079", "ID": character_id_images[1], "picture": character_profile_pics[1], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[8], "fake_ID": "206079", "real_ID": "206079", "ID": character_id_images[1], "picture": character_profile_pics[1], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[9], "fake_ID": "206079", "real_ID": "206079", "ID": character_id_images[1], "picture": character_profile_pics[1], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[10], "fake_ID": "206079", "real_ID": "206079", "ID": character_id_images[1], "picture": character_profile_pics[1], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[11], "fake_ID": "206079", "real_ID": "206079", "ID": character_id_images[1], "picture": character_profile_pics[1], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[13], "fake_ID": "206079", "real_ID": "206070", "ID": character_id_images[1], "picture": character_profile_pics[1], "choices": ["Yes", "No"], "answer": 1, "explanation": "I don't think they are who they claim to be..."},

    # Real pink
    {"character": character_images[19], "fake_ID": "374870", "real_ID": "374870", "ID": character_id_images[2], "picture": character_profile_pics[2], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[19], "fake_ID": "374870", "real_ID": "374870", "ID": character_id_images[2], "picture": character_profile_pics[2], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[19], "fake_ID": "374870", "real_ID": "374870", "ID": character_id_images[2], "picture": character_profile_pics[2], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[19], "fake_ID": "374870", "real_ID": "374870", "ID": character_id_images[2], "picture": character_profile_pics[2], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    # Fake pink
    {"character": character_images[14], "fake_ID": "374870", "real_ID": "374870", "ID": character_id_images[2], "picture": character_profile_pics[2], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[15], "fake_ID": "374870", "real_ID": "374870", "ID": character_id_images[2], "picture": character_profile_pics[2], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[16], "fake_ID": "374870", "real_ID": "374870", "ID": character_id_images[2], "picture": character_profile_pics[2], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[17], "fake_ID": "374870", "real_ID": "374870", "ID": character_id_images[2], "picture": character_profile_pics[2], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[18], "fake_ID": "374870", "real_ID": "374870", "ID": character_id_images[2], "picture": character_profile_pics[2], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[20], "fake_ID": "374870", "real_ID": "374780", "ID": character_id_images[2], "picture": character_profile_pics[2], "choices": ["Yes", "No"], "answer": 1, "explanation": "I don't think they are who they claim to be..."},

    # Real purple
    {"character": character_images[26], "fake_ID": "683893", "real_ID": "683893", "ID": character_id_images[3], "picture": character_profile_pics[3], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[26], "fake_ID": "683893", "real_ID": "683893", "ID": character_id_images[3], "picture": character_profile_pics[3], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[26], "fake_ID": "683893", "real_ID": "683893", "ID": character_id_images[3], "picture": character_profile_pics[3], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[26], "fake_ID": "683893", "real_ID": "683893", "ID": character_id_images[3], "picture": character_profile_pics[3], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    # Fake purple
    {"character": character_images[21], "fake_ID": "683893", "real_ID": "683893", "ID": character_id_images[3], "picture": character_profile_pics[3], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[22], "fake_ID": "683893", "real_ID": "683893", "ID": character_id_images[3], "picture": character_profile_pics[3], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[23], "fake_ID": "683893", "real_ID": "683893", "ID": character_id_images[3], "picture": character_profile_pics[3], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[24], "fake_ID": "683893", "real_ID": "683893", "ID": character_id_images[3], "picture": character_profile_pics[3], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[25], "fake_ID": "683893", "real_ID": "683893", "ID": character_id_images[3], "picture": character_profile_pics[3], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID photo. Something seems off..."},
    {"character": character_images[27], "fake_ID": "683893", "real_ID": "693893", "ID": character_id_images[3], "picture": character_profile_pics[3], "choices": ["Yes", "No"], "answer": 1, "explanation": "I don't think they are who they claim to be..."},

    # Real teal
    {"character": character_images[33], "fake_ID": "090470", "real_ID": "090470", "ID": character_id_images[4], "picture": character_profile_pics[4], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[33], "fake_ID": "090470", "real_ID": "090470", "ID": character_id_images[4], "picture": character_profile_pics[4], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[33], "fake_ID": "090470", "real_ID": "090470", "ID": character_id_images[4], "picture": character_profile_pics[4], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[33], "fake_ID": "090470", "real_ID": "090470", "ID": character_id_images[4], "picture": character_profile_pics[4], "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    # Fake teal
    {"character": character_images[28], "fake_ID": "090470", "real_ID": "090470", "ID": character_id_images[4], "picture": character_profile_pics[4], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID. Something seems off..."},
    {"character": character_images[29], "fake_ID": "090470", "real_ID": "090470", "ID": character_id_images[4], "picture": character_profile_pics[4], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID. Something seems off..."},
    {"character": character_images[30], "fake_ID": "090470", "real_ID": "090470", "ID": character_id_images[4], "picture": character_profile_pics[4], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID. Something seems off..."},
    {"character": character_images[31], "fake_ID": "090470", "real_ID": "090470", "ID": character_id_images[4], "picture": character_profile_pics[4], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID. Something seems off..."},
    {"character": character_images[32], "fake_ID": "090470", "real_ID": "090470", "ID": character_id_images[4], "picture": character_profile_pics[4], "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID. Something seems off..."},
    {"character": character_images[34], "fake_ID": "090470", "real_ID": "090407", "ID": character_id_images[4], "picture": character_profile_pics[4], "choices": ["Yes", "No"], "answer": 1, "explanation": "I don't think they are who they claim to be..."},
]
'''
Defines the clickable areas for user selection

Essentially says "If the user is clicking within this area, they are select option 1" for example
'''
clickable_areas = {
    0: pygame.Rect(583, 285, 33, 22),  # Yes
    1: pygame.Rect(588, 336, 23, 20),  # No
}

'''
Declare global variables and buttons

current_question - Selects which answer/painting will be displayed
selected_answer - Stores what the user selects
show_result - Shows the answer (Only after the user makes a choice)
show_next_button - Allows the user to move on to the next round (Only after they make a choice)
score - Tracks score
max_rounds - How many rounds the user is subjected to
rounds_played - Tracks how many rounds have been played

IDENTITY_VERIFICATION_MOUSE_POS - Tracks mouse position
back_button - Defines the details of the back button
next_button - Defines the details of the next button
'''
global current_question, selected_answer, show_result, show_next_button, score, max_rounds, rounds_played
current_question = random.randint(0, len(character_information) - 1)
selected_answer = -1
show_result = False
show_next_button = False
score = 0
max_rounds = 7
rounds_played = 0

global IDENTITY_VERIFICATION_MOUSE_POS
IDENTITY_VERIFICATION_MOUSE_POS = pygame.mouse.get_pos()

global back_button, next_button
back_button = Button(image=None, pos=(WIDTH - 100, HEIGHT - 50), text_input="BACK", font=FONT_TEKO_BOLD_SMALL, base_color=BLACK, hovering_color=BLUE)
back_button.changeColor(IDENTITY_VERIFICATION_MOUSE_POS)

next_button = Button(image=None, pos=(WIDTH - 100, HEIGHT - 50), text_input="NEXT", font=FONT_TEKO_BOLD_SMALL, base_color=BLACK, hovering_color=BLUE)
next_button.changeColor(IDENTITY_VERIFICATION_MOUSE_POS)

'''
Displays and instructions page

Explains the rules of the game and how to play
User can close out of it by clicking anywhere or hitting any key
'''
def show_instructions():
    instruction_text = [
        "Welcome to Identity Verification Minigame!",
        "",
        "In this game you, will be helping security process incoming packages",
        "In order to protect the museum, you need verify the droids make deliveries",
        "Because of the value of our pieces, criminals will try to break in and steal/damange them",
        "They've been known to send suspicious package containing strange items, or even pretend to",
        "be someone they are not",
        "You need to decide whether to accept each droids delivery or not by making sure they ",
        "are who they say they are",
        "If you're even a little suspicious, it's better to be safe than sorry",
        "",
        "Good luck!",
        "",
        "Press any key to continue..."
    ]

    while True:
        '''Display the instructions on a white box outlined in black'''
        pygame.draw.rect(screen, WHITE, (200, 200, 800, 600))  # White background box
        pygame.draw.rect(screen, BLACK, (200, 200, 800, 600), 3)  # Black outline

        y = 250
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
Determines if the users selection is correct

First, inputs the users selection and then compares it against the answer
'''
def check_answer_click(pos):
    global current_question, selected_answer, show_result, show_next_button, score, max_rounds, rounds_played

    for i, rect in clickable_areas.items():
        if rect.collidepoint(pos):  # Check if click is inside the rectangle
            selected_answer = i # Users choice
            show_result = True
            show_next_button = True
            rounds_played += 1  

            if selected_answer == character_information[current_question]["answer"]: # Check if the clicked answer is correct
                score += 1

'''
Resets the game values to the beginning

Prior to this, if the user selected the game again, they would been shown the final landing page
'''
def reset_identity_verification():
    global current_question, selected_answer, show_result, show_next_button, score, max_rounds, rounds_played
    current_question = random.randint(0, len(character_information) - 1)
    selected_answer = -1
    show_result = False
    show_next_button = False
    score = 0  # Reset score
    rounds_played = 0  # Reset round counter

'''
Main function

Sole purpose of this is to hold the game loop and make it callable by other places in the code
'''            
def identity_verification(screen):

    global current_question, selected_answer, show_result, show_next_button, score, max_rounds, rounds_played
    screen.blit(background_image, (0, 0))
    reset_identity_verification() # Resets game to its initial state
    show_instructions() # Shows the user the instruction page

    '''Game loop'''
    running = True
    while running:

        IDENTITY_VERIFICATION_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(background_image, (0, 0))  # Displays the background image defined previously 

        '''If the rounds played is equal to the max number of rounds, display the final landing page. If not, continue with the game'''
        if rounds_played >= max_rounds:
            '''Displays the final landing pages with the users score'''
            if score < 7: # If the user got a perfect score, show them this message
                pygame.draw.rect(screen, WHITE, (300, 400, 600, 200))
                results_surface2 = FONT_TEKO_MEDIUM.render("You might need to think about your life choices",False,'Black').convert_alpha()
                results_rect2 = results_surface2.get_rect(center = (WIDTH // 2, HEIGHT // 2))
                screen.blit(results_surface2,results_rect2)

                results_surface1 = FONT_TEKO_MEDIUM.render("You've processed all incoming packages", False, 'Black').convert_alpha()
                results_rect1 = results_surface1.get_rect(center=(WIDTH // 2, results_rect2.centery - 50))
                screen.blit(results_surface1, results_rect1)

                results_surface3 = FONT_TEKO_BOLD_SMALL.render(f"Final Score: {score} / {max_rounds}", False, 'Black').convert_alpha()
                results_rect3 = results_surface3.get_rect(center=(WIDTH // 2, results_rect2.centery + 50))
                screen.blit(results_surface3, results_rect3)

                back_button.update(screen) # Shows the back button

            else: # If the user did not get a perfect score, show them this message  
                pygame.draw.rect(screen, WHITE, (300, 400, 600, 200))
                results_surface2 = FONT_TEKO_MEDIUM.render("Great job keeping the museum safe!",False,'Black').convert_alpha()
                results_rect2 = results_surface2.get_rect(center = (WIDTH // 2, HEIGHT // 2))
                screen.blit(results_surface2,results_rect2)

                results_surface1 = FONT_TEKO_MEDIUM.render("You've processed all incoming packages", False, 'Black').convert_alpha()
                results_rect1 = results_surface1.get_rect(center=(WIDTH // 2, results_rect2.centery - 50))
                screen.blit(results_surface1, results_rect1)

                results_surface3 = FONT_TEKO_BOLD_SMALL.render(f"Final Score: {score} / {max_rounds}", False, 'Black').convert_alpha()
                results_rect3 = results_surface3.get_rect(center=(WIDTH // 2, results_rect2.centery + 50))
                screen.blit(results_surface3, results_rect3)

                back_button.update(screen) # Shows the back button
            
        else:
            '''Display the character'''
            question_data = character_information[current_question]
            character_rect = question_data["character"].get_rect(center=(350, 750))
            screen.blit(question_data["character"], character_rect)

            '''Display the character message on a white rectangle for better visibility'''
            character_message = [
            f"Hello! I am {question_data['fake_ID']} and I'm here to deliver your package",
            f"Here is my identification"]

            pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 10, 585, 500, 65))
            y = 600
            for line in character_message:
                text_surface = FONT_TEKO_LIGHT.render(line, True, BLACK)
                text_rect = text_surface.get_rect(midleft=(WIDTH // 2, y))
                screen.blit(text_surface, text_rect)
                y += 25 # print each item in the character messageon a separate line
            
            ''' Display the users identification'''
            question_data = character_information[current_question]
            character_id_rect = question_data["ID"].get_rect(center=(800, 800))
            screen.blit(question_data["ID"], character_id_rect)
            question_data2 = character_information[current_question]
            character_pic_rect = question_data2["picture"].get_rect(center=(690, 825))
            screen.blit(question_data2["picture"], character_pic_rect)

            '''Display the user prompt'''
            text_surface = FONT_TEKO_MEDIUM.render("Are you going to accept this delivery?", True, BLACK)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 250))
            screen.blit(text_surface, text_rect)    
                
            '''Display the users options'''    
            for i, choice in enumerate(question_data["choices"]):
                option_surface = FONT_TEKO_REGULAR.render(f"{choice}", True, BLACK)
                option_rect = option_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200 + i * 50))
                screen.blit(option_surface, option_rect)    
            
            '''Display the score in the top left corner'''
            score_surface = FONT_TEKO_LIGHT.render(f"Score: {score}",False,'Black').convert_alpha()
            score_rect = score_surface.get_rect(center = (55, 35))
            screen.blit(score_surface,score_rect)
                
            '''Checks if the answer is correct and displays the results'''    
            if show_result:
                result_text = "Correct!" if selected_answer == question_data["answer"] else f"Wrong! {question_data['explanation']}"
                result_color = GREEN if selected_answer == question_data["answer"] else RED

                result_surface = FONT_TEKO_LIGHT.render(result_text, True, result_color)
                result_rect = result_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
                screen.blit(result_surface, result_rect)   

                '''Displays the next button to procceed to the next round'''
                text_surface = FONT_TEKO_LIGHT.render("Click to continue", True, BLACK)
                text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 75))
                screen.blit(text_surface, text_rect)  
                
        pygame.display.flip()
        
        '''Defines what happens with the user interacts with the UI'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT: # If the user clicks the x button in the top right, close the game and exit
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if show_next_button and rounds_played < max_rounds: # If show next button is true (True when the user selects an answer) and all rounds have not been played
                        current_question = random.randint(0, len(character_information) - 1) # Select new question from character_information and do another round
                        selected_answer = -1
                        show_result = False
                        show_next_button = False
                    if back_button.checkForInput(IDENTITY_VERIFICATION_MOUSE_POS): # If the back button is clicked, go back to the game menu
                        from game import game_menu
                        game_menu(screen)
                    else:
                        check_answer_click(event.pos) # Check to see if an answer has been selected
