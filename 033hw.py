import unittest


class TicTacToe:
    def __init__(self, player):
        self.game_board = {f"{row}{col}": 'e' for row in "ABC" for col in
                           "123"}
        self.player = player

    def make_move(self, row, col):
        r = ['A', 'B', 'C']
        key = r[row - 1] + str(col)
        self.game_board[key] = self.player
        if self.game_board[key] == 'e':
            self.game_board[key] = self.player
            self.player = 'X' if self.player == 'O' else 'O'

    def get_winner(self):
        for row in "ABC":
            if self.game_board[f"{row}1"] == self.game_board[f"{row}2"] == \
                    self.game_board[f"{row}3"] != 'e':
                return self.game_board[f"{row}1"]

        for col in "123":
            if self.game_board[f"A{col}"] == self.game_board[f"B{col}"] == \
                    self.game_board[f"C{col}"] != 'e':
                return self.game_board[f"A{col}"]

        if self.game_board["A1"] == self.game_board["B2"] == \
                self.game_board["C3"] != 'e':
            return self.game_board["A1"]
        if self.game_board["A3"] == self.game_board["B2"] == \
                self.game_board["C1"] != 'e':
            return self.game_board["A3"]

        return "Ничья"

    def is_game_over(self):
        if self.get_winner() in ['X', 'O']:
            return True

        if 'e' not in self.game_board.values():
            return True

        return False


# test
class MyGameTest(unittest.TestCase):
    def test_game_board(self):
        game1 = TicTacToe('X')
        expected_board = {f"{row}{col}": 'e' for row in "ABC" for col in "123"}
        self.assertEqual(game1.game_board, expected_board)
        self.assertEqual(game1.player, 'X')

    def test_make_move(self):
        game1 = TicTacToe('O')
        expected_board = {'A1': 'e', 'A2': 'O', 'A3': 'e',
                          'B1': 'e', 'B2': 'e', 'B3': 'e',
                          'C1': 'e', 'C2': 'e', 'C3': 'e'}
        game1.make_move(1, 2)
        self.assertEqual(game1.game_board, expected_board)
        self.assertEqual(game1.player, 'O')

    def test_get_winner_row(self):
        game = TicTacToe('X')
        game.game_board = {
            'A1': 'X', 'A2': 'X', 'A3': 'X',
            'B1': 'e', 'B2': 'O', 'B3': 'e',
            'C1': 'O', 'C2': 'e', 'C3': 'e'
        }
        winner = game.get_winner()
        self.assertEqual(winner, 'X')

    def test_get_winner_column(self):
        game = TicTacToe('O')
        game.game_board = {
            'A1': 'O', 'A2': 'X', 'A3': 'e',
            'B1': 'O', 'B2': 'e', 'B3': 'e',
            'C1': 'O', 'C2': 'e', 'C3': 'e'
        }
        winner = game.get_winner()
        self.assertEqual(winner, 'O')

    def test_get_winner_diagonal(self):
        game = TicTacToe('X')
        game.game_board = {
            'A1': 'X', 'A2': 'O', 'A3': 'e',
            'B1': 'O', 'B2': 'X', 'B3': 'e',
            'C1': 'O', 'C2': 'e', 'C3': 'X'
        }
        winner = game.get_winner()
        self.assertEqual(winner, 'X')

    def test_get_winner_draw(self):
        game = TicTacToe('O')
        game.game_board = {
            'A1': 'X', 'A2': 'O', 'A3': 'X',
            'B1': 'X', 'B2': 'O', 'B3': 'O',
            'C1': 'O', 'C2': 'X', 'C3': 'X'
        }
        winner = game.get_winner()
        self.assertEqual(winner, 'Ничья')

    def test_is_game_over_winner(self):
        game = TicTacToe('X')
        game.game_board = {
            'A1': 'X', 'A2': 'X', 'A3': 'X',
            'B1': 'e', 'B2': 'O', 'B3': 'e',
            'C1': 'O', 'C2': 'e', 'C3': 'e'
        }
        is_over = game.is_game_over()
        self.assertTrue(is_over)

    def test_is_game_over_draw(self):
        game = TicTacToe('O')
        game.game_board = {
            'A1': 'X', 'A2': 'O', 'A3': 'X',
            'B1': 'X', 'B2': 'O', 'B3': 'O',
            'C1': 'O', 'C2': 'X', 'C3': 'X'
        }
        is_over = game.is_game_over()
        self.assertTrue(is_over)

    def test_is_game_over_continue(self):
        game = TicTacToe('X')
        game.game_board = {
            'A1': 'X', 'A2': 'O', 'A3': 'X',
            'B1': 'X', 'B2': 'O', 'B3': 'e',
            'C1': 'O', 'C2': 'X', 'C3': 'e'
        }
        is_over = game.is_game_over()
        self.assertFalse(is_over)

