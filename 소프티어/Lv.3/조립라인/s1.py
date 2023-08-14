import sys

si = sys.stdin.readline

N = int(si().strip())

A, B, *prev_move = map(int, si().strip().split())
dp = [A, B]

for i in range(1, N):
    A, B, *move = map(int, si().strip().split())
    new_dp = [0, 0]

    new_dp[0] = min(dp[0], dp[1] + prev_move[1]) + A
    new_dp[1] = min(dp[1], dp[0] + prev_move[0]) + B
    
    dp = new_dp
    if i == N-1:
        continue
        
    prev_move = move


print(min(dp))