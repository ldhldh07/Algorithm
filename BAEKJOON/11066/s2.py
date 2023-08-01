def prefix_sum(i, j):
    return cumulative_sum[j] - (cumulative_sum[i-1] if i else 0)

T = int(input())
ans_list = []

for _ in range(T):
    K = int(input())
    file_list = list(map(int, input().split()))

    max_size = float('inf')

    dp = [[max_size for _ in range(K)] for _ in range(K)]
    cumulative_sum = [0 for _ in range(K)]

    cumulative_sum[0] = file_list[0]
    for i in range(1, K):
        cumulative_sum[i] = cumulative_sum[i-1] + file_list[i]

    for i in range(K):
        dp[i][i] = 0

    for length in range(2, K+1):
        for i in range(K-length+1):
            j = i + length - 1
            for middle in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][middle] + dp[middle+1][j] + prefix_sum(i, j))

    ans_list.append(dp[0][K-1])

print(*ans_list, sep='\n')
