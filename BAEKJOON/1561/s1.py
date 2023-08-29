import sys

def get_count_time(i, times):
    result = 0
    for time in times:
        result += (i-1) // time  + 1
    return result


def binary_search(n, times):
    start, end = 0, n * max(times)

    while start <= end:
        mid = (start + end) // 2
        if get_count_time(mid, times) >= n:
            end = mid - 1
        else:
            start = mid + 1
    return end


si = sys.stdin.readline

N, M = map(int, si().strip().split())

times = list(map(int, si().strip().split()))

prefix_time = binary_search(N, times)
ridings = [index + 1 for index, time in enumerate(times) if not prefix_time % time]
last_index = N - get_count_time(prefix_time, times) - 1

print(ridings[last_index])