def move(x, y, n):
    global min_route
    global sum_route
    sum_route += arr[x][y]
    if x == (n-1) and y == (n-1):
        if sum_route < min_route:
            min_route = sum_route
    elif sum_route >= min_route:
        return
    else:
        for dx, dy in [[0,1], [1,0]]:
            nx, ny = x + dx, y + dy
            if arr[nx][ny]:
                move(nx, ny, n)
                sum_route -= arr[nx][ny]


T = int(input())

for t in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]

    min_route = 987654321
    sum_route = 0
    move(0, 0, N)
    print('#{} {}'.format(t, min_route))