N, S = map(int, input().split())
numbers = list(map(int, input().split()))

all_sum = sum(numbers)

if all_sum < S:
    print(0)
else:
    start = -1
    end = -1
    num_sum = 0
    min_length = 10 ** 5
    while start <= end:
        if num_sum < S:
            if end == N-1:
                break
            end += 1
            num_sum += numbers[end]
        else:
            if start == end:
                break
            if end-start < min_length:
                min_length = end-start
            start += 1
            num_sum -= numbers[start]
    print(min_length)