class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return f"{self.name} - ({self.symbol})"


class Board:
    def __init__(self):
        self.size = 3
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]

    def display(self):
        for row in self.grid:
            print("|".join(row) + "|")
            print("-" * (self.size * 2 + 1))

    def is_valid_move(self, row, col) -> bool:
        return row in range(self.size) and col in range(self.size) and self.grid[row][col] == ' '

    def make_move(self, row, col, symbol) -> bool:
        if not self.is_valid_move(row,col):
            return False

        self.grid[row][col] = symbol
        return True

    def check_winner(self, symbol: str) -> bool:
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True

        for col in range(self.size):
            if all(self.grid[row][col] == symbol for row in range(self.size)):
                return True

        if all(self.grid[i][i] == symbol for i in range(self.size)):
            return True
        if all(self.grid[i][self.size-1-i] == symbol for i in range(self.size)):
            return True

        return False

    def is_full(self):
        return all(cell != ' ' for row in self.grid for cell in row)


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player = 0

    def get_current_player(self):
        return self.players[self.current_player]

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def play_turn(self):
        player = self.get_current_player()
        print()
        print(f"Current Move: {player}")
        self.board.display()

        while True:
            try:
                row = int(input("Enter row (0-2):"))
                col = int(input("Enter col (0-2):"))

                if self.board.make_move(row, col, player.symbol):
                    break
                else:
                    print("Invalid move. Try again")

            except ValueError:
                print("Invalid Input. Try again")

    def play(self):
        while True:
            self.play_turn()

            winner = self.board.check_winner(self.get_current_player().symbol)
            if winner:
                self.board.display()
                print(f"{winner} wins!")
                break

            if self.board.is_full():
                self.board.display()
                print("It's a Tie!")
                break

            self.switch_player()


def main():
    p1 = str(input("Enter Player X name: "))
    p2 = str(input("Enter Player O name: "))

    player1 = Player(p1, "X")
    player2 = Player(p2, "O")
    game = Game(player1, player2)
    game.play()


if __name__ == '__main__':
    main()
