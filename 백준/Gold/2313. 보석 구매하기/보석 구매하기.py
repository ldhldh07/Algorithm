n = int(input())

ans = 0
index_list = []
for _ in range(n):
    L = int(input())
    value_list = list(map(int, input().split()))
    max_sum = float('-inf')
    max_start = -1
    max_end = -1
    sum = 0
    start = 0
    for index, value in enumerate(value_list):
        if sum <= 0:
            sum, start = value, index
        else:
            sum += value
        
        if sum > max_sum or (sum == max_sum and max_end-max_start > index-start):
            max_sum = sum
            max_start = start + 1
            max_end = index + 1

    ans += max_sum
    index_list.append((max_start, max_end))

print(ans)
for index1, index2  in index_list:
    print(index1, index2)