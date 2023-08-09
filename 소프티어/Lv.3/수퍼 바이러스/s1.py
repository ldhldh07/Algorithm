import sys

si = sys.stdin.readline

K, P, N = map(int, si().strip().split())

second = 10 * N
ans = K

while second:
    if second % 2:
        ans = (ans * P) % 1000000007
    P = (P ** 2) % 1000000007
    second //= 2

print(ans)