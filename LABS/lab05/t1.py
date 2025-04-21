import chess
import heapq
import itertools

def eval_board(board):
    value = 0
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9
    }
    for p in piece_values:
        value += len(board.pieces(p, chess.WHITE)) * piece_values[p]
        value -= len(board.pieces(p, chess.BLACK)) * piece_values[p]
    return value

def beam_search(board, beam_width, depth_limit):
    counter = itertools.count()
    heap = []
    heapq.heappush(heap, (-eval_board(board), next(counter), [], board))

    for _ in range(depth_limit):
        temp = []
        while heap:
            score, _, moves, b = heapq.heappop(heap)
            for move in b.legal_moves:
                new_b = b.copy()
                new_b.push(move)
                new_s = -eval_board(new_b)
                temp.append((new_s, next(counter), moves + [move], new_b))
        temp.sort(key=lambda x: x[0])
        heap = temp[:beam_width]

    if heap:
        s, _, m, _ = heap[0]
        return m, -s
    return [], 0

board = chess.Board()
beam_width = 4
depth_limit = 3
best_moves, score = beam_search(board, beam_width, depth_limit)
print("Best Move Sequence:", best_moves)
print("Evaluation Score:", score)
