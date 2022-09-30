T = int(input())

for t in range(1, 1 + T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split())) + [0] * M   # 입력된 숫자 뒤에 M개의 0이 더해진 큐를 만들어줍니다

    front = -1
    rear = -1 + N                                       # 첫 rear 값은 큐 마지막 원소의 위치로 해줍니다

    for i in range(M):                                  # m번동안
        front += 1                                      # dequeue하고
        rear += 1                                       # 그 값을 enqueue해줍니다
        queue[rear] = queue[front]

    print('#{} {}'.format(t, queue[front + 1]))