
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(i,j):
    global ans
    if arr[i][j] == 0:
        arr[i][j] = 2
        ans += 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i + di, j + dj
            dfs(ni, nj)
        else:
            return ans

M, N, K = map(int, input().split())
arr = [[1] * (N+2)] + [[1] + [0] * (N) + [1] for _ in range(M)] + [[1] * (N+2)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(M-y2+1,M-y1+1):
        for j in range(x1+1, x2+1):
            arr[i][j] = 1
ans_list = []
len_ans = 0
for i in range(1, M+1):
    for j in range(1, N+1):
        ans = 0
        dfs(i, j)
        if ans:
            len_ans +=1
            ans_list.append(ans)

ans_list.sort()
print(len_ans)
print(" ".join(map(str, ans_list)))
    