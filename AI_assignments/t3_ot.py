import time
from ortools.sat.python import cp_model

def read_file(name):
    lst = []
    try:
        with open(name, 'r') as f:
            temp = []
            for line in f:
                line = line.strip()
                if not line and temp:
                    lst.append(temp)
                    temp = []
                elif line:
                    temp.append([int(c) for c in line])
            if temp:
                lst.append(temp)
    except:
        print("error")
    return lst

def show(x):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(x[i][j] if x[i][j] != 0 else ".", end=" ")
        print()

def solve_one(p):
    m = cp_model.CpModel()
    cell = {(i, j): m.NewIntVar(1, 9, f'c_{i}_{j}') for i in range(9) for j in range(9)}

    for i in range(9):
        for j in range(9):
            if p[i][j] != 0:
                m.Add(cell[(i, j)] == p[i][j])

    for i in range(9):
        m.AddAllDifferent([cell[(i, j)] for j in range(9)])
        m.AddAllDifferent([cell[(j, i)] for j in range(9)])

    for r in range(3):
        for c in range(3):
            m.AddAllDifferent([
                cell[(r * 3 + i, c * 3 + j)]
                for i in range(3) for j in range(3)
            ])

    s = cp_model.CpSolver()
    st = s.Solve(m)

    if st == cp_model.FEASIBLE or st == cp_model.OPTIMAL:
        return [[s.Value(cell[(i, j)]) for j in range(9)] for i in range(9)]
    return None

def solve_all(lst):
    n = len(lst)
    t1 = time.time()

    for i, p in enumerate(lst, 1):
        print(f"\nPuzzle {i}/{n}")
        print("Input:")
        show(p)

        t2 = time.time()
        out = solve_one(p)
        t3 = time.time()

        if out:
            print("\nOutput:")
            show(out)
            print(f"Time: {t3 - t2:.4f} sec")
        else:
            print("No solution")

    t4 = time.time()
    print(f"\nDone in {t4 - t1:.4f} sec")
    if n:
        print(f"Avg: {(t4 - t1) / n:.4f} sec")

file = r"E:\4th semester\AI Lab\AI_A2\puzzle.txt"
data = read_file(file)

if not data:
    print("No puzzles")
else:
    print(f"{len(data)} puzzle(s)")
    solve_all(data)
