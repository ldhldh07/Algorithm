N = int(input())
triangle = []
for _ in range(N):
    arr = [0] + list(map(int, input().split())) +[0]
    triangle.append(arr)

dp = [[0, triangle[0][1], 0]]
for i in range(1, N):
    dp.append([])
    for j in range(0, 2+i):
        dp[i].append(max(dp[i-1][j-1], dp[i-1][j])+triangle[i][j])
    dp[i].append(0)
print(max(dp.pop()))