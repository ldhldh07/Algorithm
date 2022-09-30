from collections import deque

T = 1

for _ in range(1, T+1):
    t = int(input())

    queue = deque(map(int, input().split()))
    n = 0

    while True:
        n = n % 5 + 1
        a = queue.popleft()
        queue.append(a - n)
        if a - n <= 0:
            queue[7] = 0
            break

print('#{}'.format(t), *queue)