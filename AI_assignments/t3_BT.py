import time
from copy import deepcopy
from collections import deque

def load(file):
    lst = []
    with open(file, 'r') as f:
        g = []
        for line in f:
            line = line.strip()
            if not line and g:
                lst.append(g)
                g = []
            elif line:
                g.append([int(ch) for ch in line])
        if g:
            lst.append(g)
    return lst

def get_vars(grid):
    v = []
    d = {}
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                v.append((r, c))
                d[(r, c)] = list(range(1, 10))
            else:
                d[(r, c)] = [grid[r][c]]
    return v, d

def get_ngb(cell):
    r, c = cell
    n = set()
    for i in range(9):
        if i != c:
            n.add((r, i))
        if i != r:
            n.add((i, c))
    sr, sc = (r // 3) * 3, (c // 3) * 3
    for i in range(sr, sr + 3):
        for j in range(sc, sc + 3):
            if (i, j) != (r, c):
                n.add((i, j))
    return n

def run_ac3(d):
    q = deque()
    for x in d:
        for y in get_ngb(x):
            if y in d:
                q.append((x, y))

    while q:
        x, y = q.popleft()
        if change(d, x, y):
            if not d[x]:
                return False
            for z in get_ngb(x):
                if z != y and z in d:
                    q.append((z, x))
    return True

def change(d, x, y):
    done = False
    temp = d[x][:]
    for val in temp:
        if not any(val != v for v in d[y]):
            d[x].remove(val)
            done = True
    return done

def pick_var(d, g):
    for v in d:
        r, c = v
        if g[r][c] == 0:
            return v
    return None

def solve(g, d):
    if all(g[r][c] != 0 for r in range(9) for c in range(9)):
        return g

    v = pick_var(d, g)
    if v is None:
        return g

    r, c = v
    for val in d[v]:
        if all(val != g[nr][nc] for nr, nc in get_ngb(v)):
            g[r][c] = val
            saved = deepcopy(d)
            d[v] = [val]

            if run_ac3(d):
                ans = solve(g, d)
                if ans:
                    return ans

            g[r][c] = 0
            d = saved
    return None

pz = load(r'E:\4th semester\AI Lab\AI_A2\puzzle.txt')

for i, p in enumerate(pz):
    print("Puzzle", i + 1)
    st = time.time()

    g = deepcopy(p)
    _, d = get_vars(g)
    run_ac3(d)
    res = solve(g, d)

    et = time.time()
    t = et - st

    if res:
        for row in res:
            print(' '.join(str(x) for x in row))
    else:
        print("No answer")

    print("Time:", round(t, 4), "sec\n")
