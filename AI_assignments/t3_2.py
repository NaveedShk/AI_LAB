import time
import copy

def load(file):
    puzzles = []
    with open(file, 'r') as f:
        board = []
        for line in f:
            line = line.strip()
            if not line and board:
                puzzles.append(board)
                board = []
            elif line:
                board.append([int(ch) for ch in line])
        if board:
            puzzles.append(board)
    return puzzles

def show(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('-' * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')
            print(grid[i][j] if grid[i][j] != 0 else '.', end=' ')
        print()

def can_place(grid, row, col, val):
    for i in range(9):
        if grid[row][i] == val or grid[i][col] == val:
            return False
    start_r, start_c = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_r + i][start_c + j] == val:
                return False
    return True

def solve(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for n in range(1, 10):
                    if can_place(grid, r, c, n):
                        grid[r][c] = n
                        if solve(grid):
                            return True
                        grid[r][c] = 0
                return False
    return True

def solve_all(puzzle_list):
    total = len(puzzle_list)
    start = time.time()

    for i, p in enumerate(puzzle_list, 1):
        print(f"\nPuzzle {i}/{total}:")
        print("Input:")
        show(p)

        attempt = copy.deepcopy(p)
        t0 = time.time()
        done = solve(attempt)
        t1 = time.time()

        if done:
            print("\nSolved:")
            show(attempt)
            print(f"Time: {t1 - t0:.4f} sec")
        else:
            print("\nNo solution found.")

    duration = time.time() - start
    print(f"\nFinished in {duration:.4f} sec")
    print(f"Average time: {duration / total:.4f} sec")

if __name__ == "__main__":
    file = r"E:\4th semester\AI Lab\AI_A2\puzzle.txt"
    try:
        all_puzzles = load(file)
        if not all_puzzles:
            print(f"No puzzles in {file}")
        else:
            print(f"Read {len(all_puzzles)} puzzles from {file}")
            solve_all(all_puzzles)
    except FileNotFoundError:
        print(f"File not found: {file}")
    except Exception as e:
        print(f"Problem: {str(e)}")
