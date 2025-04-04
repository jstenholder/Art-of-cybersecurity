"""
Author: Jennifer Tenholder
Course: CS/PUBP/ECE-6727 - Cyber Security Practicum
Institution: Georgia Institute of Technology
Date: 2025-04-04

Project Name: The Gameification of Cybersecurity Awareness
"""

"""
This code defines the Painting Classification minigame (referred to as 'Confidential Collection' in-game)
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
pygame.display.set_caption("Confidential Collection")
background_image = pygame.image.load("assets/background_painting_classification.png")

'''
Loading paintings
These images serve as the "paintings" that are displayed to the user in-game
'''
painting_images = [
    pygame.image.load("assets/painting_1.png"),
    pygame.image.load("assets/painting_2.png"),
    pygame.image.load("assets/painting_3.png"),
    pygame.image.load("assets/painting_4.png"),
    pygame.image.load("assets/painting_5.png"),
    pygame.image.load("assets/painting_6.png"),
    pygame.image.load("assets/painting_7.png"),
    pygame.image.load("assets/painting_8.png"),
    pygame.image.load("assets/painting_9.png"),
    pygame.image.load("assets/painting_10.png"),
    pygame.image.load("assets/painting_11.png"),
    pygame.image.load("assets/painting_12.png"),
    pygame.image.load("assets/painting_13.png"),
    pygame.image.load("assets/painting_14.png"),
    pygame.image.load("assets/painting_15.png"),
    pygame.image.load("assets/painting_16.png"),
    pygame.image.load("assets/painting_17.png"),
    pygame.image.load("assets/painting_18.png"),
    pygame.image.load("assets/painting_19.png"),
    pygame.image.load("assets/painting_20.png"),
    pygame.image.load("assets/painting_21.png"),
    pygame.image.load("assets/painting_22.png"),
    pygame.image.load("assets/painting_23.png"),
    pygame.image.load("assets/painting_24.png"),
    pygame.image.load("assets/painting_25.jpg"),
    pygame.image.load("assets/painting_26.png"),
    pygame.image.load("assets/painting_27.png"),
    pygame.image.load("assets/painting_28.png"),
    pygame.image.load("assets/painting_29.png"),
    pygame.image.load("assets/painting_30.png")
]

'''
Loading prompt information

Each image (loaded previously) is loaded into a dictionary as well as a fictious artist name, painting age, and the proper classification level
This information is used in the game loop to generate game content
'''
painting_information = [
    {"painting": painting_images[0], "artist": "Pablo Phishcasso", "age": 1, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1},
    {"painting": painting_images[1], "artist": "Georgia O’Keystroke", "age": 28, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2},
    {"painting": painting_images[2], "artist": "Eve Dropper", "age": 16, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0},
    {"painting": painting_images[3], "artist": "Pablo Phishcasso", "age": 6, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1},
    {"painting": painting_images[4], "artist": "Lex Spoit", "age": 57, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2},
    {"painting": painting_images[5], "artist": "Lex Spoit", "age": 29, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1},
    {"painting": painting_images[6], "artist": "Grant Privilege", "age": 48, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1},
    {"painting": painting_images[7], "artist": "Portia Scan", "age": 40, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1},
    {"painting": painting_images[8], "artist": "Vincent Van Threat", "age": 52, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 3},
    {"painting": painting_images[9], "artist": "Georgia O’Keystroke", "age": 28, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2},
    {"painting": painting_images[10], "artist": "Reese Ponse", "age": 24, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0},
    {"painting": painting_images[11], "artist": "Grant Privilege", "age": 20, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0},
    {"painting": painting_images[12], "artist": "Randy Somware", "age": 2, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0},
    {"painting": painting_images[13], "artist": "Lex Spoit", "age": 44, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1},
    {"painting": painting_images[14], "artist": "Grant Privilege", "age": 62, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2},
    {"painting": painting_images[15], "artist": "Andy Malwarhol", "age": 49, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2},
    {"painting": painting_images[16], "artist": "Randy Somware", "age": 35, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1},
    {"painting": painting_images[17], "artist": "Eve Dropper", "age": 6, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0},
    {"painting": painting_images[18], "artist": "Pablo Phishcasso", "age": 12, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1},
    {"painting": painting_images[19], "artist": "Reese Ponse", "age": 67, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2},
    {"painting": painting_images[20], "artist": "Eve Dropper", "age": 2, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 3},
    {"painting": painting_images[21], "artist": "Alice Phisher ", "age": 73, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2},
    {"painting": painting_images[22], "artist": "Rick Connaissance", "age": 43, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 3},
    {"painting": painting_images[23], "artist": "Lex Spoit", "age": 19, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0},
    {"painting": painting_images[24], "artist": "Randy Somware", "age": 18, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0},
    {"painting": painting_images[25], "artist": "Malcolm Ware ", "age": 29, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1},
    {"painting": painting_images[26], "artist": "Malcolm Ware ", "age": 55, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2},
    {"painting": painting_images[27], "artist": "Malcolm Ware ", "age": 94, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 3},
    {"painting": painting_images[28], "artist": "Grant Privilege", "age": 31, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1},
    {"painting": painting_images[29], "artist": "Lex Spoit", "age": 2, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2} 
]
'''
Defines the clickable areas for user selection

Essentially says "If the user is clicking within this area, they are select option 1" for example
'''
clickable_areas = {
    0: pygame.Rect(92, 160, 170, 340),  # Level 1
    1: pygame.Rect(367, 160, 170, 340),  # Level 2
    2: pygame.Rect(646, 160, 170, 340),  # Level 3
    3: pygame.Rect(923, 160, 170, 340)   # Level 4
}

'''
Declare global variables and buttons

current_question - Selects which answer/painting will be displayed
selected_answer - Stores what the user selects
show_result - Shows the answer (Only after the user makes a choice)
show_next_button - Allows the user to move on to the next round (Only after they make a choice)
score - Tracks score
max_rounds - How many rounds the user is ubjected to
rounds_played - Tracks how many rounds have been played

PAINTING_CLASSIFICATION_MOUSE_POS - Tracks mouse position
back_button - Defines the details of the back button
next_button - Defines the details of the next button
'''
global current_question, selected_answer, show_result, show_next_button, score, max_rounds, rounds_played
current_question = random.randint(0, len(painting_information) - 1)
selected_answer = -1
show_result = False
show_next_button = False
score = 0
max_rounds = 5
rounds_played = 0

global PAINTING_CLASSIFICATION_MOUSE_POS
PAINTING_CLASSIFICATION_MOUSE_POS = pygame.mouse.get_pos()

global back_button, next_button
back_button = Button(image=None, pos=(WIDTH - 100, HEIGHT - 50), text_input="BACK", font=FONT_TEKO_BOLD_SMALL, base_color=BLACK, hovering_color=BLUE)
back_button.changeColor(PAINTING_CLASSIFICATION_MOUSE_POS)

next_button = Button(image=None, pos=(WIDTH - 100, HEIGHT - 50), text_input="NEXT", font=FONT_TEKO_BOLD_SMALL, base_color=BLACK, hovering_color=BLUE)
next_button.changeColor(PAINTING_CLASSIFICATION_MOUSE_POS)

'''
Displays and instructions page

Explains the rules of the game and how to play
User can close out of it by clicking anywhere or hitting any key
'''
def show_instructions():
    instruction_text = [
        "Welcome to Painting Classification Minigame!",
        "",
        "In this game, you will be classifying these incoming paintings into different rooms",
        "Companies often store data in different categories for security purposes",
        "This helps them prevent data breaches by making sure only those who need",
        "to access something can access it", 
        "At the museum, value is determined by age",
        "The more valuable something is, the more security it needs",
        "",
        "Keep yout eye out - Per museum regulations, some paintings need to be stored",
        "in higher levels",
        "",
        "Good luck!",
        "",
        "Press any key to continue..."
    ]

    while True:
        '''Display the instructions on a white box outlined in black'''
        pygame.draw.rect(screen, WHITE, (200, 200, 800, 600))
        pygame.draw.rect(screen, BLACK, (200, 200, 800, 600), 3)

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
    global selected_answer, show_result, show_next_button, rounds_played, score

    for i, rect in clickable_areas.items():
        if rect.collidepoint(pos):  # Check if click is inside the rectangle
            selected_answer = i # Users choice
            show_result = True
            show_next_button = True
            rounds_played += 1  

            if selected_answer == painting_information[current_question]["answer"]: # Check if the clicked answer is correct
                score += 1

'''
Resets the game values to the beginning

Prior to this, if the user selected the game again, they would been shown the final landing page
'''
def reset_painting_classification():
    global current_question, selected_answer, show_result, show_next_button, score, max_rounds, rounds_played
    current_question = random.randint(0, len(painting_information) - 1)
    selected_answer = -1
    show_result = False
    show_next_button = False
    score = 0
    rounds_played = 0

'''
Main function

Sole purpose of this is to hold the game loop and make it callable by other places in the code
'''
def painting_classification(screen):

    global current_question, selected_answer, show_result, show_next_button, score, max_rounds, rounds_played
    screen.blit(background_image, (0, 0))
    reset_painting_classification() # Resets to game to its initial state
    show_instructions() # Shows the user the instruction page

    '''Game loop'''
    running = True
    while running:
        PAINTING_CLASSIFICATION_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(background_image, (0, 0)) # Displays the background image defined previously 

        '''If the rounds played is equal to the max number of rounds, display the final landing page. If not, continue with the game'''
        if rounds_played >= max_rounds: 
            '''Displays the final landing pages with the users score'''
            if score < 5: # If the user got a perfect score, show them this message
                results_surface2 = FONT_TEKO_MEDIUM.render("You might need to think about your life choices",False,'Black').convert_alpha()
                results_rect2 = results_surface2.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 150))
                screen.blit(results_surface2,results_rect2)

                results_surface1 = FONT_TEKO_MEDIUM.render("You've successfully processed all incoming packages", False, 'Black').convert_alpha()
                results_rect1 = results_surface1.get_rect(center=(WIDTH // 2, results_rect2.centery - 50))
                screen.blit(results_surface1, results_rect1)

                results_surface3 = FONT_TEKO_BOLD_SMALL.render(f"Final Score: {score} / {max_rounds}", False, 'Black').convert_alpha()
                results_rect3 = results_surface3.get_rect(center=(WIDTH // 2, results_rect2.centery + 50))
                screen.blit(results_surface3, results_rect3)

                back_button.update(screen) # Shows the back button
            else: # If the user did not get a perfect score, show them this message                   
                results_surface2 = FONT_TEKO_MEDIUM.render("Great job keeping the museum safe!",False,'Black').convert_alpha()
                results_rect2 = results_surface2.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 150))
                screen.blit(results_surface2,results_rect2)

                results_surface1 = FONT_TEKO_MEDIUM.render("You've successfully processed all incoming packages", False, 'Black').convert_alpha()
                results_rect1 = results_surface1.get_rect(center=(WIDTH // 2, results_rect2.centery - 50))
                screen.blit(results_surface1, results_rect1)

                results_surface3 = FONT_TEKO_BOLD_SMALL.render(f"Final Score: {score} / {max_rounds}", False, 'Black').convert_alpha()
                results_rect3 = results_surface3.get_rect(center=(WIDTH // 2, results_rect2.centery + 50))
                screen.blit(results_surface3, results_rect3)

                back_button.update(screen) # Shows the back button
        else:
            '''Display the painting'''
            question_data = painting_information[current_question]
            painting_rect = question_data["painting"].get_rect(center=(250, 750))
            screen.blit(question_data["painting"], painting_rect)

            '''Display the painting metadata on a white rectangle for better visibility'''
            painting_metadata = [
            f"Artist: {question_data['artist']}",
            f"Age: {question_data['age']} years",
            ]

            pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 250 , 875, 300, 100))

            y = 910
            for line in painting_metadata:
                text_surface = FONT_TEKO_LIGHT.render(line, True, BLACK)
                text_rect = text_surface.get_rect(midleft=(WIDTH // 2 - 225, y))
                screen.blit(text_surface, text_rect)
                y += 35 # print each item in painting_metadata on a separate line

            '''Display the user prompt'''
            question_surface = FONT_TEKO_REGULAR.render("Where does this belong?",False, BLACK).convert_alpha()
            question_rect = question_surface.get_rect(center = (WIDTH // 2, 100))
            screen.blit(question_surface,question_rect)

            '''Display decision matrix'''
            decision_matrix = pygame.image.load("assets/decision_matrix.png")
            decision_matrix_rect = decision_matrix.get_rect(center=(1000, 775))
            screen.blit(decision_matrix, decision_matrix_rect)

            '''Display the score in the top left corner'''
            score_surface = FONT_TEKO_LIGHT.render(f"Score: {score}",False, BLACK).convert_alpha()
            score_rect = score_surface.get_rect(center = (60, 25))
            screen.blit(score_surface,score_rect)

            '''Checks if the answer is correct and displays the results'''
            if show_result:
                correct_answer = question_data["answer"]
                if selected_answer == correct_answer:
                    result_text = "Correct!"
                else:
                    result_text = "Incorrect!"

                result_surface = FONT_TEKO_REGULAR.render(result_text, False, RED if selected_answer != correct_answer else GREEN).convert_alpha()
                result_rect = question_surface.get_rect(center = (WIDTH // 2 + 70, 150))
                screen.blit(result_surface,result_rect)

            '''Displays the next button to procceed to the next round'''
            if show_next_button:
                next_button.update(screen)

        pygame.display.flip()

        '''Defines what happens with the user interacts with the UI'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the user clicks the x button in the top right, close the game and exit
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if show_next_button and rounds_played < max_rounds: # If show next button is true (True when the user selects an answer) and all rounds have not been played
                    current_question = random.randint(0, len(painting_information) - 1) # Select new question from painting_information and do another round
                    selected_answer = -1
                    show_result = False
                    show_next_button = False
                elif back_button.checkForInput(PAINTING_CLASSIFICATION_MOUSE_POS): # If the back button is clicked, go back to the game menu
                    from game import game_menu
                    game_menu(screen)
                else:
                    check_answer_click(event.pos) # Check to see if an answer has been selected