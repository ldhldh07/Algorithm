A, B = map(int, input().split())

def counting(N):
    result = 0
    i = 1
    while (1<<i-1) <= N:
        quotient = N // (1 << i)
        remainder = N % (1 << i)
        result += quotient * (1 << (i-1))
        if remainder >= (1 << i-1):
            result += remainder - (1<< i-1) + 1
        i += 1
    return result

print(counting(B)- counting(A-1))