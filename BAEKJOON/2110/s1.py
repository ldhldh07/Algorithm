import sys

def binary_search(array, n):
    start, end = 0, n-1
    target = (array[end] + array[start]) / 2

    while start <= end:
        # if start > end:
            
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1 
    
    return end if target - array[end] < array[start] - target else start


si = sys.stdin.readline

# N, C = map(int, si().strip().split())

# homes = sorted([int(si().strip()) for _ in range(N)])
array = [1, 2, 3, 4, 6, 8, 11]

print(binary_search(array,7))
# print(binary_search(homes, N))