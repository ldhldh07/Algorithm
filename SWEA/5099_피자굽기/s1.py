T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = [0] * (N + 500)

    pizza =[0] * (M-N)
    for i, a in enumerate(arr, start=1):                         # 피자중에
        if i <= N:                                               # 화덕에 들어가는 양만큼은 enQueue해주고
            queue[i-1] = i, a
        else:                                                    # 나머지는 배열로 만들어둡니다
            pizza[i-1-N] = i, a

    front = -1
    rear = -1 + N                                                # 화덕 갯수만큼 들어와 있으니 rear 더해줍니다

    leftover = M - N                                             # 남은 피자수입니다
    while rear-front != 1:                                       # 큐에 하나만 남을 때까지 while문 해줍니다
        front += 1                                               # 맨 앞에있는 것을 deQueue 해줍니다
        if queue[front][1] // 2 == 0:                            # 빼려는 피자의 치즈를 //2 했을 때 0이 나오면
            if leftover > 0:                                     # 그때 아직 안넣은 피자가 있을 때만
                rear += 1                                        # 피자 넣어줍니다
                queue[rear] = pizza[M - N - leftover]            # 피자도 선입선출 느낌으로 빼줍니다
                leftover -= 1                                    # 남은 피자 하나 줄여줍니다
            else:                                                # 안넣은 피자가 없으면
                pass                                             # 그냥 빼고 끝입니다.

        else:                                                    # 0이 안나오면
            rear += 1
            queue[rear] = queue[front][0], queue[front][1] // 2  # 그 값을 반으로 나눠서 뒤에 더해줍니다

    print('#{} {}'.format(t, queue[rear][0]))
