def bisect_left(target, num_list):
    start = 0
    end = len(num_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if num_list[mid] == target:
            return mid
        
        elif num_list[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return start


N = int(input())
array = list(map(int, input().split()))

LIS = [array[0]]
for i in range(1, N):
    if array[i] > LIS[-1]:
        LIS.append(array[i])
    else:
        LIS[bisect_left(array[i], LIS)] = array[i]

print(len(LIS))