class TicTacToe:

    def __init__(self):
        self.board = [[' '] * 3 for _ in range(3)]
        self.current_player = 1

    def print(self):
        for row in self.board:
            print("|".join(row))
            print("-"*5)

    def play(self, row, col):

        if row in range(3) and col in range(3) and self.board[row][col] == ' ':
            self.board[row][col] = "X" if self.current_player == 1 else "0"
            return True

        print("Invalid Move!")
        return False


    def have_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
            if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
                return True
            if self.board[2][0] == self.board[1][1] == self.board[0][2] != ' ':
                return True
            return False

    def change_player(self):
        self.current_player = 3 - self.current_player

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)


def main():
    game = TicTacToe()

    while True:
        game.print()
        line = input(f"Player {game.current_player} enter your move (row col):")
        if line:
            row, col = map(int, line.split())
            game.play(row, col)

            if game.have_winner():
                game.print()
                winner = "Player 1" if game.current_player == 1 else "Player 2"
                print(f"Player {game.current_player} wins!")
                break
            elif game.is_full():
                game.print()
                print("It is a Draw!")
            else:
                game.change_player()


if __name__ == "__main__":
    main()

