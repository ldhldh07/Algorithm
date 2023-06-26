from collections import defaultdict
import copy

N = int(input())
weights = list(map(int, input().split()))


dp = [0 for _ in range(40001)]
dp[0] = 1

max_weight = sum(weights)

for weight in range(N):
    next_dp = dp.copy()
    current_weight = weights[weight]
    for check_weight in range(max_weight - current_weight + 1):
        if dp[check_weight]:
            next_dp[check_weight + current_weight] = 1
            next_dp[abs(check_weight - current_weight)] = 1
    dp = next_dp

check_N = int(input())
check_weights = list(map(int, input().split()))

ans_list = []
for check_weight in check_weights:
    ans_list.append('Y' if dp[check_weight] else 'N')

print(*ans_list)