import sys

def binary_search_distance(homes, n, c):

    start, end = 0, homes[-1] - homes[0]

    while start <= end:
        mid = (start + end) // 2
        count_of_mid = get_count(mid, homes, n)
        if count_of_mid < c:
            end = mid - 1
        else:
            start = mid + 1
    
    return end


def get_count(min_dist, homes, n):
    count = 1
    prev_point = homes[0]

    for i in range(1, n):
        if homes[i] - prev_point >= min_dist:
            count += 1
            prev_point = homes[i]

    return count


si = sys.stdin.readline

N, C = map(int, si().strip().split())

homes = sorted([int(si().strip()) for _ in range(N)])


print(binary_search_distance(homes, N, C))