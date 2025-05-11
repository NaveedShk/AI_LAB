import random

tsk = [1, 2, 3, 4, 5, 6, 7]
t = {1:5, 2:8, 3:4, 4:7, 5:6, 6:3, 7:9}
fac = [1, 2, 3]
cap = {1:24, 2:30, 3:28}
cst = {
    1: {1:10, 2:12, 3:9},
    2: {1:15, 2:14, 3:16},
    3: {1:8, 2:9, 3:7},
    4: {1:12, 2:10, 3:13},
    5: {1:14, 2:13, 3:12},
    6: {1:9, 2:8, 3:10},
    7: {1:11, 2:12, 3:13}
}

def make_data(n):
    return [[random.choice(fac) for _ in range(7)] for _ in range(n)]

def fit(x):
    cost = 0
    time_used = {1: 0, 2: 0, 3: 0}
    for i, f in zip(tsk, x):
        tm = t[i]
        cost += tm * cst[i][f]
        time_used[f] += tm
    max_time = max(time_used.values())
    pen = 0
    for f in fac:
        if time_used[f] > cap[f]:
            pen += 10000 * (time_used[f] - cap[f])
    return -(cost + max_time + pen)

def pick(ppl, scores):
    w = [s + abs(min(scores)) + 1 for s in scores]
    a = random.choices(ppl, weights=w, k=1)[0]
    b = random.choices(ppl, weights=w, k=1)[0]
    while a == b:
        b = random.choices(ppl, weights=w, k=1)[0]
    return a, b

def cross(a, b, rate=0.8):
    if random.random() <= rate:
        p = random.randint(1, 6)
        c1 = a[:p] + b[p:]
        c2 = b[:p] + a[p:]
        return c1, c2
    return a[:], b[:]

def change(x, rate=0.2):
    if random.random() < rate:
        i, j = random.sample(range(len(x)), 2)
        x[i], x[j] = x[j], x[i]
    return x

def run(n, g):
    pop = make_data(n)
    for _ in range(g):
        sc = [fit(x) for x in pop]
        new_pop = []
        for _ in range(n // 2):
            p1, p2 = pick(pop, sc)
            c1, c2 = cross(p1, p2)
            new_pop += [change(c1), change(c2)]
        pop = new_pop
    best = max(pop, key=fit)
    return best

ans = run(6, 200)
print("Best:", ans)
print("Score:", fit(ans))
