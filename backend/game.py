
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def display_board(self):
        for row in range(3):
            print(" | ".join(self.board[row * 3:(row + 1) * 3]))
            if row < 2:
                print("---------")

    def available_moves(self):
        return [i for i, cell in enumerate(self.board) if cell == " "]

    def make_move(self, position, player):
        if position in self.available_moves():
            self.board[position] = player
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for a, b, c in winning_combinations:
            if (self.board[a] == self.board[b] ==
                    self.board[c] != " "):
                return self.board[a]

        if " " not in self.board:
            return "Draw"

        return None

    def reset(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
