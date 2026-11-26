
from ai import TicTacToeAI
from game import TicTacToe

game = TicTacToe()
ai = TicTacToeAI()

# Human plays first
game.make_move(0, "X")

# AI calculates its best move
move = ai.best_move(game.board)

print("AI selected position:", move)

game.make_move(move, "O")

game.display_board()
