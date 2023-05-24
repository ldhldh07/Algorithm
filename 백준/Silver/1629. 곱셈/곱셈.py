A, B, C = map(int, input().split())

num = 1
while B:
    if B % 2:
        num = num * A % C
    A = A ** 2 % C
    B = B // 2

print(num % C)