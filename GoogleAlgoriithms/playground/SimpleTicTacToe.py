"""
_ _ _
_ _ _
_ _ _

rows 0,1,2
cols 0,1,2
diag row == col
anti diag col == n - row - 1

# col = 3 - 2 - 1 == 0
# col = 3 - 1 - 1 == 1
"""


class TicTacToe:

    def __init__(self, size):
        self.rows = [0] * size
        self.cols = [0] * size
        self.diag = 0
        self.diag2 = 0
        self.n = size

    def _is_win_(self, row, col, player):
        if (abs(self.rows[row]) == self.n
                or abs(self.cols[col]) == self.n
                or abs(self.diag) == self.n
                or abs(self.diag2) == self.n
        ):
            return True

        return False

    def _play_(self, row, col, player):
        move = 1 if player == 1 else - 1

        self.rows[row] += move
        self.cols[col] += move
        if row == col:
            self.diag += move

        if col == self.n - row - 1:
            self.diag2 += move

    def move(self, row: int, col: int, player: int):
        print(f"row={row}, col={col}, player= {player}")

        self._play_(row, col, player)

        if self._is_win_(row, col, player):
            print(f'player {player} wins!')
            return player

        return 0


if __name__ == "__main__":
    game = TicTacToe(3)
    game.move(0, 0, 1)
    game.move(1, 0, 1)
    game.move(2, 0, 1)
