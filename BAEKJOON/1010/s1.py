N = int(input())
for _ in range(N):
    N, M = map(int, input().split())
    dp = [1, 1]
    # M까지의 팩토리얼의 리스트를 만들어줍니다.
    for n in range(M+1):
        if n > 1:
            dp.append(dp[n-1] * n)
    # 팩토리얼을 이용해서 순열의 공식을 구합니다.
    print(dp[M] //  (dp[M-N] * dp[N]))
