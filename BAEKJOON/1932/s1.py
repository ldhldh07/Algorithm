N = int(input())
triangle = []
for _ in range(N):
    arr = [0] + list(map(int, input().split())) + [0]     # 삼각형 배열을 2차원 배열에 받아줍니다
    triangle.append(arr)                                  # 앞뒤로 0 하나씩 넣어줍니다
                                                          # 삼각형 배열의 원소마다 그 원소까지 내려갔을 때의 최대값을 구합니다
dp = [[0, triangle[0][1], 0]]                             # 첫번째 원소만 넣어줍니다
for i in range(1, N):                                     # 각 줄마다
    dp.append([])
    for j in range(2+i):                                  # 0 제외한 각 원소마다
        dp[i].append(max(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]) # 이전 줄에서 같은 번째 순서와 이전 순서 중 더 큰값에서 원소값 더해줍니다
    dp[i].append(0)                                       # 맨 뒤에 0 들어가게 해줍니다
print(max(dp.pop()))                                      # 마지막 줄에서 가장 큰 값을 구해줍니다
