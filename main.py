class Board:
    def __init__(self):
        self.board = {
            "0": " ", "1": " ", "2": " ",
            "3": " ", "4": " ", "5": " ",
            "6": " ", "7": " ", "8": " "
        }

    def print_board(self):
        print(self.board["0"] + "|" + self.board["1"] + "|" + self.board["2"])
        print("-+-+-")
        print(self.board["3"] + "|" + self.board["4"] + "|" + self.board["5"])
        print("-+-+-")
        print(self.board["6"] + "|" + self.board["7"] + "|" + self.board["8"])

# stops the player trying to place here if the space is already taken
    def _is_valid_move(self, position):
        if self.board.get(position) == " ":
            return True
        return False

    def change_board(self, position, type):
        if self._is_valid_move(position):
            self.board[position] = type
            return self.board
        return None

 # winning lines    
    def is_winner(self, player):
        b = self.board
        p = player.type
        if (b["0"] == p and b["1"] == p and b["2"] == p) or \
           (b["3"] == p and b["4"] == p and b["5"] == p) or \
           (b["6"] == p and b["7"] == p and b["8"] == p) or \
           (b["0"] == p and b["3"] == p and b["6"] == p) or \
           (b["1"] == p and b["4"] == p and b["7"] == p) or \
           (b["2"] == p and b["5"] == p and b["8"] == p) or \
           (b["0"] == p and b["4"] == p and b["8"] == p) or \
           (b["6"] == p and b["4"] == p and b["2"] == p):
            return True
        return False

# allocate the players with their character: X / O
class Player:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return "Player {}".format(self.type)

# allocate X to players 1
class Game:
    def __init__(self):
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board()

# start message
    def print_valid_entries(self):
        print("""
            0 - top left | 1 - top middle | 2 - top right
            3 - middle left | 4 - middle | 5 - middle right
            6 - bottom left | 7 - bottom middle | 8 - bottom right
        """)

# print the board
    def printing_board(self):
        self.board.print_board()

# player switch between X & O
    def change_turn(self, player):
        return self.player2 if player == self.player1 else self.player1

# label the winner
    def won_game(self, player):
        return self.board.is_winner(player)

# modify the board once a move has been made
    def modify_board(self, position, type):
        if self.board.change_board(position, type) is not None:
            return self.board.change_board(position, type)
        else:
            position = input("Not available position. Please, try again: ")
        return self.board.change_board(position, type)

# game play
    def play(self):
        self.print_valid_entries()
        player = self.player1
        num = 9
        while num > 0:
            num -= 1
            self.printing_board()
            position = input("{} turn, what's your move? ".format(player))
            self.modify_board(position, player.type)
            if self.won_game(player):
                print("{} is the Winner!".format(player))
                self.printing_board()
                break
            else:
                player = self.change_turn(player)
        if num == 0:
            print("Game over! It's a tie!")

if __name__ == "__main__":
    game = Game()
    game.play()
