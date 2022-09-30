from collections import deque


def bfs(m):
    while True:
        a = queue.popleft()
        for b in [a + 1, a - 1, a * 2, a - 10]:
            if b == m:
                return visited[a] + 1
            else:
                if not visited[b] and 1000000 > b > 0:
                    queue.append(b)
                    visited[b] = visited[a] + 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    queue = deque([N])
    visited = [0] * 2000001

    print('#{} {}'.format(tc, bfs(M)))
