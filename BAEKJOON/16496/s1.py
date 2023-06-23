def convert(n):
    index = 0
    while n >= 10:
        index += 1
        n /= 10
    return n, index

N = int(input())
numbers = list(map(int, input().split()))
tuple_list = []


numbers.sort(key=lambda x: (int(-convert(x)[0]), convert(x)[1],-convert(x)[0]))

print(*numbers, sep='')