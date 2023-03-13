N = int(input())

first_R, first_G, first_B = map(int, input().split())

dp = [[[1001 for _ in range(N)] for _ in range(3)] for _ in range(3)]

# 첫번째 dp에 넣어주기
for first_color in range(3):
    for dp_color in range(3):
        if first_color == dp_color:
            dp[first_color][dp_color][0] = [first_R, first_G, first_B][dp_color] 

for i in range(1, N):
    R, G, B =  map(int, input().split())
    for first_color in range(3):
        for dp_color in range(3):
            # 첫번째 dp에 따라 2번째 dp에는 처음에 들어간 색깔이 안들어가게 설정
            if first_color == dp_color and i == 1:
                dp[first_color][dp_color][i] = 1001
                continue
        dp[first_color][0][i] = min(dp[first_color][1][i-1], dp[first_color][2][i-1]) + R
        dp[first_color][1][i] = min(dp[first_color][0][i-1], dp[first_color][2][i-1]) + G
        dp[first_color][2][i] = min(dp[first_color][0][i-1], dp[first_color][1][i-1]) + B

print(min(dp[0][1][N-1], dp[0][2][N-1], dp[1][0][N-1], dp[1][2][N-1], dp[2][0][N-1], dp[2][1][N-1]))