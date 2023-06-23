from collections import deque

def bfs(start, end):
    queue = deque([start])
    visited = [-1] * (10 ** 5 + 1)
    visited[start] = 0

    while queue:
        node = queue.popleft()
        if node == end:
            return visited[node]
        for next_node in (node-1, node+1, node*2):
            if 0 <= next_node < 10 ** 5 + 1 and visited[next_node] == -1:
                queue.append(next_node)
                visited[next_node] = visited[node] + 1

start, end = map(int, input().split())
print(bfs(start, end))