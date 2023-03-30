# 분할정복을 통한 거듭제곱
# (A * B) % C = ((A % C) * (B % C)) % C
# 재귀 사용 

def power_mod(a, b, c):
    if b == 0:
        return 1
    if b % 2 == 0:
        temp = power_mod(a, b // 2, c)
        return temp * temp % c
    else:
        return a * power_mod(a, b - 1, c) % c

A, B, C = 10, 11, 12
print(power_mod(A, B, C))