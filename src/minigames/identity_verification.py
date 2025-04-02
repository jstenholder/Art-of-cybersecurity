import pygame, random, sys
from settings import WIDTH, HEIGHT, BLUE, BLACK, WHITE, GREEN, RED
from button import Button
from settings import FONT_TEKO_BOLD, FONT_TEKO_LIGHT, FONT_TEKO_MEDIUM, FONT_TEKO_REGULAR, FONT_TEKO_SEMIBOLD, FONT_TEKO_SEMIBOLD_SMALL, FONT_TEKO_BOLD_SMALL

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Identity Classification Minigame")

background_image = pygame.image.load("assets/identity_verification.png")  # CHANGED

# Load images
character_images = [
    pygame.image.load("assets/robot1_original.png"),
    pygame.image.load("assets/robot1_imposter1.png"),
    pygame.image.load("assets/robot1_imposter2.png"),
    pygame.image.load("assets/robot1_imposter3.png"),
    pygame.image.load("assets/robot1_imposter4.png")
]

character_id_images = [
    pygame.image.load("assets/robot1_id.png")
]

character_information = [
    {"character": character_images[0], "ID": "317694", "Fake ID": "317694", "profession": "Museum curator", "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[0], "ID": "317694", "Fake ID": "317694", "profession": "Delivery droid", "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[0], "ID": "317694", "Fake ID": "317694", "profession": "Anthropologist", "choices": ["Yes", "No"], "answer": 0, "explanation": "Everything seems legitimate. Don't keep them waiting!"},
    {"character": character_images[0], "ID": "317694", "Fake ID": "317694", "profession": "Healthcare droid", "choices": ["Yes", "No"], "answer": 1, "explanation": "Why would a healthcare droid be delivering art?"},
    {"character": character_images[1], "ID": "317695", "Fake ID": "317694", "profession": "Museum owner", "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID. Something seems off..."},
    {"character": character_images[2], "ID": "317659", "Fake ID": "317694", "profession": "Historian", "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID. Something seems off..."},
    {"character": character_images[3], "ID": "317694", "Fake ID": "317694", "profession": "Delivery droid", "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID. Something seems off..."},
    {"character": character_images[4], "ID": "317694", "Fake ID": "317694", "profession": "Historian", "choices": ["Yes", "No"], "answer": 1, "explanation": "Take another look at their ID. Something seems off..."},
]
current_question = random.randint(0, len(character_information) - 1)
selected_answer = -1
show_result = False
show_next_button = False
rounds_played = 0
max_rounds = 7
score = 0  # Initialize score
global IDENTITY_VERIFICATION_MOUSE_POS
IDENTITY_VERIFICATION = pygame.mouse.get_pos()

global back_button
back_button = Button(image=None, pos=(WIDTH - 150, HEIGHT - 75), text_input="BACK", font=FONT_TEKO_SEMIBOLD_SMALL, base_color="Green", hovering_color="Red")
back_button.changeColor(IDENTITY_VERIFICATION)

# Function to draw text
def draw_text(text, x, y, color=BLACK):
    rendered_text = FONT_TEKO_SEMIBOLD_SMALL.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Function to check if a choice is clicked
def check_answer_click(pos):
    global selected_answer, show_result, show_next_button, score, rounds_played

    if show_result:
        return  # Prevent multiple clicks during result display

    character_bottom_left_x, character_bottom_left_y = character_information[current_question]["character"].get_rect(center=(150, 300)).bottomleft
    choice_x = character_bottom_left_x

    for i, choice in enumerate(character_information[current_question]["choices"]):
        choice_y = character_bottom_left_y + 100 + i * 50
        if choice_x <= pos[0] <= choice_x + 200 and choice_y <= pos[1] <= choice_y + 30:
            selected_answer = i
            show_result = True
            show_next_button = True

            if selected_answer == character_information[current_question]["answer"]:
                score += 1
            rounds_played += 1


# Initialize game state
game_state = "instructions"  # Start with the instructions screen

def show_instructions():
    """Display instructions and wait for user input to proceed."""
    instruction_text = [
        "Welcome to Identity Verification Minigame!",
        "Instructions:",
        "- You will be shown a delivery droid",
        "- Based on what they are delivering and if their identity is valid, you can accept or deny them access",
        "- Select 'yes' or 'no to submit your answer.",
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

running = True
while running:
    IDENTITY_VERIFICATION = pygame.mouse.get_pos()

    screen.blit(background_image, (0, 0))  # CHANGED

    if rounds_played >= max_rounds:
        if score < 7:
            results_surface2 = FONT_TEKO_MEDIUM.render("You might need to think about your life choices",False,'Black').convert_alpha()
            results_rect2 = results_surface2.get_rect(center = (WIDTH // 2, HEIGHT // 2))
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
            results_rect2 = results_surface2.get_rect(center = (WIDTH // 2, HEIGHT // 2))
            screen.blit(results_surface2,results_rect2)

            results_surface1 = FONT_TEKO_MEDIUM.render("You've successfully processed all incoming packages", False, 'Black').convert_alpha()
            results_rect1 = results_surface1.get_rect(center=(WIDTH // 2, results_rect2.centery - 50))
            screen.blit(results_surface1, results_rect1)

            results_surface3 = FONT_TEKO_BOLD_SMALL.render(f"Final Score: {score} / {max_rounds}", False, 'Black').convert_alpha()
            results_rect3 = results_surface3.get_rect(center=(WIDTH // 2, results_rect2.centery + 50))
            screen.blit(results_surface3, results_rect3)

            back_button.update(screen)
        
    else:
        rounds_surface = FONT_TEKO_REGULAR.render(f"Round {rounds_played + 1}",False,'Black').convert_alpha()
        rounds_rect = rounds_surface.get_rect(center = (WIDTH // 2, 25))
        screen.blit(rounds_surface,rounds_rect)

        # Draw score
        #draw_text(f"Score: {score}", 50, 50, BLACK)  # Display score in top-left corner
        score_surface = FONT_TEKO_REGULAR.render(f"Score: {score}",False,'Black').convert_alpha()
        score_rect = score_surface.get_rect(center = (50, 25))
        screen.blit(score_surface,score_rect)

        question_data = character_information[current_question]
        character_rect = question_data["character"].get_rect(center=(300, 550))
        screen.blit(question_data["character"], character_rect)

        character_bottom_left_x, character_bottom_left_y = character_rect.bottomleft
        choice_x = character_bottom_left_x

        character_center_x, character_center_y = character_rect.center
        #draw_text(f"{question_data['ID']}", character_center_x - 40, character_center_y + 25, BLACK)

        #draw_text(f"Hello! My ID number is {question_data['Fake ID']}", 400, 150, BLACK)
        #draw_text(f"I'm here to deliver your package", 400, 175, BLACK)

        character_message = [
        f"Hello! My ID number is {question_data['Fake ID']}",
        f"I'm here to deliver your package"]

        # Draw instructions box
        # pygame.draw.rect(screen, BLUE, (WIDTH // 2, HEIGHT // 4, 200, 100))  # White background box

        y = 275 # Used to print each line on a separate row
        for line in character_message:
            text_surface = FONT_TEKO_REGULAR.render(line, True, BLACK)
            text_rect = text_surface.get_rect(midleft=(450, y))
            screen.blit(text_surface, text_rect)
            y += 50

        text_surface = FONT_TEKO_REGULAR.render("Are you going to accept this delivery?", True, BLACK)
        text_rect = text_surface.get_rect(midleft=(character_bottom_left_x, character_bottom_left_y + 50))
        screen.blit(text_surface, text_rect)    
            
        #info_rect = pygame.Rect(400, 300, 375, 160)
        #pygame.draw.rect(screen, BLACK, info_rect)

        #character_id_rect = character_id_images[0].get_rect(topleft=(405, 305))
        #screen.blit(character_id_images[0], character_id_rect)
        #draw_text(f"ID: {question_data['ID']}", 570, 340, WHITE)
        #draw_text(f"Profession:", 570, 370, WHITE)
        #draw_text(f"{question_data['profession']}", 570, 400, WHITE)
            
        for i, choice in enumerate(question_data["choices"]):
            color = BLUE if i == selected_answer else BLACK
            draw_text(f"{i + 1}. {choice}", choice_x, character_bottom_left_y + 100 + i * 50, color)
            
            
        if show_result:
            result_text = "Correct!" if selected_answer == question_data["answer"] else f"Wrong! {question_data['explanation']}"
            result_color = GREEN if selected_answer == question_data["answer"] else RED
            draw_text(result_text, character_bottom_left_x, 900, result_color)
            draw_text("Click 'Next' to continue", character_bottom_left_x, 950, BLACK)
            
    
    pygame.display.flip()
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if show_next_button and rounds_played < max_rounds:
                    current_question = random.randint(0, len(character_information) - 1)
                    selected_answer = -1
                    show_result = False
                    show_next_button = False
                if back_button.checkForInput(IDENTITY_VERIFICATION):
                    from game import game_menu
                    game_menu(screen)
                else:
                    check_answer_click(event.pos)
