import sys
sys.setrecursionlimit(10 ** 6)

def dfs(i, j):
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        ni, nj = i+di, j + dj
        if arr[ni][nj] == 1:
            arr[ni][nj] = -1
            dfs(ni,nj)



T = int(input())


for t in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0] * (M+2) for _ in range(N+2)]
    for _ in range(K):
        j, i = map(int, input().split())
        arr[i+1][j+1] = 1
    cnt = 0

    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j] == 1:
                arr[i][j] = -1
                cnt += 1
                dfs(i, j)

    print(cnt)