import sys

def get_index(num, n):
    index = 0
    for i in range(1, n+1):
        index += min(num // i, n)
    return index


def binary_search(target, n):
    start, end = 0, n ** 2

    while start <= end:
        mid = (start + end) // 2

        mid_index = get_index(mid, n)
        if mid_index < target:
            start = mid + 1
        else:
            end = mid - 1

    return start


si = sys.stdin.readline

N, K = int(si().strip()), int(si().strip())

print(binary_search(K, N))