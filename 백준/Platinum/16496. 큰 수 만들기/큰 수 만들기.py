def convert(n):
    length = len(n)
    n = int(n * (10 // length) + n[:10 % length])
    return n

N = int(input())
numbers = list(map(str, input().split()))

numbers.sort(key=lambda x: -convert(x))

print(int(''.join(numbers)))