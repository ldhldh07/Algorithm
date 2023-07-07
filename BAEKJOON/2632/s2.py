from collections import defaultdict

T = int(input())
m, n = map(int, input().split())
A = [0]+[int(input()) for _ in range(m)]
B = [0]+[int(input()) for _ in range(n)]
dp1, dp2 = defaultdict(int), defaultdict(int)
dp1[0], dp2[0] = 1, 1

# DP for the first pizza
for i in range(1, m+1):
    total = 0
    for j in range(i, m+i):
        total += A[j%m]
        if total > T: break
        dp1[total] += 1

# DP for the second pizza
for i in range(1, n+1):
    total = 0
    for j in range(i, n+i):
        total += B[j%n]
        if total > T: break
        dp2[total] += 1

# Check for all combinations
answer = dp1[T] + dp2[T]
for i in range(1, T):
    answer += dp1[i]*dp2[T-i]

print(answer)
