T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(K):
        a, b, n, d = map(int, input().split())
        arr[a][b] = (n, d)

    for _ in range(M):
        for i in range(N):
            for j in range(N):
                if