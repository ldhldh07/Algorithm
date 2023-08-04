K, P, N = map(int, input().split())

while N:
    if N % 2:
        K = (K * P) % 1000000007 
    P = (P ** 2) % 1000000007
    N //= 2

print(K % 1000000007)