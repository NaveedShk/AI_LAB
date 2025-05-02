import copy

EMPTY = 0
WHITE = 1
BLACK = 2

class Game:
    def __init__(self):
        self.board = self.make_board()
        self.turn = WHITE

    def make_board(self):
        b = [[EMPTY]*8 for _ in range(8)]
        for i in range(3):
            for j in range(8):
                if (i+j)%2==1:
                    b[i][j] = BLACK
        for i in range(5,8):
            for j in range(8):
                if (i+j)%2==1:
                    b[i][j] = WHITE
        return b

    def print_board(self):
        for row in self.board:
            print(row)

    def get_all_moves(self, color):
        moves = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == color:
                    moves += self.get_piece_moves(i, j, color)
        return moves

    def get_piece_moves(self, r, c, color):
        dirs = [(-1,-1), (-1,1)] if color == WHITE else [(1,-1), (1,1)]
        result = []
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0<=nr<8 and 0<=nc<8 and self.board[nr][nc]==EMPTY:
                result.append(((r,c),(nr,nc)))
            elif 0<=nr<8 and 0<=nc<8 and self.board[nr][nc]!=color:
                jr, jc = nr+dr, nc+dc
                if 0<=jr<8 and 0<=jc<8 and self.board[jr][jc]==EMPTY:
                    result.append(((r,c),(jr,jc)))
        return result

    def move_piece(self, move):
        (sr, sc), (er, ec) = move
        color = self.board[sr][sc]
        self.board[sr][sc] = EMPTY
        self.board[er][ec] = color
        if abs(sr-er) == 2:
            self.board[(sr+er)//2][(sc+ec)//2] = EMPTY

    def is_game_over(self):
        return not self.get_all_moves(WHITE) or not self.get_all_moves(BLACK)

    def evaluate(self):
        w = b = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j]==WHITE:
                    w += 1
                elif self.board[i][j]==BLACK:
                    b += 1
        return b - w

    def minimax(self, depth, alpha, beta, max_player):
        if depth == 0 or self.is_game_over():
            return self.evaluate(), None
        color = BLACK if max_player else WHITE
        moves = self.get_all_moves(color)
        best_move = None
        if max_player:
            max_eval = float('-inf')
            for move in moves:
                g = copy.deepcopy(self)
                g.move_piece(move)
                eval,_ = g.minimax(depth-1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in moves:
                g = copy.deepcopy(self)
                g.move_piece(move)
                eval,_ = g.minimax(depth-1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def play(self):
        while not self.is_game_over():
            self.print_board()
            if self.turn == WHITE:
                m = input("Enter move (r1,c1 r2,c2): ")
                r1,c1,r2,c2 = map(int, m.replace(',', ' ').split())
                move = ((r1,c1),(r2,c2))
                if move in self.get_all_moves(WHITE):
                    self.move_piece(move)
                    print(f"Player moves: ({r1},{c1}) → ({r2},{c2})")
                    self.turn = BLACK
                else:
                    print("Invalid move, try again")
            else:
                _, move = self.minimax(4, float('-inf'), float('inf'), True)
                if move:
                    (sr,sc),(er,ec) = move
                    self.move_piece(move)
                    print(f"AI moves: ({sr},{sc}) → ({er},{ec})")
                self.turn = WHITE

g = Game()
g.play()
