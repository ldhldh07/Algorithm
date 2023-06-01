import heapq

T = int(input())
for _ in range(T):
    M = int(input())
    arr = []
    for a in range(M//10+1):
        arr.extend(list(map(int, input().split())))

    right_min_heap = [] 
    left_max_heap = [] 
    for index, num in enumerate(arr):
        if not index:
            mid_num = num
            center = 0
            answer = [mid_num]
        else:

            if num <= mid_num:
                heapq.heappush(left_max_heap, -num)
                center += 1
            if num > mid_num:
                center -= 1
                heapq.heappush(right_min_heap, num)
            if not index % 2:
                # 기존 중앙값보다 방금 들어간 두 값이 두개 다 작으면
                if center == 2:
                    # 기존 중앙값은 오른쪽 최소힙에 넣고
                    heapq.heappush(right_min_heap, mid_num)
                    # 왼쪽 리스트에서 가장 큰 값을 중앙값으로 재설정
                    mid_num = -heapq.heappop(left_max_heap)
                # 방금 들어간 두 값이 두개 다 크면
                elif center == -2:
                    # 기존 중앙값은 왼쪽 최대힙에 넣고
                    heapq.heappush(left_max_heap, -mid_num)
                    # 오른쪽 최소값을 중앙값으로
                    mid_num = heapq.heappop(right_min_heap)
                center = 0
                answer.append(mid_num)
    answer_length = M//2 + 1

    print(answer_length)
    for b in range(answer_length//10+1):
        print(*answer[10*b:10*(b+1)])