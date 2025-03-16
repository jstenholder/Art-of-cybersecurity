
import pygame, random, sys
from settings import WIDTH, HEIGHT, BLUE, BLACK, WHITE, GREEN, RED
from button import Button
from settings import FONT

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Painting Classification Minigame")
#screen.fill(BLACK)

# Load images
painting_images = [
    pygame.image.load("assets/painting1.png"),
    pygame.image.load("assets/painting2.png"),
    pygame.image.load("assets/painting3.png"),
    pygame.image.load("assets/painting4.png"),
    pygame.image.load("assets/painting5.png")
]

# Quiz data
painting_information = [
    {"painting": painting_images[0], "artist": "Eve Dropper", "age": 2, "value": "$","choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0, "explanation": "Explanation TBD"},
    {"painting": painting_images[1], "artist": "Max Secure", "age": 4, "value": "$$","choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 1, "explanation": "Explanation TBD"},
    {"painting": painting_images[2], "artist": "Malcome Ware", "age": 43, "value": "$$$","choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 0, "explanation": "Explanation TBD"},
    {"painting": painting_images[3], "artist": "Pablo Phishcasso", "age": 18, "value": "$$$","choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 3, "explanation": "Explanation TBD"},
    {"painting": painting_images[4], "artist": "Grant Privilege", "age": 7, "value": "$$$$","choices": ["Level 1", "Level 2", "Level 3", "Level 4"], "answer": 2, "explanation": "Explanation TBD"},
    
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
back_button = Button(image=None, pos=(WIDTH - 150, HEIGHT - 75), text_input="BACK", font=FONT, base_color="Green", hovering_color="Red")
back_button.changeColor(PAINTING_CLASSIFICATION_MOUSE_POS)

# Initialize game state
game_state = "instructions"  # Start with the instructions screen

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
            text_surface = FONT.render(line, True, BLACK)
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
    rendered_text = FONT.render(text, True, color)
    screen.blit(rendered_text, (x, y))

def check_answer_click(pos):
    global selected_answer, show_result, show_next_button, rounds_played, score  # Declare as global

    painting_bottom_left_x, painting_bottom_left_y = painting_information[current_question]["painting"].get_rect(center=(300, 300)).bottomleft
    for i in range(len(painting_information[current_question]["choices"])):
        choice_y = (painting_bottom_left_y + 100) + i * 50
        if painting_bottom_left_x <= pos[0] <= painting_bottom_left_x + 300 and choice_y <= pos[1] <= choice_y + 30:
            selected_answer = i
            show_result = True
            show_next_button = True
            rounds_played += 1  # Now correctly modifying the global variable
            print("Rounds played:", rounds_played)
            if selected_answer == painting_information[current_question]["answer"]:
                score += 1  # Increment score if correct
            
show_instructions()

running = True
while running:
    PAINTING_CLASSIFICATION_MOUSE_POS = pygame.mouse.get_pos()
    screen.fill(WHITE)
    if rounds_played >= max_rounds:
        if score < 5:
            results_surface2 = FONT.render("You might need to think about your life choices",False,'Black').convert_alpha()
            results_rect2 = results_surface2.get_rect(center = (WIDTH // 2, HEIGHT // 2))
            screen.blit(results_surface2,results_rect2)

            results_surface1 = FONT.render("You've successfully processed all incoming packages", False, 'Black').convert_alpha()
            results_rect1 = results_surface1.get_rect(center=(WIDTH // 2, results_rect2.centery - 50))
            screen.blit(results_surface1, results_rect1)

            results_surface3 = FONT.render(f"Final Score: {score} / {max_rounds}", False, 'Black').convert_alpha()
            results_rect3 = results_surface3.get_rect(center=(WIDTH // 2, results_rect2.centery + 50))
            screen.blit(results_surface3, results_rect3)

            back_button.update(screen)
        else:
                
            results_surface2 = FONT.render("Great job keeping the museum safe!",False,'Black').convert_alpha()
            results_rect2 = results_surface2.get_rect(center = (WIDTH // 2, HEIGHT // 2))
            screen.blit(results_surface2,results_rect2)

            results_surface1 = FONT.render("You've successfully processed all incoming packages", False, 'Black').convert_alpha()
            results_rect1 = results_surface1.get_rect(center=(WIDTH // 2, results_rect2.centery - 50))
            screen.blit(results_surface1, results_rect1)

            results_surface3 = FONT.render(f"Final Score: {score} / {max_rounds}", False, 'Black').convert_alpha()
            results_rect3 = results_surface3.get_rect(center=(WIDTH // 2, results_rect2.centery + 50))
            screen.blit(results_surface3, results_rect3)

            back_button.update(screen)
    else:

        rounds_surface = FONT.render(f"Round {rounds_played + 1}",False,'Black').convert_alpha()
        rounds_rect = rounds_surface.get_rect(center = (WIDTH // 2, 50))
        screen.blit(rounds_surface,rounds_rect)
           
        question_data = painting_information[current_question]
        painting_rect = question_data["painting"].get_rect(center=(300, 300))
        screen.blit(question_data["painting"], painting_rect)

        painting_bottom_left_x, painting_bottom_left_y = painting_rect.bottomleft

        # Draw question information
        info_rect = pygame.Rect(600, 100, 400, 150)
        pygame.draw.rect(screen, BLUE, info_rect)
        pygame.draw.rect(screen, BLACK, info_rect, 3)

        draw_text(f"Artist: {question_data['artist']}", 620, 120, WHITE)
        draw_text(f"Age: {question_data['age']} years", 620, 160, WHITE)
        draw_text(f"Value: {question_data['value']}", 620, 200, WHITE)

        draw_text("Value determines the initial level", 600, 280, BLACK)
        draw_text("(Ex. Value 4 initially goes into Level 4)", 600, 320, BLACK)
        draw_text("If the artist is Pablo Phishcasso, value increases", 600, 360, BLACK)
        draw_text("by one level for every five years until Level 4", 600, 400, BLACK)
        draw_text("For anyone else, the value decreases by one ", 600, 440, BLACK)
        draw_text("level for every five years until...", 600, 480, BLACK)

        # Draw score
        draw_text(f"Score: {score}", 50, 50, BLACK)  # Display score in top-left corner

        for i, choice in enumerate(question_data["choices"]):
            choice_y = (painting_bottom_left_y + 100) + i * 50
            pygame.draw.rect(screen, GREEN if selected_answer == i else WHITE, pygame.Rect(painting_bottom_left_x, choice_y, 300, 30))
            draw_text(choice, painting_bottom_left_x + 10, choice_y + 5, BLACK)

        if show_result:
            correct_answer = question_data["answer"]
            if selected_answer == correct_answer:
                result_text = "Correct!"
            else:
                result_text = "Incorrect!"
            draw_text(result_text, 620, 550, RED if selected_answer != correct_answer else GREEN)

        if show_next_button:
            next_button = pygame.Rect(1000, 900, 150, 50)
            pygame.draw.rect(screen, GREEN, next_button)
            draw_text("Next", 1010, 910, WHITE) 

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
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