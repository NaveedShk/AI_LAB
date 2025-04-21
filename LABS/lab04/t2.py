import random
import time
import threading
from queue import PriorityQueue

def astar(start, goal, graph, cost):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in graph.get(current, []):
            temp = g_score[current] + cost[current][neighbor]
            if neighbor not in g_score or temp < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp
                f_score[neighbor] = temp + heuristic(neighbor, goal)
                open_set.put((f_score[neighbor], neighbor))

    return []

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def update_costs_randomly(cost, graph, lock):
    while True:
        time.sleep(random.uniform(2, 5))
        lock.acquire()
        for node in graph:
            for neighbor in graph[node]:
                cost[node][neighbor] = random.randint(1, 10)
        lock.release()

def build_grid_graph(n, m):
    g = {}
    c = {}
    for i in range(n):
        for j in range(m):
            g[(i, j)] = []
            c[(i, j)] = {}
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    g[(i,j)].append((ni,nj))
                    c[(i,j)][(ni,nj)] = random.randint(1, 10)
    return g, c

size_x, size_y = 6, 6
start_point = (0, 0)
goal_point = (5, 5)

graph, cost_map = build_grid_graph(size_x, size_y)
cost_lock = threading.Lock()

update_thread = threading.Thread(target=update_costs_randomly, args=(cost_map, graph, cost_lock), daemon=True)
update_thread.start()

for _ in range(5):
    cost_lock.acquire()
    path = astar(start_point, goal_point, graph, cost_map)
    cost_lock.release()
    print("Path:", path)
    time.sleep(3)
