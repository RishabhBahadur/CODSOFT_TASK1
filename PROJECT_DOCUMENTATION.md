# Project Documentation: Tic-Tac-Toe AI

## 1. Introduction

Tic-Tac-Toe AI is a browser-based implementation of the classic
Tic-Tac-Toe game. A human player competes against an AI opponent on a 3
× 3 board. The AI uses the Minimax algorithm, enhanced with Alpha-Beta
Pruning, to evaluate possible moves and make decisions.

The project combines a Python game engine and AI module with a Flask web
application and a browser-based frontend.

## 2. Objectives

The main objectives are:

1.  Implement the rules of Tic-Tac-Toe in Python.
2.  Build an AI opponent using Minimax.
3.  optimize the search using Alpha-Beta Pruning.
4.  Provide multiple AI difficulty settings.
5.  Connect the Python backend to a web interface using Flask API
    routes.
6.  Build an interactive interface using HTML, CSS, and JavaScript.

## 3. Scope

The application supports one human player against one AI opponent. The
human plays as `X` and the AI plays as `O`. It supports three difficulty
settings, round reset, win/draw detection, and a scoreboard during the
running application session.

The project is intended as an educational internship task and local
demonstration.

## 4. Tools and Technologies

-   **Python:** Implements the game rules, AI logic, and server-side
    application.
-   **Flask:** Serves the frontend and provides API endpoints.
-   **HTML:** Defines the page structure and game board.
-   **CSS:** Controls visual presentation, layout, and responsive
    behavior.
-   **JavaScript:** Handles board clicks, sends API requests, and
    updates the page.
-   **Minimax:** Evaluates possible game outcomes to select a move.
-   **Alpha-Beta Pruning:** Reduces the number of branches explored by
    Minimax without changing its decision.

## 5. System Architecture

The application has three main layers:

### 5.1 Frontend

The `frontend` directory contains:

-   `index.html` --- page structure, board cells, scoreboard, status
    text, reset control, and difficulty selector.
-   `style.css` --- visual styling and layout.
-   `script.js` --- handles user actions, communicates with the Flask
    API, and renders the game state.

### 5.2 Backend

The `backend` directory contains:

-   `game.py` --- board representation, available-move detection, move
    validation, winner detection, and reset logic.
-   `ai.py` --- AI move selection using Minimax and Alpha-Beta Pruning.
-   `app.py` --- Flask server, API routes, difficulty selection, score
    tracking, and coordination between the game and AI.

### 5.3 Prototype and tests

-   `prototype/main.py` --- earlier playable prototype.
-   `test_game.py` --- game-logic tests.
-   `test_ai.py` --- AI behavior tests.

## 6. Game Logic

The board contains nine positions, represented internally as a list of
nine cells. An empty cell is represented by a single space (`" "`). The
human player uses `X`; the AI uses `O`.

The game logic supports:

-   Listing all available positions.
-   Validating and applying a move.
-   Checking the eight possible winning combinations: three rows, three
    columns, and two diagonals.
-   Detecting a draw when no empty positions remain and no player has
    won.
-   Resetting the board and setting the current player back to `X`.

A move is accepted only when its position is currently available.

## 7. Artificial Intelligence

### 7.1 Minimax

Minimax is a recursive decision-making algorithm used in two-player,
turn-based games. It explores possible future moves and assigns outcomes
according to whether they favor the AI or the human player.

The AI acts as the maximizing player and the human is treated as the
minimizing player. The algorithm selects a move with the best outcome
assuming the opponent also chooses strong moves.

### 7.2 Alpha-Beta Pruning

Alpha-Beta Pruning is an optimization of Minimax. It tracks two values:

-   **Alpha:** the best value found so far for the maximizing player.
-   **Beta:** the best value found so far for the minimizing player.

When a branch cannot improve the decision already available, the
algorithm stops exploring that branch. This reduces unnecessary search
while preserving the Minimax result.

### 7.3 Difficulty settings

The current Flask application implements the following behavior:

  -----------------------------------------------------------------------
  Difficulty                          Behavior
  ----------------------------------- -----------------------------------
  Easy                                Selects a random available move.

  Medium                              Selects a random move with 50%
                                      probability; otherwise uses the
                                      Minimax AI.

  Hard                                Uses the Minimax AI to select the
                                      move.
  -----------------------------------------------------------------------

## 8. Application Workflow

1.  The user opens the application in a browser.
2.  Flask serves the HTML page and static frontend files.
3.  The frontend requests the current state from `/api/state`.
4.  The user clicks an empty board cell.
5.  JavaScript sends the selected position to `/api/move`.
6.  Flask validates and applies the human move.
7.  The backend checks whether the game has ended.
8.  If the game continues, the AI selects and plays a move.
9.  The backend checks the result again and returns the updated game
    state.
10. JavaScript updates the board, status message, and scoreboard.

Changing the difficulty sends a request to `/api/difficulty`; the
frontend then requests a round reset so the next round uses the selected
setting.

## 9. API Endpoints

  -----------------------------------------------------------------------
  Endpoint                HTTP method             Description
  ----------------------- ----------------------- -----------------------
  `/`                     GET                     Returns the main game
                                                  page.

  `/api/state`            GET                     Returns the current
                                                  board and game
                                                  information.

  `/api/move`             POST                    Accepts a human move,
                                                  then makes an AI move
                                                  if the game continues.

  `/api/difficulty`       POST                    Validates and updates
                                                  the selected
                                                  difficulty.

  `/api/reset`            POST                    Resets the board and
                                                  round result.
  -----------------------------------------------------------------------

The move request uses JSON with a `position` value from `0` to `8`. The
precise response schema is defined by the implementation in
`backend/app.py`.

## 10. Installation and Execution

Run these commands in Windows PowerShell from the project directory.

### Step 1: Create a virtual environment

``` powershell
python -m venv venv
```

### Step 2: Activate it

``` powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Flask

``` powershell
python -m pip install Flask
```

### Step 4: Run the application

``` powershell
python -m backend.app
```

### Step 5: Open the browser

``` text
http://127.0.0.1:5000
```

To stop the server, return to PowerShell and press `Ctrl + C`.

## 11. Testing and Validation

The following checks should be performed before submission:

1.  Confirm that the home page loads.
2.  Confirm that each empty cell can be clicked.
3.  Confirm that the AI responds after a valid human move.
4.  Confirm that occupied cells cannot be played again.
5.  Test all three difficulty settings.
6.  Test horizontal, vertical, and diagonal win conditions.
7.  Test a draw.
8.  Confirm that the scoreboard changes after a completed round.
9.  Confirm that Reset starts a fresh round.
10. Check the browser developer console and Flask terminal for errors.

The project includes `test_game.py` and `test_ai.py`; run the tests
using:

``` powershell
python -m pytest
```

If pytest is not installed:

``` powershell
python -m pip install pytest
```

Only report tests as passed after actually running them.

## 12. Results

The application has been run locally using Flask, and the browser
interface has been connected to the Python backend. Human moves, AI
responses, and difficulty selection are implemented. The frontend issue
caused by treating the backend's empty-cell value (`" "`) as truthy in
JavaScript was corrected by checking the space value explicitly.

Add screenshots of the running application to the `screenshots`
directory before final submission.

## 13. Limitations

-   Scores are maintained in application memory and are not persisted
    after the Flask process stops.
-   The current application is designed for local, single-session
    demonstration.
-   No database or user-account system is included.
-   The project has not been described as deployed online; deployment
    would be a separate step.

## 14. Future Enhancements

Possible future improvements include:

-   Persist scores and match history.
-   Add sound effects and more interface animations.
-   Add an AI-thinking indicator.
-   Add automated API and end-to-end tests.
-   Improve accessibility and mobile layout.
-   Deploy the application for public access.

## 15. Conclusion

This project demonstrates how a classic game can be combined with
search-based artificial intelligence and web development. It provides
practical experience with Python programming, game-state management,
Minimax, Alpha-Beta Pruning, Flask APIs, and frontend-backend
integration.

## 16. Internship Details

-   **Program:** CodSoft Artificial Intelligence Internship
-   **Project:** Tic-Tac-Toe AI
-   **Student:**  Rishabh Bahadur
-   **GitHub repository:** https://github.com/RishabhBahadur/CODSOFT_TASK1
-   **LinkedIn demo video:** Add your post URL
-   **Completion date:** 19/11/26
