
from game import TicTacToe

game = TicTacToe()

game.make_move(0, "X")
game.make_move(3, "O")
game.make_move(1, "X")
game.make_move(4, "O")
game.make_move(2, "X")

game.display_board()

print("Winner:", game.check_winner())
