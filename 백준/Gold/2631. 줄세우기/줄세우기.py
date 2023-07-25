from bisect import bisect_left

N = int(input())

LIS = [int(input())]
len_LIS = 1
for _ in range(N-1):
    child_num = int(input())
    if LIS[-1] < child_num:
        LIS.append(child_num)
        len_LIS += 1
    else:
        LIS[bisect_left(LIS, child_num)] = child_num

print(N-len_LIS)