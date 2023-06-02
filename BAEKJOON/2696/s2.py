import heapq

# T = int(input())
# for _ in range(T):
M = int(input())
arr = []
for a in range(M//10+1):
    arr.extend(list(map(int, input().split())))

num_list = [] 
center_move = 0
for index, num in enumerate(arr):
    if not index:
        mid_index = 0
        mid_num = num
    num_list.append(num)
    print(num_list)
    if num > mid_num:
        center_move += 1
    if num < mid_num:
        center_move -= 1
    
    if not index % 2:
        print('리스트에서 중앙값을 찾아보자')