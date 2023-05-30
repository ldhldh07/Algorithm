N, K = map(int, input().split())

dp = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    # n-1번째 물품인거임
    # 그 물건의 무게 W, 가치 V
    W, V = map(int, input().split())
    for k in range(K):
        # 이 물건의 무게만큼 이전 dp의 값에 물건의 가치를 더해 버린값과
        # 그 물건이 안들어갔을 때의 최대 가치값과 비교해서 더 큰 값
        # k-W가 0 이상일때만
        if k-W+1 >= 0:
            # 첫번째 물건 넣을 때는 n-1이랑 비교 안해도 됨
            if not n:
                dp[n][k] = dp[n-1][k-W] + V
            # dp[n][k] = max(dp[n-1][k], V)
            dp[n][k] = max(dp[n-1][k], dp[n-1][k-W] + V)
        # k-W가 0보다 작을 때는 또 그냥 n-1이랑만 비교하면 됨
        else:
            if n:
                dp[n][k] = dp[n-1][k]
print(dp)
print(dp[N][K])