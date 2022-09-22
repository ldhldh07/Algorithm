N = int(input())

arr = list(map(int, input().split()))

plus = [0] * N
minus = [0] * N
plus[0] = minus[0] = 1

for i in range(N-1):
    if arr[i] == arr[i+1]:
        plus[i+1] = plus[i] + 1
        minus[i+1] = minus[i] + 1
    elif arr[i] < arr[i+1]:
        plus[i+1] = plus[i] + 1
        minus[i+1] = 1
    else:
        plus[i+1] = 1
        minus[i+1] = minus[i] + 1

print(max(plus + minus))
