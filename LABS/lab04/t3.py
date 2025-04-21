from queue import PriorityQueue

def greedy_delivery(start, stops):
    path = [start]
    visited = set()
    current = start
    time = 0

    while len(visited) < len(stops):
        queue = PriorityQueue()
        for idx, (point, window) in enumerate(stops):
            if idx in visited:
                continue
            dist = abs(current[0]-point[0]) + abs(current[1]-point[1])
            penalty = max(0, window[0] - (time + dist))
            queue.put((penalty + dist, dist, idx, point, window))

        if queue.empty():
            break

        _, dist, idx, next_stop, window = queue.get()
        visited.add(idx)
        time += dist
        if time < window[0]:
            time = window[0]
        path.append(next_stop)
        current = next_stop

    return path

start_pos = (0, 0)
delivery_points = [
    ((3, 4), (5, 15)),
    ((1, 2), (0, 10)),
    ((6, 1), (10, 20)),
    ((2, 5), (3, 12)),
    ((4, 3), (7, 17))
]

route = greedy_delivery(start_pos, delivery_points)
print("Optimized Route:", route)
