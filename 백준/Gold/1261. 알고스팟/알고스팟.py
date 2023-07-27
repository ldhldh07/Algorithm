from collections import deque

def zero_one_bfs(start_node, m, n, miro):
    queue = deque([start_node])
    distances = [[n*m+1 for _ in range(m)] for _ in range(n)]
    distances[start_node[0]][start_node[1]] = 0

    while queue:
        current_i, current_j = queue.popleft()
        for delta_i, delta_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_i, next_j = current_i + delta_i, current_j + delta_j
            
            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m:
                continue
            
            if distances[next_i][next_j] > distances[current_i][current_j] + 1:
                if not miro[next_i][next_j]:
                    distances[next_i][next_j] = distances[current_i][current_j]
                    queue.appendleft((next_i, next_j))
                else:
                    distances[next_i][next_j] = distances[current_i][current_j] + 1
                    queue.append((next_i, next_j))
    return distances[n-1][m-1]

M, N = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
print(zero_one_bfs((0,0), M, N, miro))