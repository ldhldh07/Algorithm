N, M, L, K = map(int, input().split())

earth = [[0 for _ in range(M+1)] for _ in range(N+1)]
stars = [list(map(int, input().split())) for _ in range(K)]
for star in stars:
    x, y = star
    min_x, max_x = max(x-L+1, 0), min(x+1, N+1)
    min_y, max_y = max(y-L+1, 0), min(y+1, M+1)

    for x_range in range(min_x, max_x):
        for y_range in range(min_y, max_y):
            earth[x_range][y_range] += 1

max_count = max(map(max, earth))
print(K - max_count)
