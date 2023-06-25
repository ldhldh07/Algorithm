import heapq

N = int(input())

smaller_priority_queue = []
larger_priority_queue = []

ans_list=[]

for length in range(1, 1+N):
    num = int(input())
    if length == 1:
        middle_num = num
    else:
        if num <= middle_num:
            heapq.heappush(smaller_priority_queue, -num)
            if not length % 2:
                heapq.heappush(larger_priority_queue, middle_num)
                middle_num = -heapq.heappop(smaller_priority_queue)
        else:
            heapq.heappush(larger_priority_queue, num)
            if length % 2:
                heapq.heappush(smaller_priority_queue, -middle_num)
                middle_num = heapq.heappop(larger_priority_queue)
    ans_list.append(middle_num)
print(*ans_list, sep='\n')