
import math


class TicTacToeAI:

    def __init__(self):
        self.ai_player = "O"
        self.human_player = "X"

    def minimax(self, board, depth, is_maximizing, alpha, beta):

        winner = self.check_winner(board)

        if winner == self.ai_player:
            return 10 - depth

        if winner == self.human_player:
            return depth - 10

        if winner == "Draw":
            return 0

        if is_maximizing:
            best_score = -math.inf

            for move in self.available_moves(board):
                board[move] = self.ai_player

                score = self.minimax(
                    board, depth + 1, False, alpha, beta
                )

                board[move] = " "

                best_score = max(best_score, score)
                alpha = max(alpha, best_score)

                if beta <= alpha:
                    break

            return best_score

        else:
            best_score = math.inf

            for move in self.available_moves(board):
                board[move] = self.human_player

                score = self.minimax(
                    board, depth + 1, True, alpha, beta
                )

                board[move] = " "

                best_score = min(best_score, score)
                beta = min(beta, best_score)

                if beta <= alpha:
                    break

            return best_score

    def best_move(self, board):
        best_score = -math.inf
        move = None

        for position in self.available_moves(board):
            board[position] = self.ai_player

            score = self.minimax(
                board, 0, False, -math.inf, math.inf
            )

            board[position] = " "

            if score > best_score:
                best_score = score
                move = position

        return move

    def available_moves(self, board):
        return [
            i for i, cell in enumerate(board)
            if cell == " "
        ]

    def check_winner(self, board):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for a, b, c in winning_combinations:
            if (board[a] == board[b] == board[c]
                    != " "):
                return board[a]

        if " " not in board:
            return "Draw"

        return None
