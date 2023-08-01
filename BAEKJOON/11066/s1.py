T = int(input())
ans_list = []

for _ in range(T):
    K = int(input())
    file_list = list(map(int, input().split()))

    max_size = 10 ** 4 + 1

    dp = [[max_size for _ in range(K)] for _ in range(K)]
    file_size = [[0 for _ in range(K)] for _ in range(K)]

    for i in range(K):
        dp[i][i] = 0
        file_size[i][i] = file_list[i]

    for length in range(2, K+1):
        for i in range(K-length+1):
            j = i + length - 1
            file_size[i][j] = file_size[i][j-1] + file_list[j]
            for middle in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][middle] + dp[middle+1][j] + file_size[i][j])

    ans_list.append(dp[0][K-1])

print(*ans_list, sep='\n')
