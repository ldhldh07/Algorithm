# 분할정복을 통한 거듭제곱
# (A * B) % C = ((A % C) * (B % C)) % C
# 반복문 사용 

A, B, C = map(int, input().split())

num = 1
while B:
    if B % 2:
        num = num * A % C
    A = A ** 2 % C
    B = B // 2

print(num % C)
































































