# Tic-Tac-Toe AI

A browser-based Tic-Tac-Toe game where a human player competes against
an AI opponent. The AI uses the **Minimax algorithm with Alpha-Beta
Pruning** to choose strong moves. The application uses Python and Flask
for the backend and HTML, CSS, and JavaScript for the frontend.

## Features

-   Human (`X`) versus AI (`O`) gameplay.
-   Minimax-based AI decision-making.
-   Alpha-Beta Pruning to reduce unnecessary search.
-   Three difficulty settings:
    -   **Easy:** AI selects a random available move.
    -   **Medium:** AI has a 50% chance of selecting a random move;
        otherwise it uses Minimax.
    -   **Hard:** AI uses Minimax to select its move.
-   Scoreboard for human wins, draws, and AI wins.
-   Reset button to start a new round.
-   Browser-based interface served by Flask.

## Technology Stack

  Technology           Purpose
  -------------------- ----------------------------------------
  Python               Game logic and AI
  Flask                Web server and API
  HTML                 Page structure
  CSS                  Styling and responsive layout
  JavaScript           User interaction and API communication
  Minimax              AI move selection
  Alpha-Beta Pruning   Search optimization

## Project Structure

``` text

CODSOFT_TASK1/
│
├── backend/
│   ├── __init__.py
│   ├── app.py
│   ├── ai.py
│   └── game.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── prototype/
│   └── main.py
│
├── screenshots/
│   └── (Project screenshots)
│
├── test_ai.py
├── test_game.py
├── PROJECT_DOCUMENTATION.md
├── README.md
├── requirements.txt
└── .gitignore

```

## Setup and Run

### 1. Clone the repository

``` bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd TicTacToe-AI
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

``` powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run the environment's Python
directly using `.\venv\Scripts\python.exe`.

### 3. Install Flask

``` powershell
python -m pip install Flask
```

If a `requirements.txt` file is added to the repository, use:

``` powershell
python -m pip install -r requirements.txt
```

### 4. Start the application

Run this command from the project root:

``` powershell
python -m backend.app
```

### 5. Open the game

Visit:

``` text
http://127.0.0.1:5000
```

Keep the terminal running while you play. Press `Ctrl + C` in the
terminal to stop the server.

## How to Play

1.  Open the application in your browser.
2.  Select Easy, Medium, or Hard.
3.  Click an empty square to place `X`.
4.  The AI responds with `O`.
5.  The game announces a win or draw and updates the scoreboard.
6.  Select Reset to start another round.

## API Overview

The Flask application exposes the following routes:

  Route               Method   Purpose
  ------------------- -------- --------------------------------------------
  `/`                 GET      Serves the game interface
  `/api/state`        GET      Returns the current game state
  `/api/move`         POST     Processes a human move and the AI response
  `/api/difficulty`   POST     Changes the AI difficulty
  `/api/reset`        POST     Resets the current round

The move endpoint accepts a JSON object containing the selected board
position, for example:

``` json
{
  "position": 4
}
```

The exact response fields are implemented in `backend/app.py`; consult
that file if the API is changed.

## AI Algorithm

The AI evaluates possible future game states using Minimax. The
algorithm considers available moves and assumes both players make
rational decisions. It selects a move that maximizes the AI's outcome
while accounting for the human player's best response.

Alpha-Beta Pruning improves the search by skipping branches that cannot
affect the final decision. It preserves Minimax's result while
potentially examining fewer game states.

## Testing Checklist

-   [ ] The page loads at `http://127.0.0.1:5000`.
-   [ ] A human can select an empty cell.
-   [ ] The AI responds after a valid human move.
-   [ ] An occupied cell cannot be selected again.
-   [ ] Easy, Medium, and Hard difficulty options can be selected.
-   [ ] Wins and draws are detected correctly.
-   [ ] The scoreboard updates correctly.
-   [ ] Reset starts a new round.
-   [ ] The browser console and Flask terminal show no application
    errors.

## Limitations

-   The application is a small educational game, not a production
    service.
-   The game state and scores are held in the running Flask process;
    they are not stored in a database.
-   The project is intended for local demonstration unless deployment
    and multi-user state handling are added.

## Future Improvements

-   Add sound effects and improved animations.
-   Add a difficulty explanation or AI-thinking indicator.
-   Add persistent statistics using a database or local storage.
-   Add automated tests for the Flask API and complete game flow.
-   Deploy the application so it can be played online.

## Internship Submission

-   **Internship:** CodSoft Artificial Intelligence Internship
-   **Task:** Tic-Tac-Toe AI
-   **GitHub repository:** Add your repository URL here
-   **Demo video:** Add your LinkedIn video post URL here
-   **LinkedIn Link:**: www.linkedin.com/in/rishabh-bahadur
------------------------------------------------------------------------

Built as an educational project to explore game-playing AI, backend
APIs, and frontend development.
