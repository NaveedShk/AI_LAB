import random

class Battleship:
    def __init__(self):
        self.board_size = 10
        self.player_board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ai_board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.player_ships = [(2, 2), (4, 5), (7, 8)]
        self.ai_ships = [(3, 3), (6, 6), (8, 9)]
    
    def print_board(self, board):
        for row in board:
            print(' '.join(row))
    
    def attack(self, board, x, y):
        if board[x][y] == 'S':
            board[x][y] = 'H'
            return True
        return False
    
    def ai_attack(self):
        x, y = random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1)
        return x, y

    def player_turn(self, x, y):
        if self.attack(self.ai_board, x, y):
            print(f"Player attacks: {chr(65 + x)}{y + 1} → Hit!")
        else:
            print(f"Player attacks: {chr(65 + x)}{y + 1} → Miss")
    
    def ai_turn(self):
        x, y = self.ai_attack()
        if self.attack(self.player_board, x, y):
            print(f"AI attacks: {chr(65 + x)}{y + 1} → Hit!")
        else:
            print(f"AI attacks: {chr(65 + x)}{y + 1} → Miss")

    def check_win(self, board):
        for row in board:
            if 'S' in row:
                return False
        return True

game = Battleship()
while True:
    player_x, player_y = map(int, input("Enter player attack (row col): ").split())
    game.player_turn(player_x, player_y)
    if game.check_win(game.ai_board):
        print("Player wins!")
        break
    game.ai_turn()
    if game.check_win(game.player_board):
        print("AI wins!")
        break
