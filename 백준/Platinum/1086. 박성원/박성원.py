import sys, math

si = sys.stdin.readline

N = int(si().strip())
nums = [int(si().strip()) for _ in range(N)]
K = int(si().strip())
remainders = [[((prev_remainder * 10**len(str(num))) % K + num) % K for prev_remainder in range(K)] for num in nums]

dp = [[0 for _ in range(K)] for _ in range(1 << N)]

dp[0][0] = 1
for mask in range(1<<N):
    for current_num in range(N):
        if not mask & (1 << current_num):
            for remainder in range(K):
                dp[mask | (1 << current_num)][remainders[current_num][remainder]] += dp[mask][remainder]

zero_case = dp[(1<<N)-1][0]
total_case = sum(dp[(1<<N)-1])

div = math.gcd(zero_case, total_case)

print("{}/{}".format(zero_case // div, total_case // div))