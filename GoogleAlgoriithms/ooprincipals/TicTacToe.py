from enum import Enum


class Symbol(Enum):
    EX = "X"
    CIRCLE = "O"


class Player:
    def __init__(self, name: str, symbol: Symbol):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return f"{self.name} - {self.symbol.value}"


class Board:
    def __init__(self):
        self.size = 3
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]

    def is_valid_move(self, row:int, col:int):
        return row in range(self.size) and col in range(self.size) and self.grid[row][col] == ' '

    def make_move(self, row, col, player: Player):
        if not self.is_valid_move(row, col):
            # print(self.grid[row][col] + " Invalid Move")
            return False

        self.grid[row][col] = player.symbol.value
        return True

    def is_full(self):
        return all(cell != ' ' for row in self.grid for cell in row)

    def is_winner(self, player: Player):
        for row in self.grid:
            if all(cell == player.symbol.value for cell in row):
                return True

        for row in range(self.size):
            if all(self.grid[row][col] == player.symbol for col in range(self.size)):
                return True

        if all(self.grid[i][i] == player.symbol for i in range(self.size)):
            return True

        if all(self.grid[i][self.size - i - 1] == player.symbol for i in range(self.size)):
            return True

        return False


    def display(self):
        for row in self.grid:
            print("|".join(str(cell) for cell in row) + "|")
            print("_" * (self.size * 2 + 1))


class Game:
    def __init__(self, player1:Player, player2:Player):
        self.players = [player1, player2]
        self.board = Board()
        self.currentPlayer = 0


    def get_current_player(self):
        return self.players[self.currentPlayer]

    def next_player(self):
        self.currentPlayer = 1 - self.currentPlayer
        return self.get_current_player()

    def start(self):
        print("Welcome to TicTacToe!")
        print(f"{self.players[0]} against {self.players[1]}")
        while True:
            self.play()
            if self.check_end():
                break
            self.next_player()

    def play(self):
        print()
        self.board.display()
        while True:
            print(f"Next move: {self.get_current_player()}")
            try:
                row = int(input("Row: "))
                col = int(input("Col: "))
                if self.board.make_move(row, col, self.get_current_player()):
                    break
                else:
                    print("Invalid Move!")
            except ValueError:
                print("Invalid Input")


    def check_end(self):
        winner = self.board.is_winner(self.get_current_player())
        if winner:
            print(f"{winner} wins!")
            return True

        if self.board.is_full():
            print("It is a Tie!")
            return True

        return False


def main():
    p1 = str(input("Digite o nome do primeiro jogador (X): "))
    p2 = str(input("Digite o nome do segundo jogador (O): "))

    game = Game(Player(p1, Symbol.EX), Player(p2, Symbol.CIRCLE))
    game.start()


if __name__ == "__main__":
    main()

