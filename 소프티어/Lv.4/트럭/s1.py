import sys

si = sys.stdin.readline

N = int(si().strip())
customers = []
max_car_size = 0
for _ in range(N):
    query = map(int, si().strip().split())
    customers.append(query)

M = int(si().strip())
Q_list = list(map(int, si().strip().split()))
max_Q = max(Q_list)
dp = [float('inf') for _ in range(max_Q+1)]

for A, *query in customers:
    temp_dp = [float('inf') for _ in range(max_Q + 1)]
    for i in range(A):
        car_size, offer = query[2 * i], query[2 * i+1]
        print(car_size, offer)
        for j in range(max_Q, -1, -1):
            temp_dp[j] = min(car_size if j-offer < 0 else dp[j-offer], temp_dp[j])
        print(temp_dp)
    dp = temp_dp

