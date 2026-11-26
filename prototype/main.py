
import pygame
import sys

from game import TicTacToe
from ai import TicTacToeAI

# =====================================
# INITIALIZATION
# =====================================

pygame.init()

WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CodSoft | Tic-Tac-Toe AI")

clock = pygame.time.Clock()

# =====================================
# COLORS
# =====================================

BG = (18, 24, 38)
BOARD_BG = (29, 39, 58)
WHITE = (240, 245, 255)
CYAN = (65, 210, 235)
PINK = (255, 105, 135)
GREEN = (80, 220, 160)
GRAY = (150, 165, 185)
BUTTON = (45, 65, 95)

# =====================================
# FONTS
# =====================================

title_font = pygame.font.SysFont("arial", 42, bold=True)
symbol_font = pygame.font.SysFont("arial", 90, bold=True)
status_font = pygame.font.SysFont("arial", 25, bold=True)
small_font = pygame.font.SysFont("arial", 19)
button_font = pygame.font.SysFont("arial", 23, bold=True)

# =====================================
# GAME OBJECTS
# =====================================

game = TicTacToe()
ai = TicTacToeAI()

human_score = 0
ai_score = 0
draw_score = 0

game_over = False
winner = None

# Board dimensions
BOARD_X = 60
BOARD_Y = 190
CELL_SIZE = 160
BOARD_SIZE = CELL_SIZE * 3

restart_button = pygame.Rect(180, 640, 240, 45)


# =====================================
# DRAWING FUNCTIONS
# =====================================

def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(x, y))
    screen.blit(surface, rect)


def draw_board():

    pygame.draw.rect(
        screen,
        BOARD_BG,
        (BOARD_X, BOARD_Y, BOARD_SIZE, BOARD_SIZE),
        border_radius=15
    )

    # Draw grid lines
    for i in range(1, 3):

        x = BOARD_X + i * CELL_SIZE
        y = BOARD_Y + i * CELL_SIZE

        pygame.draw.line(
            screen, GRAY,
            (x, BOARD_Y),
            (x, BOARD_Y + BOARD_SIZE), 4
        )

        pygame.draw.line(
            screen, GRAY,
            (BOARD_X, y),
            (BOARD_X + BOARD_SIZE, y), 4
        )

    # Draw X and O
    for index, value in enumerate(game.board):

        if value == " ":
            continue

        row = index // 3
        col = index % 3

        center_x = BOARD_X + col * CELL_SIZE + CELL_SIZE // 2
        center_y = BOARD_Y + row * CELL_SIZE + CELL_SIZE // 2

        color = CYAN if value == "X" else PINK

        draw_text(
            value,
            symbol_font,
            color,
            center_x,
            center_y
        )

    # Highlight winning combination
    if winner in ("X", "O"):

        combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for combo in combinations:

            a, b, c = combo

            if (game.board[a] == game.board[b] ==
                    game.board[c] == winner):

                start_row, start_col = divmod(a, 3)
                end_row, end_col = divmod(c, 3)

                start = (
                    BOARD_X + start_col * CELL_SIZE + CELL_SIZE // 2,
                    BOARD_Y + start_row * CELL_SIZE + CELL_SIZE // 2
                )

                end = (
                    BOARD_X + end_col * CELL_SIZE + CELL_SIZE // 2,
                    BOARD_Y + end_row * CELL_SIZE + CELL_SIZE // 2
                )

                pygame.draw.line(
                    screen, GREEN, start, end, 8
                )
                break


def draw_interface():

    screen.fill(BG)

    # Title
    draw_text(
        "TIC-TAC-TOE AI",
        title_font, WHITE,
        WIDTH // 2, 55
    )

    draw_text(
        "Human (X)  vs  AI (O)",
        small_font, GRAY,
        WIDTH // 2, 105
    )

    # Scoreboard
    draw_text(
        f"YOU: {human_score}",
        status_font, CYAN,
        130, 155
    )

    draw_text(
        f"AI: {ai_score}",
        status_font, PINK,
        470, 155
    )

    draw_text(
        f"DRAWS: {draw_score}",
        small_font, WHITE,
        WIDTH // 2, 155
    )

    draw_board()

    # Game status
    if winner == "X":
        status = "You Won!"
        color = GREEN

    elif winner == "O":
        status = "AI Won!"
        color = PINK

    elif winner == "Draw":
        status = "It's a Draw!"
        color = WHITE

    elif game.current_player == "X":
        status = "Your Turn"
        color = CYAN

    else:
        status = "AI Thinking..."
        color = PINK

    draw_text(
        status,
        status_font,
        color,
        WIDTH // 2,
        595
    )

    # Restart button
    pygame.draw.rect(
        screen,
        BUTTON,
        restart_button,
        border_radius=12
    )

    draw_text(
        "RESTART GAME",
        button_font,
        WHITE,
        restart_button.centerx,
        restart_button.centery
    )

    pygame.display.flip()


# =====================================
# GAME LOGIC
# =====================================

def finish_game():

    global game_over, winner
    global human_score, ai_score, draw_score

    winner = game.check_winner()

    if winner is not None:

        game_over = True

        if winner == "X":
            human_score += 1

        elif winner == "O":
            ai_score += 1

        else:
            draw_score += 1


def reset_game():

    global game_over, winner

    game.reset()

    game_over = False
    winner = None


# =====================================
# MAIN GAME LOOP
# =====================================

running = True

while running:

    clock.tick(60)

    draw_interface()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = event.pos

            # Restart button
            if restart_button.collidepoint(event.pos):
                reset_game()
                continue

            # Human move
            if not game_over and game.current_player == "X":

                if (BOARD_X <= mouse_x < BOARD_X + BOARD_SIZE
                        and BOARD_Y <= mouse_y < BOARD_Y + BOARD_SIZE):

                    col = (mouse_x - BOARD_X) // CELL_SIZE
                    row = (mouse_y - BOARD_Y) // CELL_SIZE

                    position = row * 3 + col

                    if game.make_move(position, "X"):

                        finish_game()

                        if not game_over:
                            game.current_player = "O"

    # AI move
    if not game_over and game.current_player == "O":

        pygame.display.flip()

        move = ai.best_move(game.board)

        if move is not None:
            game.make_move(move, "O")

        finish_game()

        if not game_over:
            game.current_player = "X"

    pygame.display.flip()

pygame.quit()
sys.exit()
