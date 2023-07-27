def sliding_window(arr, k, is_row):
    global max_star
    arr.sort()

    end = 0
    last_start = -1
    last_end = -1

    for start in range(k):
        while end < k and arr[end][0] - arr[start][0] <= L:
            end += 1
        if start != last_start and end != last_end:
            if is_row:
                max_star = max(max_star, end-start)
            else:
                sliding_window([(y, x) for (x, y) in arr[start:end]], end-start, True)
        last_start = start
        last_end = end

N, M, L, K = map(int, input().split())

stars = [tuple(map(int, input().split())) for _ in range(K)]

max_star = 0
sliding_window(stars, K, False)
print(K-max_star)