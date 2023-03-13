N = int(input())

first_R, first_G, first_B = map(int, input().split())

dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(N)]

# 첫번째 dp에 넣어주기
for first_color in range(3):
    for dp_color in range(3):
        dp[first_color][dp_color][0] = [first_R, first_G, first_B][dp_color] 

# dp = [[[26, 0, 0], [40, 0, 0], [83, 0, 0]], [[26, 0, 0], [40, 0, 0], [83, 0, 0]], [[26, 0, 0], [40, 0, 0], [83, 0, 0]]]

second_R, second_G, second_B =  map(int, input().split())

# 첫번째 dp에 따라 2번째 dp에는 처음에 들어간 색깔이 안들어가게 설정
for first_color in range(3):
    dp[first_color][0][1] = min(dp[first_color][1][0], dp[first_color][2][0]) + second_R
    dp[first_color][1][1] = min(dp[first_color][0][0], dp[first_color][2][0]) + second_G
    dp[first_color][2][1] = min(dp[first_color][0][0], dp[first_color][1][0]) + second_B
    
    for dp_color in range(3):
        if first_color == dp_color:
            dp[first_color][dp_color][1] = 1001

print(dp)
# dp = [[[26, 1001, 0], [40, 86, 0], [83, 83, 0]], [[26, 89, 0], [40, 1001, 0], [83, 83, 0]], [[26, 89, 0], [40, 86, 0], [83, 1001, 0]]]

for i in range(2, N):

    R, G, B =  map(int, input().split())
    for first_color in range(3):
        dp[first_color][0][i] = min(dp[first_color][1][i-1], dp[first_color][2][i-1]) + R
        dp[first_color][1][i] = min(dp[first_color][0][i-1], dp[first_color][2][i-1]) + G
        dp[first_color][2][i] = min(dp[first_color][0][i-1], dp[first_color][1][i-1]) + B



print(dp)

print(min(dp[0][1][N-1], dp[0][2][N-1], dp[1][0][N-1], dp[1][2][N-1], dp[2][0][N-1], dp[2][1][N-1]))