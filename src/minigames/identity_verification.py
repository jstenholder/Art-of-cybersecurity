import pygame, random, sys
from settings import WIDTH, HEIGHT, BLUE, BLACK
from button import Button

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)
GREEN = (50, 205, 50)
RED = (220, 20, 60)
FONT = pygame.font.Font(None, 36)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Painting Classification Minigame")

# Load images
character_images = [
    pygame.image.load("assets/robot1_original.png"),
    pygame.image.load("assets/robot1_imposter1.png"),
    pygame.image.load("assets/robot1_imposter2.png"),
    pygame.image.load("assets/robot1_imposter3.png"),
    pygame.image.load("assets/robot1_imposter4.png")
]

character_id_images = [
    pygame.image.load("robot1_id.png")
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

# Function to draw text
def draw_text(text, x, y, color=BLACK):
    rendered_text = FONT.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Function to check if a choice is clicked
def check_answer_click(pos):
    global selected_answer, show_result, show_next_button
    character_bottom_left_x, character_bottom_left_y = character_information[current_question]["character"].get_rect(center=(150, 300)).bottomleft
    choice_x = character_bottom_left_x  # Align choices with the left edge of the character image
    for i in range(len(character_information[current_question]["choices"])):
        choice_y = character_bottom_left_y + 100 + i * 50  # Offset choices below the character
        if choice_x <= pos[0] <= choice_x + 200 and choice_y <= pos[1] <= choice_y + 30:
            selected_answer = i
            show_result = True
            show_next_button = True

running = True
while running:
    screen.fill(WHITE)
    
    question_data = character_information[current_question]
    character_rect = question_data["character"].get_rect(center=(200, 300))
    screen.blit(question_data["character"], character_rect)

    character_bottom_left_x, character_bottom_left_y = character_rect.bottomleft
    choice_x = character_bottom_left_x  # Align text to bottom-left

    character_center_x, character_center_y = character_rect.center
    draw_text(f"{question_data['ID']}", character_center_x - 40, character_center_y + 25, BLACK)

    draw_text(f"Hello! My ID number is {question_data['Fake ID']}", 400, 150, BLACK)
    draw_text(f"I'm here to deliver your package", 400, 175, BLACK)

    
    # Draw drivers license rectangle
    info_rect = pygame.Rect(400, 300, 375, 160)  # Adjust size and position as needed
    pygame.draw.rect(screen, BLACK, info_rect)  # Background color

    character_id_rect = character_id_images[0].get_rect(topleft=(405, 305))
    screen.blit(character_id_images[0], character_id_rect)
    draw_text(f"ID: {question_data['ID']}", 570, 340, WHITE)
    draw_text(f"Profession:", 570, 370, WHITE)
    draw_text(f"{question_data['profession']}", 570, 400, WHITE)

    # Draw the question
    draw_text("Are you going to accept this delivery?", character_bottom_left_x, character_bottom_left_y + 50, BLACK)
    
    for i, choice in enumerate(question_data["choices"]):
        color = BLUE if i == selected_answer else BLACK
        draw_text(f"{i + 1}. {choice}", choice_x, character_bottom_left_y + 100 + i * 50, color)
    
    if show_result:
        if selected_answer == question_data["answer"]:
            result_text = "Correct!"
            result_color = GREEN
        else:
            result_text = f"Wrong! {question_data['explanation']}"
            result_color = RED
        draw_text(result_text, character_bottom_left_x, 900, result_color)
        draw_text("Click 'Next' to continue", character_bottom_left_x, 950, BLACK)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if show_next_button:
                current_question = random.randint(0, len(character_information) - 1)
                selected_answer = -1
                show_result = False
                show_next_button = False
            else:
                check_answer_click(event.pos)

pygame.quit()
sys.exit()