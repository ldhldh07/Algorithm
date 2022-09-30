T = 10

for _ in range(1, T+1):
    t = int(input())

    queue = list(map(int, input().split()))   # 큐 생성해줍니다
    n = 0

    while True:
        n = n % 5 + 1                         # 1,2,3,4,5 반복되게 합니다
        a = queue.pop(0)                      # dequeue 해줍니다
        queue.append(a - n)                   # dequeue값에서 n 뻬서 enqueue해줍니다
        if a - n <= 0:                        # 0 이하일 경우
            queue[7] = 0                      # 0으로 바꿔서 넣습니다
            break

    print('#{}'.format(t), *queue)