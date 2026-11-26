
import random
from pathlib import Path

from flask import Flask, request, jsonify, send_from_directory

from backend.game import TicTacToe
from backend.ai import TicTacToeAI


# ==========================================
# 1. PROJECT CONFIGURATION
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app = Flask(
    __name__,
    static_folder=str(FRONTEND_DIR),
    static_url_path="/static"
)


# ==========================================
# 2. GAME INITIALIZATION
# ==========================================

game = TicTacToe()
ai = TicTacToeAI()

human_score = 0
ai_score = 0
draw_score = 0

game_over = False
winner = None

difficulty = "hard"


# ==========================================
# 3. AI DIFFICULTY SYSTEM
# ==========================================

def choose_ai_move():

    moves = ai.available_moves(game.board)

    if not moves:
        return None

    # EASY: Random moves
    if difficulty == "easy":
        return random.choice(moves)

    # MEDIUM: Random or strategic moves
    if difficulty == "medium":
        if random.random() < 0.5:
            return random.choice(moves)

    # HARD: Full Minimax + Alpha-Beta Pruning
    return ai.best_move(game.board)


# ==========================================
# 4. GAME STATE
# ==========================================

def get_game_state():

    return {
        "board": game.board,
        "current_player": game.current_player,
        "winner": winner,
        "game_over": game_over,

        "difficulty": difficulty,

        "scores": {
            "human": human_score,
            "ai": ai_score,
            "draws": draw_score
        }
    }


# ==========================================
# 5. GAME RESULT HANDLING
# ==========================================

def finish_game():

    global game_over
    global winner
    global human_score
    global ai_score
    global draw_score

    winner = game.check_winner()

    if winner is not None:

        game_over = True

        if winner == "X":
            human_score += 1

        elif winner == "O":
            ai_score += 1

        elif winner == "Draw":
            draw_score += 1


# ==========================================
# 6. FRONTEND ROUTE
# ==========================================

@app.route("/")
def home():

    return send_from_directory(FRONTEND_DIR, "index.html")


# ==========================================
# 7. GET CURRENT GAME STATE
# ==========================================

@app.route("/api/state", methods=["GET"])
def state():

    return jsonify(get_game_state())


# ==========================================
# 8. HUMAN + AI MOVE
# ==========================================

@app.route("/api/move", methods=["POST"])
def make_move():

    global game_over

    if game_over:
        return jsonify({
            "error": "Game is already over."
        }), 400

    data = request.get_json(silent=True) or {}

    position = data.get("position")

    # Validate position
    if not isinstance(position, int) or isinstance(position, bool):

        return jsonify({
            "error": "Invalid position."
        }), 400

    if position < 0 or position > 8:

        return jsonify({
            "error": "Position must be between 0 and 8."
        }), 400

    if game.current_player != "X":

        return jsonify({
            "error": "It is not the human player's turn."
        }), 400

    # Human move
    if not game.make_move(position, "X"):

        return jsonify({
            "error": "Cell is already occupied."
        }), 400

    finish_game()

    # AI move
    if not game_over:

        game.current_player = "O"

        ai_position = choose_ai_move()

        if ai_position is not None:
            game.make_move(ai_position, "O")

        finish_game()

        if not game_over:
            game.current_player = "X"

    return jsonify(get_game_state())


# ==========================================
# 9. CHANGE AI DIFFICULTY
# ==========================================

@app.route("/api/difficulty", methods=["POST"])
def set_difficulty():

    global difficulty

    data = request.get_json(silent=True) or {}

    selected = data.get("difficulty")

    allowed_difficulties = ["easy", "medium", "hard"]

    if selected not in allowed_difficulties:

        return jsonify({
            "error": "Invalid difficulty. Choose easy, medium, or hard."
        }), 400

    difficulty = selected

    return jsonify({
        "message": "Difficulty updated successfully.",
        "difficulty": difficulty
    })


# ==========================================
# 10. RESET GAME
# ==========================================

@app.route("/api/reset", methods=["POST"])
def reset_game():

    global game_over
    global winner

    game.reset()

    game_over = False
    winner = None

    return jsonify(get_game_state())


# ==========================================
# 11. RUN FLASK APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
