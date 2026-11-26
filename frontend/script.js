
const cells = document.querySelectorAll(".cell");

const statusText = document.getElementById("status");
const resetButton = document.getElementById("reset-button");
const difficultySelector = document.getElementById("difficulty");

const humanScore = document.getElementById("human-score");
const aiScore = document.getElementById("ai-score");
const drawScore = document.getElementById("draw-score");


// ==========================================
// 1. GET GAME STATE
// ==========================================

async function getGameState() {
    try {
        const response = await fetch("/api/state");
        const data = await response.json();

        if (!response.ok) {
            throw new Error("Could not load game state.");
        }

        updateBoard(data);

        if (difficultySelector && data.difficulty) {
            difficultySelector.value = data.difficulty;
        }

    } catch (error) {
        statusText.textContent = "Could not connect to the server.";
        console.error(error);
    }
}


// ==========================================
// 2. CHECK WINNING LINE
// ==========================================

function getWinningLine(board) {

    const combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    for (const line of combinations) {

        const [a, b, c] = line;

        if (
            board[a] &&
            board[a] === board[b] &&
            board[b] === board[c]
        ) {
            return line;
        }
    }

    return [];
}


// ==========================================
// 3. UPDATE GAME BOARD
// ==========================================


function updateBoard(data) {
    const winningLine = getWinningLine(data.board);

    data.board.forEach((value, index) => {
        const isOccupied = value !== " ";

        cells[index].textContent = isOccupied ? value : "";

        // Disable only occupied cells or when the game is over
        cells[index].disabled = isOccupied || data.game_over;

        cells[index].classList.toggle(
            "winning",
            winningLine.includes(index) && data.game_over
        );
    });

    humanScore.textContent = data.scores.human;
    drawScore.textContent = data.scores.draw;
    aiScore.textContent = data.scores.ai;

    if (data.game_over) {
        if (data.winner === "X") {
            statusText.textContent = "You won!";
        } else if (data.winner === "O") {
            statusText.textContent = "AI wins!";
        } else {
            statusText.textContent = "It's a draw!";
        }
    } else {
        statusText.textContent = "Your turn (X)";
    }
}



// ==========================================
// 4. HUMAN AND AI MOVES
// ==========================================

async function makeMove(position) {

    try {

        const response = await fetch("/api/move", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                position: position
            })
        });

        const data = await response.json();

        if (!response.ok) {

            statusText.textContent =
                data.error || "Something went wrong.";

            return;
        }

        updateBoard(data);

    } catch (error) {

        statusText.textContent =
            "Could not connect to the game server.";

        console.error(error);
    }
}


// ==========================================
// 5. CELL CLICK EVENTS
// ==========================================

cells.forEach((cell) => {

    cell.addEventListener("click", () => {

        const position = Number(cell.dataset.position);

        if (!cell.disabled) {
            makeMove(position);
        }
    });
});


// ==========================================
// 6. RESET GAME
// ==========================================

resetButton.addEventListener("click", async () => {

    try {

        const response = await fetch("/api/reset", {
            method: "POST"
        });

        const data = await response.json();

        updateBoard(data);

    } catch (error) {

        statusText.textContent =
            "Could not reset the game.";

        console.error(error);
    }
});


// ==========================================
// 7. CHANGE AI DIFFICULTY
// ==========================================

difficultySelector.addEventListener("change", async () => {

    const selectedDifficulty = difficultySelector.value;

    try {

        const response = await fetch("/api/difficulty", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                difficulty: selectedDifficulty
            })
        });

        const data = await response.json();

        if (!response.ok) {

            alert(data.error || "Could not change difficulty.");

            return;
        }

        // Reset board after changing difficulty
        const resetResponse = await fetch("/api/reset", {
            method: "POST"
        });

        const gameData = await resetResponse.json();

        updateBoard(gameData);

    } catch (error) {

        statusText.textContent =
            "Could not connect to the server.";

        console.error(error);
    }
});


// ==========================================
// 8. INITIALIZE GAME
// ==========================================

getGameState();
