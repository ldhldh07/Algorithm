import sys

si = sys.stdin.readline

N, K = map(int, si().strip().split())

S_list = list(map(int, si().strip().split()))

culcumative_sum = [0 for _ in range(N)]
culcumative_sum[0] = S_list[0]

for i in range(1, N):
    culcumative_sum[i] = culcumative_sum[i-1] + S_list[i]

culcumative_sum = [0] + culcumative_sum

for _ in range(K):
    A, B = map(int, si().strip().split())
    average = (culcumative_sum[B] - culcumative_sum[A-1]) / (B-A+1)
    print("{:.2f}".format(average))