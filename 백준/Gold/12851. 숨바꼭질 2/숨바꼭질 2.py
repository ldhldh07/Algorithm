from collections import deque

def bfs(start, end):
    queue = deque([start])
    visited = [[-1, 0] for _ in range(10 ** 5 + 1)]
    visited[start] = [0, 1]

    while queue:
        node = queue.popleft()
        for next_node in (node-1, node+1, node*2):
            if 0 <= next_node < 10 ** 5 + 1:
                if visited[next_node][0] == -1:
                    queue.append(next_node)
                    visited[next_node][0] = visited[node][0] + 1
                    visited[next_node][1] = visited[node][1]
                elif visited[next_node][0] == visited[node][0] + 1:
                    visited[next_node][1] += visited[node][1]
    return visited
start, end = map(int, input().split())
print(*bfs(start, end)[end], sep='\n')