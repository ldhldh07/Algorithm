def bfs(n, m):
    queue = [0] * 2000001
    front = rear = -1
    rear += 1
    queue[rear] = n
    while queue:
        a = queue[front]
        front += 1

        for b in [a + 1, a - 1, a - 10, a * 2]:
            if b == m:
                return visited[a] + 1
            else:
                if visited[b] == -1 and 0 < b <1000000:
                    if a-m > 10 and a-1 == b:
                        continue
                    rear += 1
                    queue[rear] = b
                    visited[b] = visited[a] + 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [-1] * 2000001
    visited[N] = 0

    print('#{} {}'.format(tc, bfs(N, M)))
