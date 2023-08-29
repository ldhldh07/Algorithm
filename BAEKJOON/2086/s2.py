import sys

MOD = 10 ** 9

def fibonacci(n):
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD
    return fib

a, b = map(int, input().strip().split())

fib = fibonacci(b)
answer = 0
for i in range(a, b+1):
    answer = (answer + fib[i]) % MOD

print(answer)
