def max_move(arr, l, r, a, b):
    if l > r:
        return 0
    v = float('-inf')
    v = max(v, arr[l] + min_move(arr, l + 1, r, a, b))
    if v >= b:
        return v
    a = max(a, v)
    v = max(v, arr[r] + min_move(arr, l, r - 1, a, b))
    return v

def min_move(arr, l, r, a, b):
    if l > r:
        return 0
    v = float('inf')
    v = min(v, max_move(arr, l + 1, r, a, b))
    if v <= a:
        return v
    b = min(b, v)
    v = min(v, max_move(arr, l, r - 1, a, b))
    return v

def game(arr):
    l = 0
    r = len(arr) - 1
    max_score = 0
    min_score = 0
    turn = "max"
    print("Initial Cards:", arr)
    while l <= r:
        if turn == "max":
            left = arr[l] + min_move(arr, l + 1, r, float('-inf'), float('inf'))
            right = arr[r] + min_move(arr, l, r - 1, float('-inf'), float('inf'))
            if left >= right:
                pick = arr[l]
                l += 1
            else:
                pick = arr[r]
                r -= 1
            max_score += pick
            print(f"Max picks {pick}, Remaining Cards: {arr[l:r+1]}")
            turn = "min"
        else:
            if arr[l] <= arr[r]:
                pick = arr[l]
                l += 1
            else:
                pick = arr[r]
                r -= 1
            min_score += pick
            print(f"Min picks {pick}, Remaining Cards: {arr[l:r+1]}")
            turn = "max"
    print(f"Final Scores - Max: {max_score}, Min: {min_score}")
    if max_score > min_score:
        print("Winner: Max")
    elif max_score < min_score:
        print("Winner: Min")
    else:
        print("It's a Draw")

game([4, 10, 6, 2, 9, 5])
