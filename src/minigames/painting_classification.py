
import pygame, random, sys
from settings import WIDTH, HEIGHT, BLUE, BLACK, WHITE, GREEN, RED
from button import Button
from settings import FONT_TEKO_BOLD, FONT_TEKO_LIGHT, FONT_TEKO_MEDIUM, FONT_TEKO_REGULAR, FONT_TEKO_SEMIBOLD, FONT_TEKO_BOLD_SMALL, FONT_TEKO_SEMIBOLD_SMALL

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Painting Classification Minigame")
#screen.fill(BLACK)

background_image = pygame.image.load("assets/painting_classification_background_new.png")  # CHANGED

# Load images
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

# Quiz data
painting_information = [
    {"painting": painting_images[0], "artist": "Pablo Phishcasso", "age": 1, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1, "explanation": "Explanation TBD"},
    {"painting": painting_images[1], "artist": "Georgia O’Keystroke", "age": 28, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2, "explanation": "Explanation TBD"},
    {"painting": painting_images[2], "artist": "Eve Dropper", "age": 16, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0, "explanation": "Explanation TBD"},
    {"painting": painting_images[3], "artist": "Pablo Phishcasso", "age": 6, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1, "explanation": "Explanation TBD"},
    {"painting": painting_images[4], "artist": "Lex Spoit", "age": 57, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2, "explanation": "Explanation TBD"},
    {"painting": painting_images[5], "artist": "Lex Spoit", "age": 29, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1, "explanation": "Explanation TBD"},
    {"painting": painting_images[6], "artist": "Grant Privilege", "age": 48, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1, "explanation": "Explanation TBD"},
    {"painting": painting_images[7], "artist": "Portia Scan", "age": 40, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1, "explanation": "Explanation TBD"},
    {"painting": painting_images[8], "artist": "Vincent Van Threat", "age": 52, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 3, "explanation": "Explanation TBD"},
    {"painting": painting_images[9], "artist": "Georgia O’Keystroke", "age": 28, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2, "explanation": "Explanation TBD"},
    {"painting": painting_images[10], "artist": "Reese Ponse", "age": 24, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0, "explanation": "Explanation TBD"},
    {"painting": painting_images[11], "artist": "Grant Privilege", "age": 20, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0, "explanation": "Explanation TBD"},
    {"painting": painting_images[12], "artist": "Randy Somware", "age": 2, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0, "explanation": "Explanation TBD"},
    {"painting": painting_images[13], "artist": "Lex Spoit", "age": 44, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1, "explanation": "Explanation TBD"},
    {"painting": painting_images[14], "artist": "Grant Privilege", "age": 62, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2, "explanation": "Explanation TBD"},
    {"painting": painting_images[15], "artist": "Andy Malwarhol", "age": 49, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2, "explanation": "Explanation TBD"},
    {"painting": painting_images[16], "artist": "Randy Somware", "age": 35, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1, "explanation": "Explanation TBD"},
    {"painting": painting_images[17], "artist": "Eve Dropper", "age": 6, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0, "explanation": "Explanation TBD"},
    {"painting": painting_images[18], "artist": "Pablo Phishcasso", "age": 12, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1, "explanation": "Explanation TBD"},
    {"painting": painting_images[19], "artist": "Reese Ponse", "age": 67, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2, "explanation": "Explanation TBD"},
    {"painting": painting_images[20], "artist": "Eve Dropper", "age": 2, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 3, "explanation": "Explanation TBD"},
    {"painting": painting_images[21], "artist": "Alice Phisher ", "age": 73, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2, "explanation": "Explanation TBD"},
    {"painting": painting_images[22], "artist": "Rick Connaissance", "age": 43, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 3, "explanation": "Explanation TBD"},
    {"painting": painting_images[23], "artist": "Lex Spoit", "age": 19, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0, "explanation": "Explanation TBD"},
    {"painting": painting_images[24], "artist": "Randy Somware", "age": 18, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0, "explanation": "Explanation TBD"},
    {"painting": painting_images[25], "artist": "Malcolm Ware ", "age": 29, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1, "explanation": "Explanation TBD"},
    {"painting": painting_images[26], "artist": "Malcolm Ware ", "age": 55, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2, "explanation": "Explanation TBD"},
    {"painting": painting_images[27], "artist": "Malcolm Ware ", "age": 94, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 3, "explanation": "Explanation TBD"},
    {"painting": painting_images[28], "artist": "Grant Privilege", "age": 31, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1, "explanation": "Explanation TBD"},
    {"painting": painting_images[29], "artist": "Lex Spoit", "age": 2, "choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 20, "explanation": "Explanation TBD"},
    
]
current_question = random.randint(0, len(painting_information) - 1)
selected_answer = -1
show_result = False
show_next_button = False
score = 0  # Initialize score
max_rounds = 5
rounds_played = 0
global PAINTING_CLASSIFICATION_MOUSE_POS
PAINTING_CLASSIFICATION_MOUSE_POS = pygame.mouse.get_pos()

global back_button
back_button = Button(image=None, pos=(WIDTH - 150, HEIGHT - 75), text_input="BACK", font=FONT_TEKO_BOLD_SMALL, base_color="Black", hovering_color="Red")
back_button.changeColor(PAINTING_CLASSIFICATION_MOUSE_POS)

global next_button
next_button = Button(image=None, pos=(WIDTH - 150, HEIGHT - 75), text_input="NEXT", font=FONT_TEKO_BOLD_SMALL, base_color="Black", hovering_color="Red")
next_button.changeColor(PAINTING_CLASSIFICATION_MOUSE_POS)

# Initialize game state
game_state = "instructions"  # Start with the instructions screen

clickable_areas = {
    0: pygame.Rect(92, 160, 170, 340),  # Level 1
    1: pygame.Rect(367, 160, 170, 340),  # Level 2
    2: pygame.Rect(646, 160, 170, 340),  # Level 3
    3: pygame.Rect(923, 160, 170, 340)   # Level 4
}

def show_instructions():
    """Display instructions and wait for user input to proceed."""
    instruction_text = [
        "Welcome to Painting Classification Minigame!",
        "Instructions:",
        "- You will be shown a painting and details about it.",
        "- Select the correct level based on the painting's value.",
        "- Click on the level to submit your answer.",
        "- You have 5 rounds to play. Good luck!",
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

# Show instructions before starting the game loop
show_instructions()

def draw_text(text, x, y, color=BLACK):
    rendered_text = FONT_TEKO_SEMIBOLD_SMALL.render(text, True, color)
    screen.blit(rendered_text, (x, y))

def check_answer_click(pos):
    global selected_answer, show_result, show_next_button, rounds_played, score  # Declare as global

    for i, rect in clickable_areas.items():
        if rect.collidepoint(pos):  # Check if click is inside the rectangle
            selected_answer = i
            show_result = True
            show_next_button = True
            rounds_played += 1  
            print(f"Click detected in choice {i}")

            # Check if the clicked answer is correct
            if selected_answer == painting_information[current_question]["answer"]:
                score += 1
            
show_instructions()

running = True
while running:
    PAINTING_CLASSIFICATION_MOUSE_POS = pygame.mouse.get_pos()

    screen.blit(background_image, (0, 0))  # CHANGED

    if rounds_played >= max_rounds:
        if score < 5:
            results_surface2 = FONT_TEKO_MEDIUM.render("You might need to think about your life choices",False,'Black').convert_alpha()
            results_rect2 = results_surface2.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 150))
            screen.blit(results_surface2,results_rect2)

            results_surface1 = FONT_TEKO_MEDIUM.render("You've successfully processed all incoming packages", False, 'Black').convert_alpha()
            results_rect1 = results_surface1.get_rect(center=(WIDTH // 2, results_rect2.centery - 50))
            screen.blit(results_surface1, results_rect1)

            results_surface3 = FONT_TEKO_BOLD_SMALL.render(f"Final Score: {score} / {max_rounds}", False, 'Black').convert_alpha()
            results_rect3 = results_surface3.get_rect(center=(WIDTH // 2, results_rect2.centery + 50))
            screen.blit(results_surface3, results_rect3)

            back_button.update(screen)
        else:
                
            results_surface2 = FONT_TEKO_MEDIUM.render("Great job keeping the museum safe!",False,'Black').convert_alpha()
            results_rect2 = results_surface2.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 150))
            screen.blit(results_surface2,results_rect2)

            results_surface1 = FONT_TEKO_MEDIUM.render("You've successfully processed all incoming packages", False, 'Black').convert_alpha()
            results_rect1 = results_surface1.get_rect(center=(WIDTH // 2, results_rect2.centery - 50))
            screen.blit(results_surface1, results_rect1)

            results_surface3 = FONT_TEKO_BOLD_SMALL.render(f"Final Score: {score} / {max_rounds}", False, 'Black').convert_alpha()
            results_rect3 = results_surface3.get_rect(center=(WIDTH // 2, results_rect2.centery + 50))
            screen.blit(results_surface3, results_rect3)

            back_button.update(screen)
    else:
           
        question_data = painting_information[current_question]
        painting_rect = question_data["painting"].get_rect(center=(250, 750))
        screen.blit(question_data["painting"], painting_rect)

        painting_bottom_left_x, painting_bottom_left_y = painting_rect.bottomleft

        # Draw question information
        #info_rect = pygame.Rect(600, 100, 400, 150)
        #pygame.draw.rect(screen, BLUE, info_rect)
        #pygame.draw.rect(screen, BLACK, info_rect, 3)

        #draw_text(f"Artist: {question_data['artist']}", 620, 120, WHITE)
        #draw_text(f"Age: {question_data['age']} years", 620, 160, WHITE)
        #draw_text(f"Value: {question_data['value']}", 620, 200, WHITE)

        painting_metadata = [
        f"Artist: {question_data['artist']}",
        f"Age: {question_data['age']} years",
        #f"Value: {question_data['value']}"
        ]

        # Draw instructions box
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 100 , 675, 400, 150))  # White background box

        y = 725 # Used to print each line on a separate row
        for line in painting_metadata:
            text_surface = FONT_TEKO_LIGHT.render(line, True, BLACK)
            text_rect = text_surface.get_rect(midleft=(WIDTH // 2 - 50, y))
            screen.blit(text_surface, text_rect)
            y += 50

        #rounds_surface = FONT_TEKO_REGULAR.render(f"Round {rounds_played + 1}",False,'Black').convert_alpha()
        #rounds_rect = rounds_surface.get_rect(center = (WIDTH // 2, 25))
        #screen.blit(rounds_surface,rounds_rect)

        # Draw score
        #draw_text(f"Score: {score}", 50, 50, BLACK)  # Display score in top-left corner
        score_surface = FONT_TEKO_REGULAR.render(f"Score: {score}",False,'Black').convert_alpha()
        score_rect = score_surface.get_rect(center = (50, 25))
        screen.blit(score_surface,score_rect)

        question_surface = FONT_TEKO_REGULAR.render("Where does this belong?",False,'Black').convert_alpha()
        question_rect = question_surface.get_rect(center = (WIDTH // 2 + 25 , 600))
        screen.blit(question_surface,question_rect)

        #for i, choice in enumerate(question_data["choices"]):
            #choice_y = (painting_bottom_left_y + 100) + i * 50
            #pygame.draw.rect(screen, GREEN if selected_answer == i else WHITE, pygame.Rect(painting_bottom_left_x, choice_y, 300, 30))
            #draw_text(choice, painting_bottom_left_x + 10, choice_y + 5, BLACK)

        if show_result:
            correct_answer = question_data["answer"]
            if selected_answer == correct_answer:
                result_text = "Correct!"
            else:
                result_text = "Incorrect!"
            draw_text(result_text, WIDTH // 2 - 100, 850, RED if selected_answer != correct_answer else GREEN)

        if show_next_button:
            next_button.update(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(f"Clicked at: ({x}, {y})")
            if show_next_button and rounds_played < max_rounds:
                current_question = random.randint(0, len(painting_information) - 1)
                selected_answer = -1
                show_result = False
                show_next_button = False
            elif back_button.checkForInput(PAINTING_CLASSIFICATION_MOUSE_POS):
                from game import game_menu
                game_menu(screen)
            else:
                check_answer_click(event.pos)