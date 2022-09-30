def cart(i, n, s):
    global min_battery
    if 0 not in visited:
        s += arr[i-1][0]
        if s < min_battery:
            min_battery = s
    elif s >= min_battery:
        return
    else:
        for j in range(1, n+1):
            if visited[j-1] == 0:
                visited[j-1] = 1
                cart(j, n, s + arr[i-1][j-1])
                visited[j-1] = 0


T = int(input())

for t in range(1, 1+T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N)
    min_battery = 100 * N + 1

    visited[0] = 1
    cart(1, N, 0)
    print('#{} {}'.format(t, min_battery))
