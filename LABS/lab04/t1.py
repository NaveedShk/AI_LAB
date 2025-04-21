from queue import PriorityQueue
from itertools import permutations

def find_path(start, end, grid):
    rows, cols = len(grid), len(grid[0])
    search_queue = PriorityQueue()
    search_queue.put((0, start))
    checked_places = set()
    came_from = {start: None}

    while not search_queue.empty():
        priority, place = search_queue.get()
        if place == end:
            steps = []
            while place:
                steps.append(place)
                place = came_from[place]
            return steps[::-1]

        if place in checked_places:
            continue

        checked_places.add(place)
        row, col = place

        for drow, dcol in [(-1,0), (1,0), (0,-1), (0,1)]:
            new_row, new_col = row + drow, col + dcol
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != '#' and (new_row, new_col) not in checked_places:
                search_queue.put((abs(new_row - end[0]) + abs(new_col - end[1]), (new_row, new_col)))
                if (new_row, new_col) not in came_from:
                    came_from[(new_row, new_col)] = place

    return []

def total_steps(sequence, grid):
    total = []
    for i in range(len(sequence) - 1):
        part = find_path(sequence[i], sequence[i+1], grid)
        if not part:
            return float('inf'), []
        if i > 0:
            part = part[1:]
        total.extend(part)
    return len(total), total

def find_complete_path(maze_map, entrance, targets):
    best_path = float('inf')
    shortest_way = []
    for plan in permutations(targets):
        length, steps = total_steps([entrance] + list(plan), maze_map)
        if length < best_path:
            best_path = length
            shortest_way = steps
    return shortest_way

maze_layout = [
    ['S', '.', '.', '#', '.', '.', 'G'],
    ['#', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '.', '.'],
    ['G', '.', '.', '.', '#', '#', 'G']
]

start_pos = None
all_goals = []
for r in range(len(maze_layout)):
    for c in range(len(maze_layout[0])):
        if maze_layout[r][c] == 'S':
            start_pos = (r, c)
        elif maze_layout[r][c] == 'G':
            all_goals.append((r, c))

result_path = find_complete_path(maze_layout, start_pos, all_goals)
print("Shortest journey visiting all goals:")
print(result_path)
