import numpy as np

states = ['Sunny', 'Cloudy', 'Rainy']
trans = {
    'Sunny': [0.6, 0.3, 0.1],
    'Cloudy': [0.2, 0.5, 0.3],
    'Rainy': [0.1, 0.4, 0.5]
}

def next_state(curr):
    return np.random.choice(states, p=trans[curr])

def simulate(days):
    seq = ['Sunny']
    for _ in range(days - 1):
        seq.append(next_state(seq[-1]))
    return seq

def count_rainy(seq):
    return seq.count('Rainy')

n = 10000
count = 0
for _ in range(n):
    s = simulate(10)
    if count_rainy(s) >= 3:
        count += 1

prob = count / n
print(prob)
