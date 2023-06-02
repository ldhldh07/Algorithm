import heapq

T = int(input())
for _ in range(T):
    M = int(input())
    arr = []
    for a in range(M//10+1):
        arr.extend(list(map(int, input().split())))

    '''
    중앙값보다 작은 값들은 최대힙으로 입력
    큰 값들은 최소힙으로 입력
    '''
    left_max_heap = [] 
    right_min_heap = [] 

    for index, num in enumerate(arr):
        # 처음 값을 중앙값으로 지정
        if not index:
            mid_num = num
            center = 0
            answer = [mid_num]
        else:
            # 그 이후로는 이 중앙값 기준으로 작으면 왼쪽에 크면 오른쪽에 넣는다
            if num <= mid_num:
                heapq.heappush(left_max_heap, -num)
                center += 1
            if num > mid_num:
                center -= 1
                heapq.heappush(right_min_heap, num)
            # 홀수일때 체크
            if not index % 2:
                # 작은값이 두번 들어온 경우 중앙값이 기존 중앙값보다 하나 더 작은 값으로 바뀌어야 함
                if center == 2:
                    # 기존 중앙값은 오른쪽 최소힙에 넣고
                    heapq.heappush(right_min_heap, mid_num)
                    # 왼쪽 최대힙에서 최대값을 뽑아서 중앙값으로 재할당한다
                    mid_num = -heapq.heappop(left_max_heap)
                # 큰 값이 두번 들어온 경우 기존 중앙값보다 하나 더 큰 값으로 바뀌어야 함
                elif center == -2:
                    # 기존 중앙값은 왼쪽 최대힙에 넣고
                    heapq.heappush(left_max_heap, -mid_num)
                    # 오른쪽 최소힙에서 가장 작은 값을 빼서 중앙값으로 선정
                    mid_num = heapq.heappop(right_min_heap)
                # 센터값 초기화
                center = 0
                answer.append(mid_num)
    answer_length = M//2 + 1

    print(answer_length)
    for b in range(answer_length//10+1):
        print(*answer[10*b:10*(b+1)])




    
