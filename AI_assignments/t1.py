def query(x):
    return -1 * (x - 7)**2 + 49

def find_peak(n):
    x = 0
    while x < n:
        if query(x + 1) > query(x):
            x += 1
        else:
            break
    return x

N = 14
peak = find_peak(N)
print("Peak index:", peak)
print("Peak elevation:", query(peak))
