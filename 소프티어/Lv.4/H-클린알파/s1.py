import sys

def p_n(base, p, n):
    result = base

    while n:
        if n % 2:
            result = (result * p) % 1000000007 
        p = (p ** 2) % 1000000007
        n //= 2

    return result

si = sys.stdin.readline

P, N = map(int, si().strip().split())
virus_inputs = list(map(int, si().strip().split()))
ans = 0

for i in range(N):
    ans = (ans + p_n(virus_inputs[i], P, (N - 1 - i))) % 1000000007
    
print(ans)