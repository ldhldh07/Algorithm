def binary_search(value, array, n):
    start, end = 0, n - 1
    while start < end:
        mid = (start + end) // 2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            start = mid + 1
        elif array[mid] > value:
            end = mid - 1
    if array[start] == -value:
        start += 1
    elif array[end] == -value:
        end -= 1
    return array[start] if value - array[start] > array[end] - value else array[end]


N = int(input())
solutions = list(map(int, input().split()))
middle = N//2 + 1 if N % 2 else N//2
min_diff = 2 * 10 ** 9 + 1
for i in range(middle):
    diff = abs(solutions[i] + binary_search(-solutions[i], solutions, N))
    if diff <= min_diff:
        min_diff = min(min_diff, diff)
        answer = (solutions[i], binary_search(-solutions[i], solutions, N))

print(*answer)