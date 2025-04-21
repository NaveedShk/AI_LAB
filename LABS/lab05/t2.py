import random
import math

def calc_dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def total_dist(path):
    return sum(calc_dist(path[i], path[i + 1]) for i in range(len(path) - 1))

def hill_climb(points):
    curr = points[:]
    random.shuffle(curr)
    curr_cost = total_dist(curr)
    while True:
        changed = False
        for i in range(len(curr)):
            for j in range(i + 1, len(curr)):
                temp = curr[:]
                temp[i], temp[j] = temp[j], temp[i]
                temp_cost = total_dist(temp)
                if temp_cost < curr_cost:
                    curr = temp
                    curr_cost = temp_cost
                    changed = True
        if not changed:
            break
    return curr, curr_cost

places = [(0,0), (2,5), (5,2), (3,6), (8,3), (2,8)]
path, dist = hill_climb(places)
print("Optimized Route:", path)
print("Total Distance:", dist)
